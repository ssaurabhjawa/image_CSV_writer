import os
import re



def update_image_positions(folder_path):
    # Create a dictionary to store the maximum image position for each UUID
    uuid_positions = {}

    # Iterate through all the files in the folder
    for filename in os.listdir(folder_path):
        # Check if the file is a valid image file
        if filename.endswith(".jpg") or filename.endswith(".png"):
            # Extract the UUID and image position from the filename
            uuid, image_position = re.findall(r"([0-9a-f]{6,})--\d+--(\d+)\.\w+", filename)[0]

            # Update the maximum image position for this UUID
            if uuid not in uuid_positions:
                uuid_positions[uuid] = int(image_position)
            else:
                uuid_positions[uuid] = max(uuid_positions[uuid], int(image_position))

    # Iterate through all the files in the folder again and update the image position in the filename
    for filename in os.listdir(folder_path):
        # Check if the file is a valid image file
        if filename.endswith(".jpg") or filename.endswith(".png"):
            # Extract the UUID and image position from the filename
            uuid, image_position = re.findall(r"([0-9a-f]{6,})--(\d+)--\d+\.\w+", filename)[0]

            # Get the maximum image position for this UUID
            max_image_position = uuid_positions[uuid]

            # Update the image position in the filename
            new_filename = re.sub(r"([0-9a-f]{6,})--(\d+)--(\d+)\.\w+", rf"\1--\2--{max_image_position+1}\3", filename)

            # Rename the file
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
