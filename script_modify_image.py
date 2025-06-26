from PIL import Image
import os

# Chemin du répertoire contenant les images
input_dir = "C:/Users/Administrateur/OneDrive/Documents/STAGE/projet/image/beauté"
# Chemin du répertoire de sortie pour les images transformées
output_dir = "C:/Users/Administrateur/OneDrive/Documents/STAGE/projet/image converti/beauté converti"

# Créer le répertoire de sortie s'il n'existe pas
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Taille cible (800x800 pixels)
target_size = (800, 800)
# Taille maximale du fichier (50 Ko)
max_file_size = 50 * 1024  # 50 Ko en octets

# Parcourir tous les fichiers dans le répertoire source
for filename in os.listdir(input_dir):
    # Vérifier si le fichier est une image (extensions courantes)
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
        # Chemin complet du fichier source
        input_path = os.path.join(input_dir, filename)
        # Charger l'image
        with Image.open(input_path) as img:
            # Redimensionner l'image en 800x800 pixels (mode 'thumbnail' conserve le ratio)
            img.thumbnail(target_size)
            
            # Créer une nouvelle image carrée de 800x800 pixels avec fond blanc
            new_img = Image.new("RGB", target_size, (255, 255, 255))
            # Coller l'image redimensionnée au centre
            new_img.paste(img, ((target_size[0] - img.width) // 2, (target_size[1] - img.height) // 2))
            
            # Chemin complet du fichier de sortie (même nom, mais en .webp)
            output_filename = os.path.splitext(filename)[0] + ".webp"
            output_path = os.path.join(output_dir, output_filename)
            
            # Enregistrer l'image en WebP avec une qualité ajustée pour respecter la taille maximale
            quality = 90  # Qualité initiale
            while quality >= 10:  # Ne pas descendre en dessous de 10% de qualité
                new_img.save(output_path, "WEBP", quality=quality)
                # Vérifier la taille du fichier
                if os.path.getsize(output_path) <= max_file_size:
                    print(f"Image {filename} transformée et sauvegardée en {output_filename} (qualité: {quality}%)")
                    break
                else:
                    # Réduire la qualité de 10% à chaque itération
                    quality -= 10
                    os.remove(output_path)  # Supprimer le fichier trop volumineux
            else:
                print(f"Impossible de réduire {filename} en dessous de 50 Ko sans perte de qualité excessive.")

print("Traitement terminé !")