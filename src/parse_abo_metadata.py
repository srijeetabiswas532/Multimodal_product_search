import json
import csv
import os
from tqdm import tqdm # just shows progress bar

METADATA_DIR = "../data/abo/abo-listings"
IMAGE_DIR = "../data/abo/abo-images-small"
OUTPUT_DIR = '../data/products.csv'

os.makedirs(os.path.dirname(OUTPUT_DIR), exist_ok=True) # ensures that output dir exists

def extract_text_field(field):
    """Safely extract the first value from a multilingual field list."""
    if isinstance(field, list) and len(field) > 0:
        return field[0].get("value", "")
    return ""

with open(OUTPUT_DIR, "w", newline="", encoding="utf-8") as f_out: # opens products.csv for writing
    writer = csv.DictWriter(f_out, fieldnames=["product_id", "title", "description", "image_path"]) # creates CSV headers
    writer.writeheader()

    for filename in tqdm(os.listdir(METADATA_DIR)): # iterates over JSON files
        if not filename.endswith(".json"):
            continue

        filepath = os.path.join(METADATA_DIR, filename)
        with open(filepath, "r", encoding="utf-8") as f_in:
            try:
                data = json.load(f_in)
                product_id = data.get("item_id", "")
                title = extract_text_field(data.get("item_name", []))
                description = extract_text_field(data.get("bullet_point", []))
                image_id = data.get("main_image_id", "")
                image_path = os.path.join(IMAGE_DIR, f"{image_id}.jpg")

                if not os.path.exists(image_path):
                    continue  # skip items with missing images

                writer.writerow({
                    "product_id": product_id,
                    "title": title,
                    "description": description,
                    "image_path": image_path
                })

            except Exception as e:
                print(f"Failed to process {filename}: {e}")