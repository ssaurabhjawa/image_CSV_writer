from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url

def upload_to_cloudinary(output_folder_path):
    cloudinary.config(
    cloud_name = "djqvqmqe2",
    api_key = "379169473671185",
    api_secret = "HFgkfTbvvKlD0TGtXmQDLBFBDys",
    secure = True
)
    for filename in os.listdir(output_folder_path):
        if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
            file_path = os.path.join(output_folder_path, filename)
            response = cloudinary.uploader.upload(file_path, folder="product-images/")
            public_id = response["public_id"]
            print(public_id)
            print(f"Uploaded image {response['public_id']} to Cloudinary")



from create_dict import create_img_dictionary

import os
def process_images():
    folder_path = output_folder_path # Replace with the path to your folder

    # Iterate through each file in the folder and create an image dictionary for it
    for file in os.listdir(folder_path):
        print(file)
        if file.endswith((".jpg", ".jpeg", ".png")):
            image_dict = create_img_dictionary(file)
            

# Create a tkinter window and button to process the images
window = tk.Tk()
window.title("Process Images")

process_images = tk.Button(root, text="1", command=process_images)
process_images.grid(row=6, column=6,padx=5, pady=5)