import os
import glob

def rename_images_and_labels(image_dir, label_dir, output_image_dir, output_label_dir, prefix="dataset"):
    # Criar diretórios de saída se não existirem
    os.makedirs(output_image_dir, exist_ok=True)
    os.makedirs(output_label_dir, exist_ok=True)
    
    # Listar todas as imagens e rótulos (assumindo que as imagens são .jpg e rótulos .txt)
    image_files = glob.glob(os.path.join(image_dir, "*.jpg"))
    label_files = glob.glob(os.path.join(label_dir, "*.txt"))
    
    # Ordenar os arquivos para garantir correspondência correta entre imagens e rótulos
    image_files.sort()
    label_files.sort()
    
    for i, (image_file, label_file) in enumerate(zip(image_files, label_files)):
        # Novo nome base para imagem e rótulo (prefixo + número sequencial)
        new_base_name = f"{prefix}_{i+1:04d}"  # Exemplo: "dataset_0001"

        # Renomear e mover a imagem
        new_image_name = os.path.join(output_image_dir, new_base_name + ".jpg")
        os.rename(image_file, new_image_name)

        # Renomear e mover o rótulo
        new_label_name = os.path.join(output_label_dir, new_base_name + ".txt")
        os.rename(label_file, new_label_name)

        print(f"Renomeado: {image_file} -> {new_image_name}")
        print(f"Renomeado: {label_file} -> {new_label_name}")

# Exemplo de uso
if __name__ == "__main__":
    image_directory = "./dataset/Orange"  # Diretório das imagens
    label_directory = "./dataset/Orange/rotulos_txt"  # Diretório dos rótulos (arquivos .txt)
    output_image_directory = "./dataset/Orange/imagens_renomeadas"  # Diretório de saída para as imagens renomeadas
    output_label_directory = "./dataset/Orange/rotulos_renomeados"  # Diretório de saída para os rótulos renomeados
    prefix = "laranja1"  # Prefixo para os novos arquivos (pode ser personalizado)

    rename_images_and_labels(image_directory, label_directory, output_image_directory, output_label_directory, prefix)
