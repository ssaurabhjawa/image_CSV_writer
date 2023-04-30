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
