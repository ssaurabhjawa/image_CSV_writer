

def create_product_size_dict(product_type):
    # Define the product sizes for each product type
    product_sizes = {
        "canvas": {
            "Landscape": [
                {"width": 16, "height": 13, "ratio": 1.230769231},
                {"width": 22, "height": 18, "ratio": 1.222222222},
                {"width": 30, "height": 24, "ratio": 1.25},
            ],
            "Portrait": [
                {"width": 19, "height": 10, "ratio": 1.9},
                {"width": 24, "height": 12, "ratio": 2},
                {"width": 36, "height": 19, "ratio": 1.894736842},
            ],
            "Square": [
                {"width": 13, "height": 13},
                {"width": 18, "height": 18},
                {"width": 24, "height": 24},
            ],
        },
        "acrylic": {
            "Landscape": [
                {"width": 10, "height": 8, "ratio": 1.25},
                {"width": 19, "height": 13, "ratio": 1.461538462},
                {"width": 24, "height": 18, "ratio": 1.333333333},
                {"width": 36, "height": 24, "ratio": 1.5},
            ],
            "Portrait": [
                {"width": 8, "height": 10, "ratio": 0.8},
                {"width": 13, "height": 19, "ratio": 0.6842105263},
                {"width": 18, "height": 24, "ratio": 0.75},
                {"width": 24, "height": 36, "ratio": 0.6666666667},
            ],
            "Square": [
                {"width": 10, "height": 10, "ratio": 1},
                {"width": 20, "height": 20, "ratio": 1},
                {"width": 30, "height": 30, "ratio": 1},
            ],
        },
        "poster": {
            "Portrait": [
                {"width": 13, "height": 17, "ratio": 0.7647058824},
                {"width": 18, "height": 24, "ratio": 0.75},
                {"width": 24, "height": 34, "ratio": 0.7058823529},
            ],
            "Landscape": [
                {"width": 9, "height": 12, "ratio": 0.75},
                {"width": 12, "height": 16, "ratio": 0.75},
                {"width": 18, "height": 24, "ratio": 0.75},
                {"width": 30, "height": 40, "ratio": 0.75},
            ],
        },
        "art_prints": {
            "Portrait": [
                {"width": 13, "height": 16, "ratio": 0.8125},
                {"width": 18, "height": 22, "ratio": 0.8181818182},
                {"width": 24, "height": 30, "ratio": 0.8},
            ],
        },
    }

    # Define the option values based on the product type
    if product_type in product_sizes:
        option1_values = []
        for size in product_sizes[product_type]:
            for dimensions, ratio in product_sizes[product_type][size].items():
                option1_values.append(f"{size} ({dimensions}, {ratio})")
    else:
        option1_values = []

    # Create a dictionary of product sizes for the selected product type
    product_size_dict = {}
    for filename in os.listdir("images"):
        if (
            filename.endswith(".jpg")
            or filename.endswith(".jpeg")
            or filename.endswith(".png")
        ):
            selected_file = os.path.splitext(filename)[0]
            product_info = selected_file.split("--")
            handle = generate_handle(product_info)
            title = product_info[1]
            product_type = product_info[0]
            size = product_info[2]
            option1_name = "Size"
            option1_value = (
                f"{size} ({product_sizes[product_type][size][size+'x'+size]}, {product_sizes[product_type][size][size+'x'+size]})"
                if product_type in product_sizes
                and size in product_sizes[product_type]
                and size + "x" + size in product_sizes[product_type][size]
                else ""
            )
            product_size_dict[filename] = {
                "handle": handle,
                "title": title,
                "product_type": product_type,
                "size": size,
                "option1_name": option1_name,
                "option1_value": option1_value,
            }

    return option1_name, option1_value, product_sizes


import cloudinary
import cloudinary.uploader

cloudinary.config(
  cloud_name = "djqvqmqe2",
  api_key = "215651395579232",
  api_secret = "gAA9lxku5Idr4AZNOTaLHnROghk"
)

