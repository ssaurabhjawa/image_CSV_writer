from create_dict import create_img_dictionary
from product_level_dict import product_level_dictionary
from variant_level_dict import variant_level_dictionary
import os

def process_image(file_path):
    # Extract file name from file path
    file_name = os.path.basename(file_path)
    # Split file name into parts based on delimiter
    file_parts = file_name.split("--")
    
    # Extract title from file parts
    title_and_ext = file_parts[-1].split(".")
    title = title_and_ext[0]
    ext = "." + title_and_ext[1]
    file_parts[-1] = title
    
    print(f"file_name: {file_name}")
    print(f"file_parts: {file_parts}")

    # Extract image position from file parts
    image_position = int(file_parts[4])
    
    # Call the appropriate dictionary function based on image position
    if image_position == 1:
        image_dict = product_level_dictionary("--".join(file_parts))
    elif image_position > 1:
        image_dict = variant_level_dictionary("--".join(file_parts))
    else:
    # If image position is invalid, return an empty dictionary
        return {}

    
    # Upload image to Cloudinary and add image URL to dictionary
    public_id = upload_to_cloudinary(file_path)
    image_dict['Image Src'] = get_image_url_from_cloudinary(public_id)
    
    return image_dict

def test_process_image():
    file_path = "test_images/0.93--c94d05--Canvas--Jumbled Letters--1--OBL_Print.png"
    output = process_image(file_path)
    print(f"output: {output}")

test_process_image()



