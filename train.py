from ultralytics import YOLO
import os

def train():
    # Получаем полный путь к текущей папке
    base_path = os.getcwd()
    yaml_path = os.path.join(base_path, 'data', 'VisDrone.yaml')
    
    model = YOLO('yolo11n.pt')
    
    # Запускаем с указанием пути
    model.train(data=yaml_path, epochs=5, imgsz=640)

if __name__ == '__main__':
    train()