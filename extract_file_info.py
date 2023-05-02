import os

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


def extract_file_info(file_name):
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
        for dimensions in product_sizes[product_type.lower()][orientation]:
            option1_values.append(dimensions)
    else:
        option1_values = []

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
