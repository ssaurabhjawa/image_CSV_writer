def create_product_dict(image_dict):
    """
    Takes in an image dictionary and returns a product level dictionary.

    Args:
    - image_dict (dict): a dictionary containing image information including variant-level data.

    Returns:
    - product_dict (dict): a dictionary containing product-level data.
    """
    product_dict = {}

    # Extract product-level data
    product_dict["Title"] = image_dict["title"]
    product_dict["Body (HTML)"] = image_dict["description"]
    product_dict["Vendor"] = image_dict["vendor"]
    product_dict["Type"] = image_dict["product_type"]
    product_dict["Tags"] = image_dict["tags"]
    product_dict["Published"] = "TRUE"  # assuming all products should be published

    # Extract image data for the first image
    product_dict["Image Src"] = image_dict["image_urls"][0]
    product_dict["Image Alt Text"] = image_dict["title"]

    # Set initial values for option and variant-related fields
    option1_name = None
    option2_name = None
    option3_name = None
    variant_sku_list = []
    variant_price_list = []
    variant_inventory_list = []

    # Iterate over each image in the image_dict to create the list of unique option values
    option_values_set = set()
    for image_data in image_dict.values():
        option_values_set.add((image_data["option1"], image_data["option2"], image_data["option3"]))

    # Set the option fields and create the list of variant level dictionaries
    if option_values_set:
        option1_name = image_dict["option1_name"]
        option2_name = image_dict.get("option2_name", "")
        option3_name = image_dict.get("option3_name", "")

        for option_values in option_values_set:
            variant_dict = {}
            variant_dict["Option1 Value"] = option_values[0]
            variant_dict["Option2 Value"] = option_values[1]
            variant_dict["Option3 Value"] = option_values[2]
            variant_sku_list.append(variant_dict["Variant SKU"])
            variant_price_list.append(variant_dict["Variant Price"])
            variant_inventory_list.append(variant_dict["Variant Inventory Qty"])

    # Set the option and variant fields in the product_dict
    product_dict["Option1 Name"] = option1_name
    product_dict["Option2 Name"] = option2_name
    product_dict["Option3 Name"] = option3_name
    product_dict["Variant SKU"] = ",".join(variant_sku_list)
    product_dict["Variant Grams"] = ""  # assuming all products have no weight
    product_dict["Variant Inventory Policy"] = "continue"  # assuming all products use continue policy
    product_dict["Variant Price"] = ",".join(variant_price_list)
    product_dict["Variant Requires Shipping"] = "TRUE"  # assuming all products require shipping
    product_dict["Variant Taxable"] = "TRUE"  # assuming all products are taxable
    product_dict["Variant Inventory Qty"] = ",".join(variant_inventory_list)

    return product_dict


def create_variant_dicts(image_dict):
    """
    Takes in an image dictionary and returns a list of variant level dictionaries.

    Args:
    - image_dict (dict): a dictionary containing image information including variant-level data.

    Returns:
    - variant_dicts (list of dicts): a list of variant level dictionaries.
    """
    variant_dicts = []

    # Iterate over each image in the image_dict to create the list of variant level dictionaries
    for image_data in image_dict.values():
