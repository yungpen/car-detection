# Car Detection (VisDrone)

**Доступен по адресу:** [тут](https://car-detection-aqhzxgsqbr73brzrg86snp.streamlit.app/)

---

### Результаты (Metrics)
Модель дообучена на датасете VisDrone (5 эпох).

| Класс | Images | Instances | mAP50 | mAP50-95 |
| :--- | :--- | :--- | :--- | :--- |
| **All (все классы)** | 519 | 36451 | **0.195** | 0.107 |
| **Car (автомобиль)** | 487 | 13208 | **0.642** | 0.404 |
| **Pedestrian (пешеход)** | 491 | 8415 | **0.215** | 0.078 |

---

### Инструкция по установке и запуску
```text
1. Клонировать репозиторий и перейти в него:
git clone https://github.com/yungpen/car-detection
cd car-detection

2. Настроить окружение (Windows PowerShell):
python -m venv venv
.\venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt

3. Запустить сервис:
streamlit run app.py
---
 Структура проекта:
app.py — Веб-интерфейс на Streamlit.
runs/detect/train/weights/best.pt — Обученные веса модели.
train.py — Скрипт для дообучения модели.
convert.py — Скрипт конвертации аннотаций VisDrone.
VisDrone.yaml — Конфигурация датасета.
report.md — Отчет о результатах.
requirements.txt — Список зависимостей.
