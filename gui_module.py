import tkinter as tk
root = tk.Tk()

from pricing_dict import artist_royalty_dict
# from rename_file_with_position import rename_file_with_position


# Button to rename selected image file with highest image position from entry box
# rename_with_position_button = tk.Button(root, text="Rename File with Next Position", command=rename_file_with_position)
# rename_with_position_button.grid(row=3, column=3, padx=10, pady=10,sticky='e')


# Create dropdown variable and set default value
selected_artist = tk.StringVar(root)
# Create the dropdown menu
artist_dropdown = ttk.Combobox(root, values=list(artist_royalty_dict.keys()))

# Configure the dropdown menu
artist_dropdown.config(state="readonly", width=50)

# Display the dropdown menu using grid
artist_dropdown.grid(row=0, column=1)
