import cloudinary
import cloudinary.uploader
import cloudinary.api
from extract_file_info import extract_file_info
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url





def product_level_dictionary(image_filename):
    # Extract image information from filename
    file_info = extract_file_info(image_filename)
    aspect_ratio = file_info["aspect_ratio"]
    uuid = file_info["uuid"]
    product_type = file_info["product_type"]
    title = file_info["title_var"]
    image_position = file_info["image_position_var"]
    artist= file_info["vendor"]
    option1_values = file_info["option1_values"]
    option1_prices = file_info["option1_prices"]
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
        "Option1 Value":option1_values[0] if option1_values else "",
        "Option2 Name": "",
        "Option2 Value": "",
        "Variant Price":option1_prices[0] if option1_prices else "",
        "Option3 Name": "",
        "Option3 Value": "",
        "Image Src": "",
        "Image Alt Text": title,
        "Gift Card": "FALSE",
        "SEO Title": "",
        "SEO Description": "",
        "Variant Image": "",
        "Variant Weight Unit": "kg",
        "Variant Tax Code": "",
        "Cost per item": "",
        "Included / United Arab Emirates": "TRUE",
        "Included / International": "FALSE",
        "Price / International": "",
        "Compare At Price / International": "",
        "Status": "active",
        "image_position": image_position,
         }
    return image_dict

def test_product_level_dictionary():
    file_name = "1.5--12345--canvas--abstract--1--Jane_Doe.jpg"
    output = product_level_dictionary(file_name)
    print(output)

test_product_level_dictionary()