csv_filename = "product_upload.csv"

def create_csv():
    # Prompt user to select output folder
    output_folder = filedialog.askdirectory(title="Select Output Folder")
    
    # Get list of images in output folder
    image_list = os.listdir(output_folder_path)
    
    # Initialize CSV file and write header row
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        csv_header = [
            'Handle',
            'Title',
            'Body (HTML)',
            'Vendor',
            'Type',
            'Tags',
            'Published',
            'Option 1 Name',
            'Option 1 Value',
            'Variant SKU',
            'Variant Grams',
            'Variant Inventory Tracker',
            'Variant Inventory Qty',
            'Variant Inventory Policy',
            'Variant Fulfillment Service',
            'Variant Price',
            'Variant Compare At Price',
            'Variant Requires Shipping',
            'Variant Taxable',
            'Variant Barcode',
            'Image Src',
            'Image Position',
            'Image Alt Text',
            'Gift Card',
            'SEO Title',
            'SEO Description',
            'Variant Image',
            'Variant Weight Unit',
            'Variant Tax Code',
            'Cost per item'
        ]
        writer.writerow(csv_header)
        
        # Loop through each image in output folder and create a row in the CSV file
        for i, image_filename in enumerate(image_list):
            # Get image metadata from Cloudinary
            image_url = cloudinary.utils.cloudinary_url(image_filename)[0]
            image_metadata = cloudinary.uploader.explicit(image_filename, type='upload', eager=[{'width': 600, 'height': 800, 'crop': 'pad'}], metadata=True)
            
            # Extract handle, title, product_type, size, option1_name, and option1_value from selected file name
            product_info = image_filename.split('--')
            handle = generate_handle(product_info)
            title = product_info[1]
            product_type = product_info[0]
            
            # Get option 1 name and values
            option1_name, option1_values, product_size_dict  = create_product_size_dict(product_type)
            
            # Create product size dictionary/metadata for image
            # ...
            
            # Get image metadata from Cloudinary
            image_url = cloudinary.utils.cloudinary_url(image_filename)[0]
            image_metadata = cloudinary.uploader.explicit(image_filename, type='upload', eager=[{'width': 600, 'height': 800, 'crop': 'pad'}], metadata=True)
            
            # Add image metadata to product size dictionary/metadata
            # ...
            import csv

# Define the output CSV file name
output_csv = "product_metadata.csv"

# Open the CSV file for writing
with open(output_csv, "w", newline="") as f:
    writer = csv.writer(f)

    # Write the header row
    header = [
        "Handle",
        "Title",
        "Body (HTML)",
        "Vendor",
        "Type",
        "Tags",
        "Published",
        "Option 1 Name",
        "Option 1 Value",
        "Variant SKU",
        "Variant Grams",
        "Variant Inventory Tracker",
        "Variant Inventory Qty",
        "Variant Inventory Policy",
        "Variant Fulfillment Service",
        "Variant Price",
        "Variant Compare At Price",
        "Variant Requires Shipping",
        "Variant Taxable",
        "Variant Barcode",
        "Image Src",
        "Image Position",
        "Image Alt Text",
        "Gift Card",
        "SEO Title",
        "SEO Description",
        "Variant Image",
        "Variant Weight Unit",
        "Variant Tax Code",
        "Cost per item"
    ]
    writer.writerow(header)

    # Loop through the product size dictionary/metadata and write each row to the CSV file
    for filename, metadata in product_size_dict.items():
        row = [
            metadata["handle"],
            metadata["title"],
            "",
            "",
            metadata["product_type"],
            "",
            "TRUE",
            metadata["option1_name"],
            metadata["option1_value"],
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            metadata["image_src"],
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        writer.writerow(row)


               


create_csv_button = tk.Button(root, text="Create CSV", command=create_csv)
create_csv_button.pack()