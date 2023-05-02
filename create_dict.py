import os
import uuid
from dotenv import load_dotenv
from pricing_dict import productType_dict, artist_royalty_dict
from calculate_price import calculate_price
from cloudinary_utils import get_image_url_from_cloudinary
from extract_file_info import extract_file_info
from cloudinary_utils import get_image_url_from_cloudinary

# Function to generate a Cloudinary public ID
def generate_cloudinary_public_id():
    return str(uuid.uuid4())

load_dotenv()
cloud_name = os.getenv('CLOUDINARY_CLOUD_NAME')
api_key = os.getenv('CLOUDINARY_API_KEY')
api_secret = os.getenv('CLOUDINARY_API_SECRET')

def create_img_dictionary(image_filename):
    # Extract image information from filename
    file_info = extract_file_info(image_filename)
    aspect_ratio = file_info["aspect_ratio"]
    uuid = file_info["uuid"]
    product_type = file_info["product_type"]
    title = file_info["title_var"]
    image_position = file_info["image_position_var"]
    artist= file_info["vendor"]
    option1_values = file_info["option1_values"]
    public_id = generate_cloudinary_public_id,
    print("*******************************")
    print(file_info, aspect_ratio, uuid, product_type, title, image_position, option1_values)       
    print("#########################################")


    # Derive orientation from aspect ratio
    if float(aspect_ratio) < 1:
        orientation = "Portrait"
    elif float(aspect_ratio) > 1:
        orientation = "Landscape"
    else:
        orientation = "Square"

    # Create a dictionary for the image with all the CSV fields
    image_dict = {
        "Handle":uuid ,
        "Title": title,
        "Body (HTML)": "",
        "Vendor": artist,
        "Product Category": "",
        "Type": product_type,
        "Tags": "Miscellaneous",
        "Published": "TRUE",
        "Option1 Name": "Size",
        "Option1 Value":option1_values,
        "Option2 Name": "",
        "Option2 Value": "",
        "Option3 Name": "",
        "Option3 Value": "",
        "Variant SKU": "",
        "Variant Grams": "",
        "Variant Inventory Policy":"Continue",
        "Image Src": get_image_url_from_cloudinary(public_id),
        "Image Alt Text": title,
        "Gift Card": "FALSE",
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
        "Variant Weight Unit": "kg",
        "Variant Tax Code": "",
        "Cost per item": "",
        "Included / United Arab Emirates": "TRUE",
        "Included / International": "FALSE",
        "Price / International": "",
        "Compare At Price / International": "",
        "Status": "active",
        "cloudinary_public_id":generate_cloudinary_public_id(),
        "cloudinary_url":get_image_url_from_cloudinary(public_id)
    }

    return image_dict

def create_img_dictionary_2(image_filename):
    # Extract image information from filename
    file_info = extract_file_info(image_filename)
    aspect_ratio = file_info["aspect_ratio"]
    uuid = file_info["uuid"]
    product_type = file_info["product_type"]
    title = file_info["title_var"]
    image_position = file_info["image_position_var"]
    artist= file_info["vendor"]
    option1_values = file_info["option1_values"]
    public_id = generate_cloudinary_public_id,
    print("*******************************")
    print(file_info, aspect_ratio, uuid, product_type, title, image_position, option1_values)       
    print("#########################################")


    # Derive orientation from aspect ratio
    if float(aspect_ratio) < 1:
        orientation = "Portrait"
    elif float(aspect_ratio) > 1:
        orientation = "Landscape"
    else:
        orientation = "Square"

    # Create a dictionary for the image with all the CSV fields
    image_dict = {
        "Handle":uuid ,
        "Title": "",
        "Body (HTML)": "",
        "Vendor": artist,
        "Product Category": "",
        "Type": product_type,
        "Tags": "Miscellaneous",
        "Published": "",
        "Option1 Name": "",
        "Option1 Value":option1_values,
        "Option2 Name": "",
        "Option2 Value": "",
        "Option3 Name": "",
        "Option3 Value": "",
        "Variant SKU": "",
        "Variant Grams": "",
        "Variant Inventory Policy":"Continue",
        "Image Src": get_image_url_from_cloudinary(public_id),
        "Image Alt Text": title,
        "Gift Card": "FALSE",
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
        "Variant Weight Unit": "kg",
        "Variant Tax Code": "",
        "Cost per item": "",
        "Included / United Arab Emirates": "TRUE",
        "Included / International": "FALSE",
        "Price / International": "",
        "Compare At Price / International": "",
        "Status": "active",
        "cloudinary_public_id":generate_cloudinary_public_id(),
        "cloudinary_url":get_image_url_from_cloudinary(public_id)
    }

    return image_dict