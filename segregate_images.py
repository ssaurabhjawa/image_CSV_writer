import os
import shutil
from tkinter import Tk
from tkinter.filedialog import askdirectory
from PIL import Image


def segregate_images_by_aspect_ratio():
    # Ask user to select the folder containing images to be segregated
    root = Tk()
    root.withdraw()
    folder_path = askdirectory(title="Select Folder Containing Images to be Segregated")

    # Create directory for each aspect ratio
    os.makedirs(os.path.join(folder_path, "0.666666667"), exist_ok=True)
    os.makedirs(os.path.join(folder_path, "0.75"), exist_ok=True)
    os.makedirs(os.path.join(folder_path, "0.80"), exist_ok=True)
    os.makedirs(os.path.join(folder_path, "0.714285714"), exist_ok=True)
    os.makedirs(os.path.join(folder_path, "1"), exist_ok=True)
    os.makedirs(os.path.join(folder_path, "1.5"), exist_ok=True)
    os.makedirs(os.path.join(folder_path, "1.333333333"), exist_ok=True)
    os.makedirs(os.path.join(folder_path, "1.25"), exist_ok=True)
    os.makedirs(os.path.join(folder_path, "1.4"), exist_ok=True)

    # Iterate through each image file in the folder
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".jpg") or file_name.endswith(".jpeg") or file_name.endswith(".png"):
            file_path = os.path.join(folder_path, file_name)

            # Skip the file if it's being used by another process
            try:
                with Image.open(file_path) as img:
                    aspect_ratio = img.size[0] / img.size[1]
            except (PermissionError, OSError):
                print(f"{file_name} is being used by another process, skipping...")
                continue

            # Use shutil.move to move the file to the respective aspect ratio folder
            if aspect_ratio >= 0.666666667:
                if aspect_ratio < 0.75:
                    new_file_path = os.path.join(folder_path, "0.666666667", file_name)
                elif aspect_ratio < 0.8:
                    new_file_path = os.path.join(folder_path, "0.75", file_name)
                elif aspect_ratio < 0.714285714:
                    new_file_path = os.path.join(folder_path, "0.80", file_name)
                elif aspect_ratio < 1:
                    new_file_path = os.path.join(folder_path, "0.714285714", file_name)
                elif aspect_ratio < 1.5:
                    new_file_path = os.path.join(folder_path, "1", file_name)
                elif aspect_ratio < 1.333333333:
                    new_file_path = os.path.join(folder_path, "1.5", file_name)
                elif aspect_ratio < 1.25:
                    new_file_path = os.path.join(folder_path, "1.333333333", file_name)
                elif aspect_ratio < 1.4:
                    new_file_path = os.path.join(folder_path, "1.25", file_name)
                else:
                    new_file_path = os.path.join(folder_path, "1.4", file_name)

                shutil.move(file_path, new_file_path)
                print(f"{file_name} moved to {new_file_path}")

    print("Image segregation complete!")
