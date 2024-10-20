from ultralytics import YOLO
import cv2

# Carregar o modelo treinado
model = YOLO('runs/detect/train12/weights/best.pt')  # Caminho para o modelo salvo após o treino

# Fazer inferência em uma nova imagem
path_image = ['./dataset3/test/cheio.jpg', './dataset3/test/meio_cheio.jpg', './dataset3/test/vazio.jpg']
for i in path_image:
    results = model.predict(i, conf=0.95, imgsz=800)
    results[0].show()