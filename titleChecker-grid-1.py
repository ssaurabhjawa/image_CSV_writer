import os
import csv
import tkinter as tk
from tkinter import filedialog, ttk, Listbox, Canvas, NW, END, messagebox
from PIL import Image, ImageTk
import csv
import shutil
from PIL import Image
import cloudinary
import cloudinary.uploader
import cloudinary.api
import uuid
import tkinter.simpledialog


from pricing_dict import artist_royalty_dict
from segregate import segregate_images_by_ratio


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
select_folder_button = tk.Button(root, text="Select Folder", command=select_folder)
select_folder_button.grid(row=0, column=0, padx=5, pady=5)

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
#                           Artist Dropdown
#==================================================================

artist_label = tk.Label(root, text="Artist:")
artist_label.grid(row=3, column=1, padx=5, pady=5,sticky='n')
# Create the dropdown menu
selected_artist = tk.StringVar(root, value=list(artist_royalty_dict.keys())[0])
artist_dropdown = ttk.Combobox(root, textvariable=selected_artist, values=list(artist_royalty_dict.keys()))

# Configure the dropdown menu
artist_dropdown.config(state="readonly", width=10)
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
        print(aspect_ratio)

    # Get file extension
    ext = os.path.splitext(selected_file)[1]

    # Create new filename with aspect ratio and UUID
    new_filename = f"{aspect_ratio}--{uuid.uuid4().hex[:6]}--{product_type_var.get()}--{title_var.get()}--{image_position_var.get()}{ext}"

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
#                           Segregate
#==================================================================
def segregate_images():
    aspect_ratios = {"1.33": [], "1.5": [], "1.6": [], "1.77": [], "1.85": [], "2": [], "2.2": [], "2.39": []}
    segregate_images_by_ratio("C:/Users/Saurabh/Documents/Python Scripts/Products/Products", aspect_ratios)


# Create button to segregate images
segregate_button = tk.Button(root, text="Segregate Images", command=segregate_images)
segregate_button.grid(row=1, column=3, padx=10, pady=10)


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
            # Get aspect ratio, uuid, product type, and title from the filename
            filename_parts = file.split("--")
            aspect_ratio = filename_parts[0]
            uuid = filename_parts[1]
            product_type_var.set(filename_parts[2])
            title_var.set(filename_parts[3])

            # Create new filename with updated image position number
            ext = os.path.splitext(file)[1]
            new_filename = f"{aspect_ratio}--{uuid}--{product_type_var.get()}--{title_var.get()}--{image_position}{ext}"

            # Rename file
            os.rename(os.path.join(folder_path, file), os.path.join(folder_path, new_filename))

    # Update image_listbox
    image_listbox.delete(0, tk.END)
    for file in os.listdir(folder_path):
        if file.endswith((".jpg", ".jpeg", ".png")):
            image_listbox.insert(tk.END, file)
    
    tk.messagebox.showinfo("Success", f"All files in {folder_path} have been renamed with image position {image_position}.")


# Create the "Update Image Position" button
update_position_button = tk.Button(root, text="Update Image Position", command=update_image_position)
update_position_button.grid(row=3, column=3, padx=5, pady=5)




# Run the main event loop
root.mainloop()

# Destroy the GUI window and exit the application
root.destroy()
