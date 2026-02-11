import os
import csv
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
import matplotlib.pyplot as plt
import re

# --- Config Tesseract ---
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
os.environ['TESSDATA_PREFIX'] = "C:\\Program Files\\Tesseract-OCR\\tessdata"

# --- Fonction pour afficher une image ---
def show_image(img, title="Image"):
    plt.figure(figsize=(8,6))
    plt.imshow(img, cmap='gray')
    plt.title(title)
    plt.axis('off')
    plt.show()

# --- Fonction de correction simple du texte OCR ---
def correction_texte(texte):
    # Remplacements fréquents
    corrections = {
        '0': 'O',
        '1': 'l',
        '5': 'S',
        '6': 'G',
        '8': 'B',
        '+': 't',
        '@': 'a',
    }
    for k, v in corrections.items():
        texte = texte.replace(k, v)
    # Nettoyage général
    texte = re.sub(r'[^\x00-\x7F\u00C0-\u017F\s\.,;:!?-]', '', texte)
    texte = re.sub(r'\s+', ' ', texte).strip()
    return texte

# --- Fonction OCR adaptative améliorée ---
def ocr_adaptatif(image_path, lang='fra+eng', afficher=False):
    original = Image.open(image_path)
    images_a_tester = [original]

    # Gris
    gray = original.convert('L')
    images_a_tester.append(gray)

    # Contraste
    enhancer = ImageEnhance.Contrast(gray)
    contrast = enhancer.enhance(2.0)
    images_a_tester.append(contrast)

    # Binarisation avec plusieurs seuils
    for seuil in [120, 140, 160]:
        binarized = contrast.point(lambda x: 0 if x < seuil else 255)
        images_a_tester.append(binarized)

    # Redimensionner si trop petite
    for i in range(len(images_a_tester)):
        w, h = images_a_tester[i].size
        if w < 800:
            images_a_tester[i] = images_a_tester[i].resize((w*2, h*2))

    # Filtrage optionnel pour réduire le bruit
    for i in range(len(images_a_tester)):
        img = images_a_tester[i]
        if img.mode != 'L':
            img = img.convert('L')
        images_a_tester[i] = img.filter(ImageFilter.MedianFilter(3))

    # Tester et choisir le meilleur texte
    meilleur_texte = ""
    image_finale = original
    for img in images_a_tester:
        try:
            texte = pytesseract.image_to_string(img, lang=lang, config='--oem 3 --psm 6').strip()
            texte = correction_texte(texte)
            if texte and len(texte) > len(meilleur_texte):
                meilleur_texte = texte
                image_finale = img
        except:
            continue

    if afficher:
        show_image(image_finale, f"OCR: {os.path.basename(image_path)}")

    return meilleur_texte, image_finale

# --- Parcourir dossier d’images ---
dossier_images = 'image/'  # ton dossier
fichiers = [f for f in os.listdir(dossier_images) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

# --- CSV pour stocker résultats ---
csv_file = 'ocr_results_ameliore1.csv'
with open(csv_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Image', 'Texte_extrait'])

    for fichier in fichiers:
        chemin = os.path.join(dossier_images, fichier)
        texte, img_utilisee = ocr_adaptatif(chemin, afficher=False)
        writer.writerow([fichier, texte])
        print(f"\n--- {fichier} ---")
        print("Texte extrait (aperçu) :", texte[:200], '...')  # aperçu du texte

print(f"\n✅ OCR terminé ! Les résultats sont enregistrés dans {csv_file}")
