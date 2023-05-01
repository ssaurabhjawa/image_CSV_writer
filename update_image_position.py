import os
import re

def update_image_position():
    # Ask user for the folder path
    folder_path = filedialog.askdirectory(title="Select Folder")

    if not folder_path:
        # User cancelled the operation
        return

    # Ask user for the new position number
    new_position = tk.simpledialog.askinteger(title="New Image Position", prompt="Enter the new position number:")

    if not new_position:
        # User cancelled the operation or entered an invalid value
        return

    # Rename files in the folder
    for i, file_name in enumerate(os.listdir(folder_path)):
        if file_name.endswith((".jpg", ".jpeg", ".png")):
            # Get the file extension
            ext = os.path.splitext(file_name)[1]

            # Create the new file name with the updated position number
            new_file_name = f"{aspect_ratio}--{uuid.uuid4().hex[:6]}--{product_type_var.get()}--{title_var.get()}--{new_position+i}{ext}"

            # Rename the file
            os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_file_name))

    # Show a success message
    tk.messagebox.showinfo("Success", "Image positions have been updated.")


