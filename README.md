# Car Detection (VisDrone)
Сервис для детекции автотранспорта и пешеходов на аэрофотоснимках.

**Доступен по адресу:** [Нажми сюда](https://car-detection-aqhzxgsqbr73brzrg86snp.streamlit.app/)

---

### 📦 Веса моделей
*   **Обученная модель (YOLO11n-VisDrone):** [`best.pt`](https://github.com/yungpen/car-detection/blob/main/runs/detect/train/weights/best.pt)
*   **Базовая модель:** [yolo11n.pt](https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo11n.pt)

### 🛠 Стек технологий
* **Язык:** Python
* **Библиотеки:** Ultralytics (YOLO11), Streamlit, PyTorch
* **Датасет:** VisDrone2019-DET

### 📋 Результаты (Metrics)
Модель дообучена на датасете VisDrone (5 эпох).

| Класс | Images | Instances | mAP50 | mAP50-95 |
| :--- | :--- | :--- | :--- | :--- |
| **All (все классы)** | 519 | 36451 | **0.195** | 0.107 |
| **Car (автомобиль)** | 487 | 13208 | **0.642** | 0.404 |
| **Pedestrian (пешеход)** | 491 | 8415 | **0.215** | 0.078 |

---

### ⚙️ Инструкция по установке

1. **Клонировать репозиторий:**
```bash
git clone https://github.com/yungpen/car-detection
cd car-detection
### Настроить окружение (Windows PowerShell):
* python -m venv venv
* .\venv\Scripts\activate
* python -m pip install --upgrade pip
* pip install -r requirements.txt
