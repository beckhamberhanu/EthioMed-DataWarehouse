import os
import shutil
from pathlib import Path

# Create YOLO dataset structure
dataset_dir = Path("data/yolo_dataset")
dataset_dir.mkdir(parents=True, exist_ok=True)

# Copy images from scraped data
src_dir = Path("data/raw/images")
dest_dir = dataset_dir / "images"
shutil.copytree(src_dir, dest_dir, dirs_exist_ok=True)

print(f"Prepared {len(list(dest_dir.glob('*.jpg')))} images for YOLO")