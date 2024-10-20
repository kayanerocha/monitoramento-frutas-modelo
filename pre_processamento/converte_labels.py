import os
import json
import glob

def convert_labelme_to_yolo(json_file, output_dir, class_mapping):
    # Abrindo o arquivo JSON gerado pelo Labelme
    with open(json_file, 'r') as f:
        data = json.load(f)

    image_width = data['imageWidth']
    image_height = data['imageHeight']
    
    # Nome do arquivo txt de saída será o mesmo nome da imagem, mas com extensão .txt
    txt_file_name = os.path.join(output_dir, os.path.basename(json_file).replace('.json', '.txt'))
    
    with open(txt_file_name, 'w') as txt_file:
        for shape in data['shapes']:
            label = shape['label']
            points = shape['points']  # Coordenadas dos pontos da bounding box
            
            # Converter as coordenadas dos pontos (Labelme dá 4 pontos para caixas delimitadoras)
            x_min = min([p[0] for p in points])
            y_min = min([p[1] for p in points])
            x_max = max([p[0] for p in points])
            y_max = max([p[1] for p in points])

            # Calcular YOLO format (x_center, y_center, width, height)
            x_center = (x_min + x_max) / 2.0 / image_width
            y_center = (y_min + y_max) / 2.0 / image_height
            width = (x_max - x_min) / image_width
            height = (y_max - y_min) / image_height

            # Identificar o índice da classe (mapeamento)
            class_id = class_mapping.get(label, -1)
            if class_id == -1:
                print(f"Warning: Label '{label}' not found in class mapping!")
                continue

            # Escrever a linha no formato YOLO (class_id, x_center, y_center, width, height)
            txt_file.write(f"{class_id} {x_center} {y_center} {width} {height}")


def batch_convert_labelme_to_yolo(input_dir, output_dir, class_mapping):
    # Criar diretório de saída se não existir
    os.makedirs(output_dir, exist_ok=True)

    # Procurar todos os arquivos .json no diretório de entrada
    json_files = glob.glob(os.path.join(input_dir, "*.json"))

    # Converter cada arquivo
    for json_file in json_files:
        convert_labelme_to_yolo(json_file, output_dir, class_mapping)

# Exemplo de uso
if __name__ == "__main__":
    input_directory = "./dataset/Orange/rotulos"  # Diretório contendo os arquivos .json do Labelme
    output_directory = "./dataset/Orange/rotulos_txt"  # Diretório para salvar os arquivos .txt
    class_mapping = {
        "maca": 0,
        "banana": 1,
        "laranja": 2,
    }  # Mapeamento das classes (substituir pelas suas classes)

    batch_convert_labelme_to_yolo(input_directory, output_directory, class_mapping)
