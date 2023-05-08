import os
import csv
import tkinter as tk
from tkinter import filedialog, ttk, Listbox, Canvas, NW, END, messagebox
from PIL import Image, ImageTk
import csv
import shutil
from PIL import Image
# import cloudinary
# import cloudinary.uploader
# import cloudinary.api
import uuid
import tkinter.simpledialog


from pricing_dict import artist_royalty_dict
from segregate_images import segregate_images_by_aspect_ratio


# Initialize tkinter app
root = tk.Tk()
root.title(" OBL Image Naming App")

# Define global variables
image_folder = ""
completed_renaming = []
renamed_files = []

# Create a frame with a border
frame = tk.Frame(root, borderwidth=2, relief="groove")
frame.grid(row=0, column=0, rowspan=4, columnspan=3)

# Configure rows and columns with grid_columnconfigure and grid_rowconfigure
for i in range(10):
    root.grid_columnconfigure(i, weight=1, minsize=50)
    root.grid_rowconfigure(i, weight=1, minsize=50)

# Create widgets with grid
for i in range(10):
    for j in range(10):
        label = tk.Label(root, text=f"({i}, {j})", borderwidth=1, relief="solid")
        label.grid(row=i, column=j, padx=1, pady=1, sticky="nsew")

def select_folder():
    global image_folder, image_files
    image_folder = filedialog.askdirectory()
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png')]
    # Display list of image files in listbox
    for image in image_files:
        image_listbox.insert(tk.END, image)


count_label = tk.Label(root, text="")
count_label.grid(row=0, column=0, padx=5, pady=10, sticky="sw") 

# Create button to select folder
select_folder_button = tk.Button(root, text="Select Image Folder", command=select_folder)
select_folder_button.grid(row=0, column=1, padx=5, pady=5, sticky='sw')

#==================================================================
#                           Listbox
#==================================================================

# Create listbox to display image files
image_listbox = tk.Listbox(root,width=100,height=20)
image_listbox.grid(row=0, column=1,columnspan=4, padx=5, pady=1, sticky="w")

# Create Canvas to display image
image_canvas = tk.Canvas(root, width=400, height=400)
image_canvas.grid(row=0, column=2, padx=5, pady=1, sticky="w")

# Function to display selected image
def show_image(event):
    # Get selected file name
    selected_file = current_selection_listbox.get(current_selection_listbox.curselection())

    # Load and display image on canvas
    img = Image.open(os.path.join(image_folder, selected_file))
    img.thumbnail((400, 400))
    img_tk = ImageTk.PhotoImage(img)
    image_canvas.create_image(0, 0, anchor=NW, image=img_tk)
    image_canvas.image = img_tk

# Bind Listbox selection event to show_image function
image_listbox.bind('<<ListboxSelect>>', show_image)

# Define input variables
product_type_options = ["Canvas", "Acrylic", "Mugs", "T-Shirts","Wall Paper", "Poster", "NoteBook", "ArtBook"]
product_type_var = tk.StringVar(root, product_type_options[0])

#==================================================================
#                          Refresh Listbox
#==================================================================
def refresh_images():
    # Clear current image selection
    current_selection_listbox.selection_clear(0, END)

    # Clear current image on canvas
    image_canvas.delete("all")

    # Get list of image files in image folder
    image_files = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]

    # Clear current listbox options
    image_listbox.delete(0, END)

    # Add image files to listbox options
    for f in image_files:
        image_listbox.insert(END, f)

    # Bind Listbox selection event to show_image function
    image_listbox.bind('<<ListboxSelect>>', show_image)


refresh_button = tk.Button(root, text="Refresh", width = 15, command=refresh_images)
refresh_button.grid(row=0, column=1, padx=5, pady=5, sticky='se')



#==================================================================
#                       Segrage Images by Ratio
#==================================================================

refresh_button = tk.Button(root, text="Segregate Images", width = 15, command=segregate_images_by_aspect_ratio)
refresh_button.grid(row=0, column=1, padx=5, pady=5, sticky='s')



#==================================================================
#                           Artist Dropdown
#==================================================================

