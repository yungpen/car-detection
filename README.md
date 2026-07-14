Car Detection (VisDrone)
Сервис для детекции автотранспорта и пешеходов на аэрофотоснимках.
Доступен по адресу: Нажми сюда
📦 Веса моделей
Обученная модель (YOLO11n-VisDrone): best.pt
Базовая модель: yolo11n.pt
📋 Результаты (Metrics)
Модель дообучена на датасете VisDrone (5 эпох).
Класс	Images	Instances	mAP50	mAP50-95
All (все классы)	519	36451	0.195	0.107
Car (автомобиль)	487	13208	0.642	0.404
Pedestrian (пешеход)	491	8415	0.215	0.078
⚙️ Инструкция по установке
Клонировать репозиторий:
code
Bash
git clone https://github.com/yungpen/car-detection
cd car-detection
Настроить окружение (Windows PowerShell):
code
Powershell
python -m venv venv
.\venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
Запустить сервис:
code
Bash
streamlit run app.py
📂 Структура проекта
app.py — Веб-интерфейс на Streamlit.
train.py — Скрипт для дообучения модели.
convert.py — Скрипт конвертации аннотаций VisDrone.
VisDrone.yaml — Конфигурация датасета.
report.md — Отчет о результатах.
requirements.txt — Список зависимостей.
