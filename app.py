import streamlit as st
from ultralytics import YOLO
from PIL import Image
import os

def main():
    st.set_page_config(page_title="Детектор автотранспорта")
    st.title("Детектор автотранспорта")
    
    # Настройки в боковой панели
    st.sidebar.header("Параметры")
    
    # Выбор модели
    model_choice = st.sidebar.radio(
        "Выберите модель:",
        ("Базовая (YOLO11n)", "Обученная (VisDrone)")
    )
    
    # Слайдер для настройки чувствительности
    conf_level = st.sidebar.slider("Порог уверенности", 0.1, 0.9, 0.25)

    # Определение пути к файлу модели
    if model_choice == "Базовая (YOLO11n)":
        path = 'yolo11n.pt'
    else:
        path = 'runs/detect/train/weights/best.pt'

    if os.path.exists(path):
        model = YOLO(path)
        file = st.file_uploader("Загрузить фото", type=["jpg", "jpeg", "png"])
        
        if file:
            img = Image.open(file)
            
            # Запуск обработки
            results = model(img, conf=conf_level)
            
            # Считаем количество найденных объектов
            count = len(results[0].boxes)
            st.subheader(f"Результат анализа (найдено объектов: {count})")
            
            # Отрисовка результата
            for r in results:
                res_image = r.plot()
                st.image(res_image, channels="BGR", use_container_width=True)
    else:
        st.error(f"Ошибка: файл {path} не найден. Проверьте пути.")

if __name__ == '__main__':
    main()