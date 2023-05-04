import cloudinary
import cloudinary.api
import cloudinary.uploader
import uuid
from dotenv import load_dotenv

load_dotenv()

def generate_public_id():
    # Generate a unique ID using uuid
    unique_id = uuid.uuid4().hex

    # Check if the public ID already exists in Cloudinary
    while cloudinary.api.resource_exists(unique_id):
        # If it does, generate a new unique ID
        unique_id = uuid.uuid4().hex

    return unique_id