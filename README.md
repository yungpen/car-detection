# Car Detection (VisDrone)
Сервис для детекции автотранспорта и пешеходов на аэрофотоснимках.

**Доступен по адресу:** [тут](https://car-detection-aqhzxgsqbr73brzrg86snp.streamlit.app/)

---

### 📦 Веса моделей
* **Обученная модель (best.pt):** [Скачать](https://github.com/yungpen/car-detection/blob/main/runs/detect/train/weights/best.pt)
* **Базовая модель:** [yolo11n.pt](https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo11n.pt)

---

### 📊 Результаты (Metrics)
Модель дообучена на датасете VisDrone (5 эпох).

| Класс | Images | Instances | mAP50 | mAP50-95 |
| :--- | :--- | :--- | :--- | :--- |
| **All (все классы)** | 519 | 36451 | **0.195** | 0.107 |
| **Car (автомобиль)** | 487 | 13208 | **0.642** | 0.404 |
| **Pedestrian (пешеход)** | 491 | 8415 | **0.215** | 0.078 |

---

### ⚙️ Инструкция по установке

#### 1. Клонирование репозитория
```bash
git clone https://github.com/yungpen/car-detection
cd car-detection
#### 2. **Настройка окружения**
```powershell
python -m venv venv
.\venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt

#### 3. **Запуск сервиса**
```bash
streamlit run app.py
#### **Структура проекта**
app.py           - Веб-интерфейс на Streamlit.
train.py         - Скрипт для дообучения модели.
convert.py       - Скрипт конвертации аннотаций VisDrone.
VisDrone.yaml    - Конфигурация путей и классов.
report.md        - Отчет о результатах и метриках.
requirements.txt - Список всех зависимостей.
best.pt          - Обученные веса модели YOLO11n.
