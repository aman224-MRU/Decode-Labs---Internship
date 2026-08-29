"""Read text from the sample.png file using OCR and print it."""

from __future__ import annotations

from pathlib import Path

import cv2
import pytesseract
from PIL import Image, ImageOps

TESSERACT_PATH = Path(r"C:\Program Files\Tesseract-OCR\tesseract.exe")
if TESSERACT_PATH.exists():
    pytesseract.pytesseract.tesseract_cmd = str(TESSERACT_PATH)


def read_text(image_path: str | Path) -> str:
    """Extract readable text from an image and normalize whitespace."""
    image_file = Path(image_path)
    if not image_file.exists():
        raise FileNotFoundError(f"Image not found: {image_file}")

    image = cv2.imread(str(image_file), cv2.IMREAD_COLOR)
    if image is None:
        raise ValueError(f"Could not read image: {image_file}")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (3, 3), 0)
    processed = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    text = pytesseract.image_to_string(processed, config="--psm 6")
    return " ".join(text.split())


def main() -> None:
    image_path = Path(__file__).with_name("sample.png")
    if not image_path.exists():
        raise FileNotFoundError(f"Sample image not found: {image_path}")

    print("Extracted text from sample.png:")
    print(read_text(image_path))


if __name__ == "__main__":
    main()