artist_label = tk.Label(root, text="Artist:")
artist_label.grid(row=3, column=1, padx=5, pady=5,sticky='n')
# Create the dropdown menu
selected_artist = tk.StringVar(root, value=list(artist_royalty_dict.keys())[0])
artist_dropdown = ttk.Combobox(root, textvariable=selected_artist, values=list(artist_royalty_dict.keys()))

# Configure the dropdown menu
artist_dropdown.config(state="readonly", width=15)
# Display the dropdown menu using grid
artist_dropdown.grid(row=3, column=1,padx=5, pady=5, sticky='s')

#==================================================================
#                           Product Type Dropdown
#==================================================================

# Create the label and dropdown for the product type dropdown
product_type_label = tk.Label(root, text="Product Type:")
product_type_dropdown = ttk.Combobox(root, textvariable=product_type_var, values=product_type_options)
product_type_dropdown.config(width=10)

product_type_label.grid(row=3, column=1, padx=5, pady=5, sticky="nw")
product_type_dropdown.grid(row=3, column=1, padx=5, pady=5, sticky="sw")

root.rowconfigure(3, minsize=70)

title_var = tk.StringVar(root)
# Create variable for image position
image_position_var = tk.IntVar(value=0)

title_label = tk.Label(root, text="Title:")
title_entry = tk.Entry(root, textvariable=title_var, width=100)
title_label.grid(row=2, column=0, padx=5, pady=1, sticky="e")
title_entry.grid(row=2, column=1, columnspan=2, padx=5, pady=1, sticky="w")


# Create the renamed_listbox
renamed_listbox = tk.Listbox(root, width=100)
renamed_listbox.grid(row=6, column=1, padx=10, pady=10)

#==================================================================
#                           OUTPUT Folder
#==================================================================

