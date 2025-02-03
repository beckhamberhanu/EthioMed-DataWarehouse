import cv2
from pathlib import Path
from model_loader import load_yolo_model  # Import shared loader

# Load model once
model = load_yolo_model()

def visualize(image_path: str):
    img = cv2.imread(image_path)
    results = model(img)  # Now works!
    results.render()
    
    output_path = Path("data/yolo_dataset/processed") / Path(image_path).name
    cv2.imwrite(str(output_path), img)
    print(f"Saved visualized image to {output_path}")

# Example usage
visualize("data/yolo_dataset/images/2.jpg")