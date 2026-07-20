import os
import uuid
from PIL import Image


def generate_filename(filename: str) -> str:
    """
    Generate a unique filename.
    """

    extension = os.path.splitext(filename)[1]

    return f"{uuid.uuid4().hex}{extension}"


def get_image_size(image: Image.Image):

    return {
        "width": image.width,
        "height": image.height,
    }


def allowed_file(content_type: str, allowed_types: set) -> bool:

    return content_type in allowed_types