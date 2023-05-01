import os
import uuid
from dotenv import load_dotenv
from pricing_dict import productType_dict, artist_royalty_dict
from calculate_price import calculate_price
from cloudinary_utils import get_image_url_from_cloudinary, upload_image_to_cloudinary
from extract_file_info import extract_file_info

# Create new Entry widget for product type
def generate_handle(product_info):
    handle = f"{product_info[0]}-{product_info[1]}".lower().replace(' ', '-')
    unique_id = str(uuid.uuid4()).split('-')[-1]
    handle = f"{handle}-{unique_id}"
    return handle

load_dotenv()
cloud_name = os.getenv('CLOUDINARY_CLOUD_NAME')
api_key = os.getenv('CLOUDINARY_API_KEY')
api_secret = os.getenv('CLOUDINARY_API_SECRET')

import os
import json

def create_img_dictionary(image_filename):
    # Extract image information from filename
    file_info = extract_file_info(image_filename)
    aspect_ratio = file_info["aspect_ratio"]
    uuid = file_info["uuid"]
    product_type = file_info["product_type"]
    title = file_info["title_var"]
    image_position = file_info["image_position_var"]
    option1_values = file_info["option1_values"] 

    print(file_info, aspect_ratio, uuid, product_type, title, image_position, option1_values)       



    # Derive orientation from aspect ratio
    if float(aspect_ratio) < 1:
        orientation = "Portrait"
    elif float(aspect_ratio) > 1:
        orientation = "Landscape"
    else:
        orientation = "Square"

    # Create a dictionary for the image with all the CSV fields
    image_dict = {
        "Handle": generate_handle(image_filename),
        "Title": title,
        "Body (HTML)": "",
        "Vendor": "",
        "Product Category": "",
        "Type": "",
        "Tags": "Miscellaneous",
        "Published": "",
        "Option1 Name": "Size",
        "Option1 Value": "",
        "Option2 Name": "",
        "Option2 Value": "",
        "Option3 Name": "",
        "Option3 Value": "",
        "Variant SKU": "",
        "Variant Grams": "",
        "Image Src": image_filename,
        "Image Alt Text": title,
        "Gift Card": "",
        "SEO Title": "",
        "SEO Description": "",
        "Google Shopping / Google Product Category": "",
        "Google Shopping / Gender": "",
        "Google Shopping / Age Group": "",
        "Google Shopping / MPN": "",
        "Google Shopping / AdWords Grouping": "",
        "Google Shopping / AdWords Labels": "",
        "Google Shopping / Condition": "",
        "Google Shopping / Custom Product": "",
        "Google Shopping / Custom Label 0": "",
        "Google Shopping / Custom Label 1": "",
        "Google Shopping / Custom Label 2": "",
        "Google Shopping / Custom Label 3": "",
        "Google Shopping / Custom Label 4": "",
        "Variant Image": "",
        "Variant Weight Unit": "",
        "Variant Tax Code": "",
        "Cost per item": "",
        "Included / United Arab Emirates": "",
        "Included / International": "",
        "Price / International": "",
        "Compare At Price / International": "",
        "Status": ""
    }

    # Update the Option1 Value field based on available option values
    if option1_values:
        image_dict["Option1 Value"] = option1_values[image_position % len(option1_values)]

    return image_dict