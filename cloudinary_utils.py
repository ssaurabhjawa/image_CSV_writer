import os
import cloudinary
import cloudinary.api
import cloudinary.uploader
from dotenv import load_dotenv

load_dotenv()

cloud_name = os.getenv('CLOUDINARY_CLOUD_NAME')
api_key = os.getenv('CLOUDINARY_API_KEY')
api_secret = os.getenv('CLOUDINARY_API_SECRET')

# Set up the Cloudinary configuration
cloudinary.config(
    cloud_name="<your_cloud_name>",
    api_key="<your_api_key>",
    api_secret="<your_api_secret>"
)

# def upload_image_to_cloudinary(filename, new_filename):
#     # Upload the image to Cloudinary
#     response = cloudinary.uploader.upload(filename, public_id=os.path.splitext(new_filename)[0])

#     # Return the Cloudinary public ID
#     return response["public_id"]


def get_image_url_from_cloudinary(public_id):
    image = cloudinary.CloudinaryImage(public_id)
    return image.image()


def get_image_url_from_cloudinary(public_id):
    resource = cloudinary.api.resource(public_id)
    return resource["url"]