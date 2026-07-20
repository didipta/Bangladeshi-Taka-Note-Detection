import os

# ==========================================================
# Application Settings
# ==========================================================

APP_NAME = "Bangladeshi Taka Note Detection API"
APP_VERSION = "1.0.0"

# ==========================================================
# Model Settings
# ==========================================================

MODEL_PATH = os.getenv("MODEL_PATH", "models/best.pt")

CONFIDENCE_THRESHOLD = float(
    os.getenv("CONFIDENCE_THRESHOLD", 0.25)
)

# ==========================================================
# API Settings
# ==========================================================

API_HOST = os.getenv("API_HOST", "0.0.0.0")
API_PORT = int(os.getenv("API_PORT", 8000))

# ==========================================================
# Upload Settings
# ==========================================================

ALLOWED_CONTENT_TYPES = {
    "image/jpeg",
    "image/jpg",
    "image/png",
}

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB

# ==========================================================
# Logging
# ==========================================================

LOG_LEVEL = "INFO"