import logging
from typing import Dict
from starlette.requests import Request

from fastapi import FastAPI, File, UploadFile, HTTPException, status
from fastapi.responses import JSONResponse

from app.predict import load_model, run_inference
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("taka-detector")

app = FastAPI(
    title="Bangladeshi Taka Note Detection API",
    description="REST API for detecting Bangladeshi Taka notes using YOLOv11.",
    version="1.0.0",
)

ALLOWED_CONTENT_TYPES = {
    "image/jpeg",
    "image/jpg",
    "image/png",
}


# ==========================================================
# Startup
# ==========================================================

@app.on_event("startup")
def startup():

    try:
        load_model()
        logger.info("YOLO model loaded successfully.")

    except Exception as e:
        logger.error(f"Failed to load model: {e}")


# ==========================================================
# Root
# ==========================================================

# app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="taka-note-detector.html"
    )
# ==========================================================
# Health Check
# ==========================================================

@app.get("/health")
def health():

    try:
        load_model()

        return {
            "status": "healthy",
            "model_loaded": True,
        }

    except Exception:

        return {
            "status": "unhealthy",
            "model_loaded": False,
        }


# ==========================================================
# Prediction
# ==========================================================

@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    if file.filename == "":
        raise HTTPException(
            status_code=400,
            detail="No file selected."
        )

    if file.content_type not in ALLOWED_CONTENT_TYPES:
        raise HTTPException(
            status_code=400,
            detail="Only JPG and PNG images are supported."
        )

    image_bytes = await file.read()

    if len(image_bytes) == 0:
        raise HTTPException(
            status_code=400,
            detail="Uploaded file is empty."
        )

    try:

        result = run_inference(image_bytes)

        if not result["success"]:
            raise HTTPException(
                status_code=422,
                detail=result["error"]
            )

        return JSONResponse(
            status_code=200,
            content={
                "success": True,
                "filename": file.filename,
                "image_size": result["image_size"],
                "num_detections": result["num_detections"],
                "inference_time_ms": result["inference_time_ms"],
                "detections": result["detections"],
            },
        )

    except HTTPException:
        raise

    except FileNotFoundError:
        raise HTTPException(
            status_code=500,
            detail="Model weights not found."
        )

    except Exception as e:

        logger.exception(e)

        raise HTTPException(
            status_code=500,
            detail="Internal server error."
        )