def create_output_folder():
    global output_folder_path
    output_folder_path = filedialog.askdirectory(title="Select output folder")
    if output_folder_path:
        os.makedirs(output_folder_path, exist_ok=True)
        tk.messagebox.showinfo("Success", f"Output folder created at {output_folder_path}")
        # Display list of image files in output_listbox
        output_files = [f for f in os.listdir(output_folder_path) if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png')]
        output_listbox.delete(0, tk.END)
        for file in output_files:
            output_listbox.insert(tk.END, file)
    else:
        tk.messagebox.showerror("Error", "No output folder selected")

# Create Output Folder button
create_output_folder_button = tk.Button(root, text="Select Output Folder", command=create_output_folder)
create_output_folder_button.grid(row=6, column=0, padx=10, pady=10)


#==================================================================
#                           Name Creation
#==================================================================
def rename_file():
    # Activate current_selection_listbox
    current_selection_listbox.focus_set()


    # Get selected image filename
    selected_file = current_selection_listbox.get(current_selection_listbox.curselection())

    if not selected_file:
        tk.messagebox.showerror("Error", "Please select an image to rename.")
        return

    # Get image aspect ratio
    img_path = os.path.join(image_folder, selected_file)
    with Image.open(img_path) as img:
        width, height = img.size
        aspect_ratio = round(width / height, 2)
        

    # Get file extension
    ext = os.path.splitext(selected_file)[1]

    # Create new filename with aspect ratio and UUID
    new_filename = f"{aspect_ratio}--{uuid.uuid4().hex[:6]}--{product_type_var.get()}--{title_var.get()}--{image_position_var.get()}--{selected_artist.get()}{ext}"

    try:
        # Check if file exists in the old file path
        if os.path.isfile(img_path):
            # Copy file to output folder
            shutil.copy(img_path, os.path.join(output_folder_path, new_filename))

            # Update current_selection_listbox
            current_selection_listbox.delete(0, tk.END)
            current_selection_listbox.insert(0, new_filename)

            # Clear current_selection_listbox
            current_selection_listbox.selection_clear(0, tk.END)

            # Update image_listbox
            image_listbox.delete(0, tk.END)
            for file in os.listdir(image_folder):
                if file.endswith((".jpg", ".jpeg", ".png")):
                    image_listbox.insert(tk.END, file)

            # Add new filename to renamed_files array
            renamed_files.append(new_filename)

            # Update renamed_listbox
            renamed_listbox.delete(0, END)
            for file in renamed_files:
                renamed_listbox.insert(END, file)
        else:
            tk.messagebox.showerror("Error", "The selected file no longer exists.")
    except Exception as e:
        tk.messagebox.showerror("Error", f"An error occurred while renaming the file: {e}")
        # Print error message to console for debugging
        print(f"Error occurred while renaming the file: {str(e)}")


#==================================================================
#                           Display Image
#==================================================================

# Create new Listbox widget to hold current selection
current_selection_listbox = tk.Listbox(root, height=1, width=100)
current_selection_listbox.grid(row=1, column=1, padx=5, pady=5, sticky="w")

def update_current_selection(event):
    # Get selected file name
    selected_file = image_listbox.get(image_listbox.curselection())

    # Update current selection Listbox
    current_selection_listbox.delete(0, tk.END)
    current_selection_listbox.insert(0, selected_file)

# Bind the image_listbox to update the current_selection_listbox
image_listbox.bind('<Double-Button-1>', update_current_selection)

# Bind the current_selection_listbox to rename_file function
current_selection_listbox.bind('<<ListboxSelect>>', rename_file)

# "Rename File" and binds it to the function 'rename_file'.
rename_button = tk.Button(root, text="<--Rename Me", command=rename_file)
rename_button.grid(row=1, column=2, padx=5, pady=1, sticky="w")

# Listbox widget to display the output image files and set its width
output_listbox = tk.Listbox(root, width=70,height=20)
output_listbox.grid(row=0, column=3, padx=5, pady=1)

#==================================================================
#                           Update Output Listbox
#==================================================================

# Define function to update the output listbox
def update_output_listbox():
    output_listbox.delete(0, tk.END)
    for file in os.listdir(output_folder_path):
        if file.endswith((".jpg", ".jpeg", ".png")):
            output_listbox.insert(tk.END, file)

# Create button to update the output listbox
update_output_button = tk.Button(root, text="Update Output Listbox", command=update_output_listbox)
update_output_button.grid(row=0, column=3, padx=5, pady=5, sticky="s")


#==================================================================
#                          Update Image Position
#==================================================================
def update_image_position():
    # Ask user to select a folder
    folder_path = filedialog.askdirectory(title="Select a folder")

    # Ask user for image position number to rename
    image_position = tk.simpledialog.askinteger("Image Position", "Enter the image position number to rename:", minvalue=1)

    if not folder_path:
        tk.messagebox.showerror("Error", "Please select a folder.")
        return

    if not image_position:
        tk.messagebox.showerror("Error", "Please enter the image position number to rename.")
        return

    # Iterate through each file in the folder and rename it with updated image position number
    for file in os.listdir(folder_path):
        if file.endswith((".jpg", ".jpeg", ".png")):
            # Remove extension from filename
            filename_without_ext = os.path.splitext(file)[0]
            # Get aspect ratio, uuid, product type, title, and artist from the filename
            filename_parts = filename_without_ext.split("--")
            aspect_ratio = filename_parts[0]
            uuid = filename_parts[1]
            product_type = filename_parts[2]
            title = (filename_parts[3])
            artist_name = filename_parts[5] # assuming artist name is separated by underscore

            # Create new filename with updated image position number and artist name
            ext = os.path.splitext(file)[1]
            new_filename = f"{aspect_ratio}--{uuid}--{product_type}--{title}--{image_position}--{artist_name}{ext}"



            # Rename file
            os.rename(os.path.join(folder_path, file), os.path.join(output_folder_path, new_filename))

    # Update image_listbox
    image_listbox.delete(0, tk.END)
    for file in os.listdir(folder_path):
        if file.endswith((".jpg", ".jpeg", ".png")):
            image_listbox.insert(tk.END, file)
    
    tk.messagebox.showinfo("Success", f"All files in {folder_path} have been renamed with image position {image_position}.")


# Create the "Update Image Position" button
update_position_button = tk.Button(root, text="Update Image Position", command=update_image_position)
update_position_button.grid(row=3, column=3, padx=5, pady=5)





            


# #==================================================================
# #              Step 1. Upload to Cloudinary & URL
# #==================================================================
# from cloudinary.uploader import upload
# from cloudinary.utils import cloudinary_url

# def upload_to_cloudinary(image_path):
#     cloudinary.config(
#     cloud_name = "djqvqmqe2",
#     api_key = "379169473671185",
#     api_secret = "HFgkfTbvvKlD0TGtXmQDLBFBDys",
#     secure = True
# )
#     response = cloudinary.uploader.upload(image_path, folder="product-images/")
#     public_id = response["public_id"]
#     print(f"Uploaded image {public_id} to Cloudinary")
#     return public_id
            
# def get_image_url_from_cloudinary(public_id):
#     resource = cloudinary.api.resource(public_id)
#     return resource["url"]


#==================================================================
#      Step 2. Process Directory
#==================================================================

from create_dict import create_img_dictionary
from product_level_dict import product_level_dictionary
from variant_level_dict import variant_level_dictionary
from extract_file_info import extract_file_info
from variant_level_dict_3 import variant_level_dictionary_3

from datetime import datetime
import os
import csv
import pathlib
from datetime import datetime
import time


def write_csv(images_list):
    fieldnames = ["Handle", "Title", "Body (HTML)", "Vendor", "Product Category", "Type", "Tags", "Published", "Option1 Name", "Option1 Value", "Option2 Name", "Option2 Value", "Variant Price", "Option3 Name", "Option3 Value", "Image Src", "Image Alt Text", "Gift Card", "SEO Title", "SEO Description", "Variant Image", "Variant Weight Unit", "Variant Tax Code", "Cost per item", "Included / United Arab Emirates", "Included / International", "Price / International", "Compare At Price / International", "Status", "image_position"]
    
    # Create directory for CSV file
    csv_dir = os.path.join(os.getcwd(), 'product_csv')
    pathlib.Path(csv_dir).mkdir(parents=True, exist_ok=True)
    
    # Create filename with current timestamp
    current_time = datetime.now().strftime("%H:%M:%S")
    csv_filename = f"products_{current_time}.csv"
    csv_path = os.path.join(output_folder_path, f"products_{time.strftime('%H_%M_%S')}.csv")

    
    with open(csv_path, "w", newline="", encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for image_dict in images_list:
            writer.writerow(image_dict)
            
    messagebox.showinfo("CSV Generated", "CSV file generated successfully!")


def process_image():
    image_list = []
    image_dict = []
    image_filename_dict = {}
    for filename in os.listdir(output_folder_path):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            file_path = os.path.join(output_folder_path, filename)
            # Extract image position number from filename
            file_parts = filename.split("--")
            position = int(file_parts[4])
            if position == 1 :
                print(f"file name::{filename}")
                image_dict = product_level_dictionary(filename, output_folder_path)  
                image_list.append(image_dict)         
            elif position == 2 :
                file_info = extract_file_info(filename)
                option1_values = file_info["option1_values"][1:]
                option1_prices = file_info["option1_prices"][1:]
                print(option1_values)
                print(option1_prices)
                for i, option in enumerate(option1_values, start=1):
                    image_dict = variant_level_dictionary(filename, output_folder_path, option1_values[i-1], option1_prices[i-1], image_filename_dict)
                    image_list.append(image_dict)
            elif position > 2:
            # code for image position 3 and above
                image_dict = variant_level_dictionary_3(filename, output_folder_path)
                image_list.append(image_dict)

    return image_list

# Call process_image function when the "Process Images" button is clicked
def process_images():
    global images_list
    images_list = process_image()
    write_csv(images_list)


process_button = tk.Button(root, text="Process Images", command=process_images)
process_button.grid(row=6, column=6, padx=10, pady=10)




# Run the main event loop
root.mainloop()

# Destroy the GUI window and exit the application
root.destroy()
