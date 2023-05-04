def extract_file_info(file_path):
    # Extract file name from file path
    file_name = os.path.basename(file_path)
    # Split file name into parts based on delimiter
    file_parts = file_name.split("--")

    # Extract variables from file parts
    aspect_ratio = float(file_parts[0])
    uuid = file_parts[1]
    product_type = file_parts[2]
    title_var = file_parts[3]
    image_position_var = int(file_parts[4])
    artist_name = os.path.splitext(file_parts[5])[0]

    # Derive orientation from aspect ratio
    if aspect_ratio < 1:
        orientation = "Portrait"
    elif aspect_ratio > 1:
        orientation = "Landscape"
    else:
        orientation = "Square"

    # Define the option values based on the product type and orientation
    if product_type.lower() in product_sizes and orientation in product_sizes[product_type.lower()]:
        option1_values = []
        option1_prices = []
        for dimensions in product_sizes[product_type.lower()][orientation]:
            option1_values.append(dimensions["size"])
            price = dimensions["price"]
            if artist_name in artist_prices:
                price = price * artist_prices[artist_name]
            option1_prices.append(price)
    else:
        option1_values = []
        option1_prices = []

    # Create dictionary containing the extracted variables
    file_info = {
        "aspect_ratio": aspect_ratio,
        "uuid": uuid,
        "product_type": product_type,
        "title_var": title_var,
        "image_position_var": image_position_var,
        "vendor": artist_name,
        "option1_values": option1_values,
        "option1_prices": option1_prices
    }

    return file_info


def extract_file_info(file_path):
    # Extract file name from file path
    file_name = os.path.basename(file_path)
    # Split file name into parts based on delimiter
    file_parts = file_name.split("--")

    # Extract variables from file parts
    aspect_ratio = float(file_parts[0])
    uuid = file_parts[1]
    product_type = file_parts[2]
    title_var = file_parts[3]
    image_position_var = int(file_parts[4])
    artist_name = os.path.splitext(file_parts[5])[0]

    # Check if the product type is canvas and adjust aspect ratio based on tolerance
    if product_type.lower() == "canvas":
        option1_values = []
        for dimensions in product_sizes[product_type.lower()]["portrait"]:
            ratio_tolerance = dimensions["ratio"] * 0.05
            if abs(aspect_ratio - dimensions["ratio"]) <= ratio_tolerance:
                option1_values.append(dimensions["size"])
    else:
        # Derive orientation from aspect ratio
        if aspect_ratio < 1:
            orientation = "Portrait"
        elif aspect_ratio > 1:
            orientation = "Landscape"
        else:
            orientation = "Square"

        # Define the option values based on the product type and orientation
        if product_type.lower() in product_sizes and orientation in product_sizes[product_type.lower()]:
            option1_values = []
            for dimensions in product_sizes[product_type.lower()][orientation]:
                option1_values.append(dimensions["size"])
        else:
            option1_values = []

    # Check if artist is Shutterstock or Artist 1/2/3 and adjust price accordingly
    if artist_name == "Shutterstock":
        price_factor = 1.1
    elif artist_name in artist_prices:
        price_factor = artist_prices[artist_name]
    else:
        price_factor = 1.0

    # Adjust price based on artist
    if product_type.lower() == "canvas":
        option1_values = [size + " - " + str(round(float(size.split("x")[0]) * float(size.split("x")[1]) * 0.01 * product_sizes[product_type.lower()]["portrait"][i]["price"] * price_factor, 2)) for i, size in enumerate(option1_values)]
    else:
        option1_values = [size + " - " + str(round(product_sizes[product_type.lower()][orientation][i]["price"] * price_factor, 2)) for i, size in enumerate(option1_values)]

    # Create dictionary containing the extracted variables
    file_info = {
        "aspect_ratio": aspect_ratio,
        "uuid": uuid,
        "product_type": product_type,
        "title_var": title_var,
        "image_position_var": image_position_var,
        "vendor": artist_name,
        "option1_values": option1_values
    }

    return file_info
