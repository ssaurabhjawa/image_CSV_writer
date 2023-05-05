import cloudinary
import cloudinary.uploader
import cloudinary.api
from extract_file_info import extract_file_info
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url

import requests
import openai_secret_manager
import openai
import re
import os


#==================================================================
#              Step 1. Upload to Cloudinary & URL
#==================================================================
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url

def upload_to_cloudinary(image_path):
    cloudinary.config(
    cloud_name = "djqvqmqe2",
    api_key = "379169473671185",
    api_secret = "HFgkfTbvvKlD0TGtXmQDLBFBDys",
    secure = True
)
    response = cloudinary.uploader.upload(image_path, folder="product-images/")
    public_id = response["public_id"]
    print(f"Uploaded image {public_id} to Cloudinary")
    return public_id
            
def get_image_url_from_cloudinary(public_id):
    resource = cloudinary.api.resource(public_id)
    return resource["url"]

#==================================================================
#              Step 2. generate_description
#==================================================================

def generate_description(prompt, max_length):
    # Get OpenAI API credentials
    secrets = openai_secret_manager.get_secret("openai")
    openai.api_key = secrets["api_key"]

    # Use the Davinci model to generate the description
    model_engine = "davinci"
    prompt = f"{prompt}\n\nDescription:"
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_length,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Extract the generated description from the API response
    description = response.choices[0].text
    # Clean up the description by removing leading/trailing white space and any extra line breaks
    description = description.strip()
    description = re.sub(r'\n+', '\n', description)

    return description


# prompt = "Write a prompt here..."
# response = requests.post(
#     "https://api.openai.com/v1/engine/<engine-id>/completions",
#     headers={
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {API_KEY}",
#     },
#     json={
#         "prompt": prompt,
#         "max_tokens": 1000,
#         "temperature": 0.7,
#     },
# )

# if response.ok:
#     generated_text = response.json()["choices"][0]["text"]
#     print(generated_text)
# else:
#     print("Failed to generate text:", response.status_code, response.text)


#==================================================================
#              Product_level_dictionary
#==================================================================

def product_level_dictionary(image_filename, output_folder_path):
    file_path = os.path.join(output_folder_path, image_filename)
    public_id = upload_to_cloudinary(file_path)
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
        "Image Src": get_image_url_from_cloudinary(public_id),  # Use the Cloudinary URL
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

# def test_product_level_dictionary(output_folder_path):
#     file_name = "1.5--12345--canvas--abstract--1--Jane_Doe.jpg"
#     output = product_level_dictionary(file_name,output_folder_path=output_folder_path)
#     print(output)

# test_product_level_dictionary()