title_var = tk.StringVar(root)
# Create variable for image position
image_position_var = tk.IntVar(value=0)



def rename_file_with_position():
    # Get selected file from the current selection Listbox
    selected_file = current_selection_listbox.get(current_selection_listbox.curselection())
    img_path = os.path.normpath(os.path.join(image_folder, selected_file))
    print(img_path)

    if not selected_file:
        tk.messagebox.showerror("Error", "Please select an image to rename.")
        return

    # Get the new filename from the highest_image_position_entry input box
    new_filename = highest_image_position_entry.get()

    # Rename the file with the new filename
    try:
        os.rename(img_path, os.path.join(image_folder, new_filename))

        # Copy file to output folder with new filename
        shutil.copy(os.path.join(image_folder, new_filename), os.path.join(output_folder_path, new_filename))

        # Update current selection Listbox
        current_selection_listbox.delete(0, tk.END)
        current_selection_listbox.insert(0, new_filename)

        # Clear current_selection_listbox
        current_selection_listbox.selection_clear(0, tk.END)

        # Update image_listbox
        image_listbox.delete(0, tk.END)
        for file in os.listdir(image_folder):
            if file.endswith((".jpg", ".jpeg", ".png")):
                image_listbox.insert(tk.END, file)

        # Update output_listbox
        output_listbox.delete(0, tk.END)
        for file in os.listdir(output_folder_path):
            if file.endswith((".jpg", ".jpeg", ".png")):
                output_listbox.insert(tk.END, file)

        # Update renamed_listbox
        renamed_files.append(new_filename)
        renamed_listbox.delete(0, tk.END)
        for file in renamed_files:
            renamed_listbox.insert(tk.END, file)

    except Exception as e:
        tk.messagebox.showerror("Error", f"An error occurred while renaming the file: {e}")
        # Print error message to console for debugging
        print(f"Error occurred while renaming the file: {str(e)}")


def find_name():
    # Get the selected filename from the output listbox
    selected_filename = output_listbox.get(output_listbox.curselection())

    # Split filename into its components
    parts = selected_filename.split("--")
    product_type = parts[0]
    title = parts[1]
    aspect_ratio = parts[2]

    # Find existing files with the same product type, title, and aspect ratio in output folder
    output_files = [f for f in os.listdir(output_folder_path) if f.startswith(f"{product_type}--{title}--{aspect_ratio}")]
    image_positions = [int(os.path.splitext(f.split("--")[3])[0]) for f in output_files]
    if len(image_positions) == 0:
        next_image_position = 1
    else:
        next_image_position = max(image_positions) + 1

    # Update the title_entry with the next available image position
    highest_image_position_entry.delete(0, END)
    highest_image_position_entry.insert(0, f"{product_type}--{title}--{aspect_ratio}--{next_image_position}")

    # Set the focus on the option_value_entry for easy editing
    highest_image_position_entry.focus()



find_name_button = tk.Button(root, text="Use Name", command=find_name)
find_name_button.grid(row=3, column=3, padx=5, pady=5, sticky="w")


# Create new Entry widget for highest image position
highest_image_position_entry = tk.Entry(root, width=70)
highest_image_position_entry.grid(row=2, column=3, padx=5, pady=5, sticky="w")