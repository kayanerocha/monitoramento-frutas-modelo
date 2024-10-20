from ultralytics import YOLO

# Carregar o modelo YOLOv8 pré-treinado
model = YOLO('yolov8n.pt')  # Você pode usar outros como 'yolov8s.pt' ou 'yolov8m.pt'

# Treinar o modelo com seus próprios dados
model.train(data='dataset3/data.yaml', epochs=10, imgsz=100)

model.val()
