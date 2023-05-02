def group_images(images):
    # Create an empty dictionary to store the grouped images
    grouped_images = {}

    # Iterate over the list of images
    for image in images:
        # Get the product handle and image position
        product_handle = image['handle']
        image_position = image['image_position']

        # Check if the product handle is already in the grouped images dictionary
        if product_handle in grouped_images:
            # If the product handle is already in the dictionary, append the image URL to the corresponding list
            if image_position == 1:
                grouped_images[product_handle]['Image Src'].append(image['url'])
        else:
            # If the product handle is not in the dictionary, create a new dictionary for the product
            if image_position == 1:
                grouped_images[product_handle] = {
                    'Handle': product_handle,
                    'Title': image['title'],
                    'Vendor': image['vendor'],
                    'Body (HTML)': image['body_html'],
                    'Tags': image['tags'],
                    'Image Src': [image['url']],
                    'Variant SKU': [],
                    'Variant Grams': [],
                    'Variant Inventory Tracker': '',
                    'Variant Inventory Qty': [],
                    'Variant Inventory Policy': '',
                    'Variant Fulfillment Service': '',
                    'Variant Price': [],
                    'Variant Compare At Price': [],
                    'Variant Requires Shipping': '',
                    'Variant Taxable': '',
                    'Variant Barcode': '',
                    'Option1 Name': '',
                    'Option1 Value': [],
                    'Option2 Name': '',
                    'Option2 Value': [],
                    'Option3 Name': '',
                    'Option3 Value': [],
                    'Variant Image': [],
                    'Variant Weight Unit': '',
                    'Variant Tax Code': ''
                }
    return list(grouped_images.values())
