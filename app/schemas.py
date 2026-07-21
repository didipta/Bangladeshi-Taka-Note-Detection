from typing import List
from pydantic import BaseModel


class ImageSize(BaseModel):
    width: int
    height: int


class BoundingBox(BaseModel):
    x1: float
    y1: float
    x2: float
    y2: float


class Detection(BaseModel):
    class_name: str
    confidence: float
    bbox: BoundingBox


class PredictionResponse(BaseModel):
    success: bool
    filename: str
    image_size: ImageSize
    num_detections: int
    inference_time_ms: float
    detections: List[Detection]


class HealthResponse(BaseModel):
    status: str
    model_loaded: bool