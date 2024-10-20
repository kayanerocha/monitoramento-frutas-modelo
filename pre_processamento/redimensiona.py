from PIL import Image
import os

def resize_images(input_dir, output_dir, size=(100, 100)):
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            img_path = os.path.join(input_dir, filename)
            img = Image.open(img_path)
            img = img.resize(size, Image.LANCZOS)  # Redimensiona mantendo a qualidade
            img.save(os.path.join(output_dir, filename))

# Exemplo de uso
resize_images('C:/Users/oi416936/Pessoal/Projetos/TCC/reconhecimento_volumes/imagens', 'C:/Users/oi416936/Pessoal/Projetos/TCC/reconhecimento_volumes/imagens_dimensionadas', size=(800, 800))
