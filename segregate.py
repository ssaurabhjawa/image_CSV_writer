import os
import shutil
from PIL import Image

aspect_ratios = {"2.33": [], "2.39": [], "1.33": [], "1.5": [], "1.6": [], "1.77": [], "1.85": [], "2": [], "2.2": []}

def create_temp_dir():
    # Create a temporary directory in the user's home directory
    home_dir = os.path.expanduser("~")
    temp_dir = os.path.join(home_dir, "temp_segregation")
    os.makedirs(temp_dir, exist_ok=True)
    return temp_dir

def segregate_images_by_ratio(image_folder, aspect_ratios, tolerance=0.05):
    temp_dir = create_temp_dir()
    
    for ratio in aspect_ratios:
        # Create folder for this ratio in the temporary directory
        folder_name = f"{ratio}"
        folder_path = os.path.join(temp_dir, folder_name)
        os.makedirs(folder_path, exist_ok=True)

    # Iterate through all images in the folder
    for file_name in os.listdir(image_folder):
        file_path = os.path.join(image_folder, file_name)

        # Copy the image to the temporary directory
        temp_file_path = os.path.join(temp_dir, file_name)
        shutil.copy(file_path, temp_file_path)

        # Get aspect ratio of the image
        with Image.open(temp_file_path) as img:
            width, height = img.size
            aspect_ratio = round(width / height, 2)

        # Find closest ratio
        closest_ratio = min(aspect_ratios, key=lambda r: abs(float(r) - aspect_ratio))

        # Check if the image falls within the tolerance of the closest ratio
        if abs(float(closest_ratio) - aspect_ratio) <= tolerance:
            # Move image to the corresponding folder in the temporary directory
            folder_name = f"{closest_ratio}"
            folder_path = os.path.join(temp_dir, folder_name)
            new_file_path = os.path.join(folder_path, file_name)
            shutil.move(temp_file_path, new_file_path)

    # Move the segregated images back to the original location
    for ratio in aspect_ratios:
        # Get folder path in the temporary directory
        folder_name = f"{ratio}"
        folder_path = os.path.join(temp_dir, folder_name)

        # Move images in the folder back to the original location
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            new_file_path = os.path.join(image_folder, file_name)
            shutil.move(file_path, new_file_path)

        # Remove the empty folder in the temporary directory
        os.rmdir(folder_path)

    # Remove the temporary directory
    os.rmdir(temp_dir)
