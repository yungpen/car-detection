import os
from PIL import Image
from tqdm import tqdm
from pathlib import Path

def convert_visdrone(base_path):
    for folder in ['VisDrone2019-DET-train', 'VisDrone2019-DET-val']:
        path = Path(base_path) / folder
        img_dir = path / 'images'
        ann_dir = path / 'annotations'
        out_dir = path / 'labels'
        out_dir.mkdir(parents=True, exist_ok=True)

        print(f"Конвертация {folder}...")
        for ann_file in tqdm(list(ann_dir.glob('*.txt'))):
            img_file = img_dir / (ann_file.stem + '.jpg')
            if not img_file.exists():
                continue
                
            img = Image.open(img_file)
            width, height = img.size
            
            lines = []
            with open(ann_file, 'r') as f:
                for line in f:
                    data = line.strip().split(',')
                    if len(data) < 8: continue
                    
                    # Извлекаем данные (VisDrone: class на 5-м месте)
                    # Формат: left, top, width, height, score, category, ...
                    cls = int(data[5]) - 1 
                    if cls < 0: continue # игнорируем класс 0
                    
                    # Конвертация в YOLO формат
                    box = [float(x) for x in data[:4]]
                    x_center = (box[0] + box[2] / 2) / width
                    y_center = (box[1] + box[3] / 2) / height
                    w = box[2] / width
                    h = box[3] / height
                    
                    lines.append(f"{cls} {x_center:.6f} {y_center:.6f} {w:.6f} {h:.6f}\n")
            
            with open(out_dir / ann_file.name, 'w') as f:
                f.writelines(lines)

if __name__ == '__main__':
    convert_visdrone('data')