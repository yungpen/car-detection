# Car Detection (VisDrone)
Сервис для детекции автотранспорта и пешеходов на аэрофотоснимках.

**Доступен по адресу:** https://car-detection-aqhzxgsqbr73brzrg86snp.streamlit.app/

### Веса моделей
*   **Обученная модель (YOLO11n-VisDrone):** [ВСТАВЬ_ССЫЛКУ_НА_GOOGLE_ДИСК_ЗДЕСЬ]
*   **Базовая модель:** [yolo11n.pt](https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo11n.pt)

### Стек технологий
*   Python
*   Ultralytics (YOLO11)
*   Streamlit
*   PyTorch

### Требования
*   Python 3.10+

### Подготовка к установке
Клонировать репозиторий и перейти в него в командной строке:
```bash
git clone https://github.com/твой_логин/MyCarDetection
cd MyCarDetection

Локальный запуск
Установить и активировать виртуальное окружение, обновить менеджер пакетов pip:
Windows (PowerShell):

python -m venv venv
.\venv\Scripts\activate
python -m pip install --upgrade pip

Git Bash / Linux:

python -m venv venv
source venv/Scripts/activate
python -m pip install --upgrade pip

Установить все зависимости из файла requirements.txt:
pip install -r requirements.txt

Запустить сервис:
streamlit run app.py

Результаты (Metrics)
Модель дообучена на датасете VisDrone2019-DET (5 эпох).

Класс	Images	Instances	mAP50	mAP50-95
All (все классы)	519	36451	0.195	0.107
Car (автомобиль)	487	13208	0.642	0.404
Pedestrian (пешеход)	491	8415	0.215	0.078

Структура проекта:
app.py — веб-интерфейс на Streamlit.
train.py — скрипт для дообучения модели.
convert.py — скрипт конвертации аннотаций VisDrone в формат YOLO.
VisDrone.yaml — конфигурация путей к датасету и классов.
report.md — краткий отчет о результатах и метриках.
requirements.txt — список зависимостей проекта.
