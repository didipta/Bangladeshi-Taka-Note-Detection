import io
import os
import time
from typing import Any, Dict, List, Union

import numpy as np
from PIL import Image
from ultralytics import YOLO

# ==========================================================
# Configuration
# ==========================================================

# MODEL_PATH = os.getenv("MODEL_PATH", "/models/best.pt")
CONFIDENCE_THRESHOLD = float(os.getenv("CONFIDENCE_THRESHOLD", 0.25))

_model = None

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "models", "best.pt")
print(MODEL_PATH)
print(os.path.exists(MODEL_PATH))


# ==========================================================
# Load Model (Singleton)
# ==========================================================

def load_model(model_path: str = MODEL_PATH) -> YOLO:
    global _model

    if _model is None:
        if not os.path.isfile(model_path):
            raise FileNotFoundError(
                f"Model weights not found: {model_path}"
            )

        _model = YOLO(model_path)

    return _model


# ==========================================================
# Convert input to PIL Image
# ==========================================================

def _to_pil_image(
    image: Union[str, bytes, bytearray, Image.Image, np.ndarray]
) -> Image.Image:

    if isinstance(image, Image.Image):
        return image.convert("RGB")

    if isinstance(image, (bytes, bytearray)):
        return Image.open(io.BytesIO(image)).convert("RGB")

    if isinstance(image, str):
        if not os.path.exists(image):
            raise FileNotFoundError(image)
        return Image.open(image).convert("RGB")

    if isinstance(image, np.ndarray):
        return Image.fromarray(image).convert("RGB")

    raise TypeError(
        f"Unsupported image type: {type(image)}"
    )


# ==========================================================
# Inference
# ==========================================================

def run_inference(
    image: Union[str, bytes, bytearray, Image.Image, np.ndarray],
    conf_threshold: float = CONFIDENCE_THRESHOLD,
) -> Dict[str, Any]:

    model = load_model()

    try:
        pil_image = _to_pil_image(image)
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
        }

    start = time.perf_counter()

    results = model.predict(
        source=pil_image,
        conf=conf_threshold,
        verbose=False,
    )

    inference_time = (time.perf_counter() - start) * 1000

    result = results[0]

    detections: List[Dict[str, Any]] = []

    for box in result.boxes:

        cls_id = int(box.cls.item())

        detections.append(
            {
                "class_name": model.names[cls_id],
                "confidence": round(float(box.conf.item()), 4),
                "bbox": {
                    "x1": round(float(box.xyxy[0][0]), 2),
                    "y1": round(float(box.xyxy[0][1]), 2),
                    "x2": round(float(box.xyxy[0][2]), 2),
                    "y2": round(float(box.xyxy[0][3]), 2),
                },
            }
        )

    detections.sort(
        key=lambda x: x["confidence"],
        reverse=True,
    )

    return {
        "success": True,
        "image_size": {
            "width": pil_image.width,
            "height": pil_image.height,
        },
        "num_detections": len(detections),
        "inference_time_ms": round(inference_time, 2),
        "detections": detections,
    }


# ==========================================================
# CLI Demo
# ==========================================================

if __name__ == "__main__":

    import json
    import sys

    if len(sys.argv) != 2:
        print("Usage:")
        print("app/predict.py sample_image/test (1).jpg")
        sys.exit(1)

    image_path = sys.argv[1]

    result = run_inference(image_path)

    print(json.dumps(result, indent=4))