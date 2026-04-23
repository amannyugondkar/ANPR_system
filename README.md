# 🚗 Automated Number Plate Recognition (ANPR) using YOLOv8

## 📌 Overview

This project implements an **Automated Number Plate Recognition (ANPR)** system using **YOLOv8** for real-time vehicle number plate detection and recognition. The system detects vehicles in images/videos, extracts number plates, and processes them for text recognition.

---

## 🎯 Objectives

* Detect vehicles using deep learning (YOLOv8)
* Identify and localize number plates
* Extract and recognize text from number plates
* Enable real-time traffic monitoring and automation

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Framework:** YOLOv8 (Ultralytics)
* **Libraries:**

  * OpenCV
  * NumPy
  * Pandas
  * EasyOCR / Tesseract OCR
* **Tools:** Jupyter Notebook / VS Code

---

## 📂 Project Structure

```
ANPR-YOLOv8/
│
├── dataset/                # Training and testing data
├── models/                 # Trained YOLOv8 model weights
├── outputs/                # Detected images/videos
├── src/
│   ├── detect.py           # Detection script
│   ├── ocr.py              # OCR processing
│   └── utils.py            # Helper functions
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Methodology

1. **Input Data**

   * Images or video streams are provided as input.

2. **Frame Extraction**

   * Video is converted into frames using OpenCV.

3. **Vehicle Detection**

   * YOLOv8 detects vehicles in each frame.

4. **Number Plate Detection**

   * A trained model identifies number plate regions.

5. **Text Extraction (OCR)**

   * OCR tools (EasyOCR/Tesseract) extract text from plates.

6. **Output**

   * Recognized number plate is displayed and stored.

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ANPR-YOLOv8.git
cd ANPR-YOLOv8
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Install YOLOv8

```bash
pip install ultralytics
```

---

## ▶️ Usage

### Run Detection

```bash
python src/detect.py --source input_video.mp4
```

### Run OCR

```bash
python src/ocr.py
```

---

## 📊 Output

* Bounding boxes around vehicles and number plates
* Extracted plate text displayed on screen
* Saved results in `/outputs` folder

---

## 📈 Applications

* Traffic monitoring systems
* Automated toll collection
* Parking management systems
* Law enforcement (speed/violation tracking)

---

## ⚠️ Challenges

* Low-resolution images
* Motion blur in videos
* Different plate formats and fonts
* Poor lighting conditions

---

## 🔮 Future Improvements

* Improve OCR accuracy using deep learning models
* Add multi-language plate recognition
* Deploy as a web/mobile application
* Integrate with real-time CCTV systems

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repository and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---


