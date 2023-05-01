import os
import shutil

aspect_ratios = {"2:3": [], "3:4": [], "4:5": [], "5:7": [], "3:2": [], "4:3": [],"5:4": [], "7:5": []}


def segregate_images_by_ratio(image_folder, aspect_ratios, tolerance=0.05):
    for ratio in aspect_ratios:
        # Create folder for this ratio
        folder_name = f"{ratio[0]}_{ratio[1]}"
        folder_path = os.path.join(image_folder, folder_name)
        os.makedirs(folder_path, exist_ok=True)

    # Iterate through all images in the folder
    for file_name in os.listdir(image_folder):
        file_path = os.path.join(image_folder, file_name)

        # Get aspect ratio of the image
        with Image.open(file_path) as img:
            width, height = img.size
            aspect_ratio = round(width / height, 2)

        # Find closest ratio
        closest_ratio = min(aspect_ratios, key=lambda r: abs(r[0]/r[1] - aspect_ratio))

        # Check if the image falls within the tolerance of the closest ratio
        if abs(closest_ratio[0]/closest_ratio[1] - aspect_ratio) <= tolerance:
            # Move image to the corresponding folder
            folder_name = f"{closest_ratio[0]}_{closest_ratio[1]}"
            folder_path = os.path.join(image_folder, folder_name)
            new_file_path = os.path.join(folder_path, file_name)
            shutil.move(file_path, new_file_path)

import os
from PIL import Image



