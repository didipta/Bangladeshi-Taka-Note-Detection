# 💵 Bangladeshi Taka Note Detection using YOLOv11, FastAPI & Docker

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-REST_API-green)
![YOLOv11](https://img.shields.io/badge/YOLO-v11-red)
![Docker](https://img.shields.io/badge/Docker-Container-blue)
![License](https://img.shields.io/badge/License-Academic-lightgrey)

## 📌 Project Overview

This project implements a **Bangladeshi Taka Note Detection REST API** using a trained **YOLOv11** object detection model. The API accepts an uploaded image, detects Bangladeshi currency notes, and returns the detected denominations, confidence scores, and bounding box coordinates in JSON format.

The application is built with **FastAPI**, containerized using **Docker**, and deployed on **Render** for public access.

This project was developed as part of the **Deployment of Bangladeshi Taka Note Detection Model Using REST API & Docker** assignment.

---

# 🚀 Live Demo

### Public API

https://bangladeshi-taka-note-detection-lkfo.onrender.com

### Swagger Documentation

https://bangladeshi-taka-note-detection-lkfo.onrender.com/docs

---

# ✨ Features

- Detect Bangladeshi Taka Notes
- YOLOv11 Object Detection
- FastAPI REST API
- Dockerized Application
- Swagger Documentation
- Health Check Endpoint
- JSON Response
- Input Validation
- Exception Handling
- Cloud Deployment on Render

---

# 🛠 Technology Stack

| Technology | Description |
|------------|-------------|
| Python 3.11 | Programming Language |
| YOLOv11 | Object Detection Model |
| FastAPI | REST API Framework |
| Uvicorn | ASGI Server |
| OpenCV | Image Processing |
| Pillow | Image Handling |
| NumPy | Numerical Computing |
| Docker | Containerization |
| Render | Cloud Deployment |

---

# 📁 Project Structure

```text
Bangladeshi-Taka-Note-Detection/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── predict.py
│   ├── schemas.py
│   ├── models/
│   │   └── best.pt
│   └── templates/
│
├── sample_images/
├── screenshots/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .dockerignore
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK

cd Bangladeshi-Taka-Note-Detection
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Running the API

```bash
uvicorn app.main:app --reload
```

Application runs at

```
http://127.0.0.1:8000
```

---

# 📖 API Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# 📡 API Endpoints

## Home

| Method | Endpoint |
|---------|----------|
| GET | / |

Returns the web interface.

---

## Health Check

| Method | Endpoint |
|---------|----------|
| GET | /health |

Example Response

```json
{
  "status": "healthy",
  "model_loaded": true
}
```

---

## Predict Currency Notes

| Method | Endpoint |
|---------|----------|
| POST | /predict |

### Request

Content-Type

```
multipart/form-data
```

Parameter

| Name | Type | Required |
|------|------|----------|
| file | Image (.jpg/.jpeg/.png) | Yes |

---

### cURL Example

```bash
curl -X POST \
-F "file=@sample_images/100.jpg" \
http://127.0.0.1:8000/predict
```

---

### Sample JSON Response

```json
{
  "success": true,
  "filename": "100.jpg",
  "image_size": {
    "width": 640,
    "height": 640
  },
  "num_detections": 1,
  "inference_time_ms": 37.82,
  "detections": [
    {
      "class_name": "100_taka",
      "confidence": 0.9876,
      "bbox": {
        "x1": 96.52,
        "y1": 58.20,
        "x2": 520.43,
        "y2": 310.88
      }
    }
  ]
}
```

---

# 🐳 Docker

## Build Docker Image

```bash
docker build -t taka-note-detector .
```

---

## Run Docker Container

```bash
docker run -p 8000:8000 taka-note-detector
```

---

## Using Docker Compose

Build

```bash
docker compose build
```

Run

```bash
docker compose up
```

Stop

```bash
docker compose down
```

---

# ☁ Cloud Deployment

This application is deployed on **Render**.

### Live API

https://bangladeshi-taka-note-detection-lkfo.onrender.com

### Swagger UI

https://bangladeshi-taka-note-detection-lkfo.onrender.com/docs

---

# 🧪 Testing

The REST API was tested using:

- Swagger UI
- Postman
- cURL

Testing includes:

- Single image inference
- Invalid image validation
- Missing file validation
- Empty image validation
- Five different Bangladeshi Taka note images

---

# 📊 Model Output

The API returns:

- Detected denomination
- Confidence score
- Bounding box coordinates
- Number of detections
- Image dimensions
- Inference time

---

# ⚠ Error Handling

The API gracefully handles:

- Missing file
- Empty file
- Invalid image format
- Model loading errors
- Internal server errors

Appropriate HTTP status codes are returned for all error cases.

---

# 📷 Project Screenshots

Include the following screenshots in the Google Docs report.

- Model Inference
- Swagger UI
- Health Endpoint
- Prediction Endpoint
- Postman Request
- Postman Response
- Docker Build
- Docker Run
- Docker Container
- Render Deployment

---

# 📚 Assignment Requirements Covered

- ✅ YOLOv11 Model Integration
- ✅ Single Image Inference
- ✅ REST API Development
- ✅ JSON Response
- ✅ FastAPI
- ✅ Docker Containerization
- ✅ Docker Compose
- ✅ API Testing
- ✅ Documentation
- ✅ Cloud Deployment
- ✅ Public API

---

# 👨‍💻 Author

**Name:** Dipta Saha

**Course Project:** Deployment of Bangladeshi Taka Note Detection Model Using REST API & Docker
