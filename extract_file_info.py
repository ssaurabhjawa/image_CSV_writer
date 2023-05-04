import os

product_sizes = {
    "canvas": {
        "Landscape": [
            {"width": 40.64, "height": 33.02, "ratio": 1.230769231},
            {"width": 55.88, "height": 45.72, "ratio": 1.222222222},
            {"width": 76.2, "height": 60.96, "ratio": 1.25},
        ],
        "Portrait": [
            {"width": 48.26, "height": 25.4, "ratio": 1.9},
            {"width": 60.96, "height": 30.48, "ratio": 2},
            {"width": 91.44, "height": 48.26, "ratio": 1.894736842},
        ],
        "Square": [
            {"width": 33.02, "height": 33.02},
            {"width": 45.72, "height": 45.72},
            {"width": 60.96, "height": 60.96},
        ],
    },
    "acrylic": {
        "Landscape": [
            {"width": 25.4, "height": 20.32, "ratio": 1.25},
            {"width": 48.26, "height": 33.02, "ratio": 1.461538462},
            {"width": 60.96, "height": 45.72, "ratio": 1.333333333},
            {"width": 91.44, "height": 60.96, "ratio": 1.5},
        ],
        "Portrait": [
            {"width": 20.32, "height": 25.4, "ratio": 0.8},
            {"width": 33.02, "height": 48.26, "ratio": 0.6842105263},
            {"width": 45.72, "height": 60.96, "ratio": 0.75},
            {"width": 60.96, "height": 91.44, "ratio": 0.6666666667},
        ],
        "Square": [
            {"width": 25.4, "height": 25.4, "ratio": 1},
            {"width": 50.8, "height": 50.8, "ratio": 1},
            {"width": 76.2, "height": 76.2, "ratio": 1},
        ],
    },
    "poster": {
        "Portrait": [
            {"width": 33.02, "height": 43.18, "ratio": 0.7647058824},
            {"width": 45.72, "height": 60.96, "ratio": 0.75},
            {"width": 60.96, "height": 86.36, "ratio": 0.7058823529},
        ],
        "Landscape": [
            {"width": 22.86, "height": 30.48, "ratio": 0.75},
            {"width": 30.48, "height": 40.64, "ratio": 0.75},
            {"width": 45.72, "height": 60.96, "ratio": 0.75},
            {"width": 76.2, "height": 101.65,  "ratio": 0.75},
        ],
        }
}
product_sizes = {
    "acrylic": {
        "Portrait": [
            {"size": "24x30cm", "ratio": 1.25, "price": 144},
            {"size": "32x40cm", "ratio": 1.25, "price": 256},
            {"size": "48x60cm", "ratio": 1.25, "price": 576},
            {"size": "64x80cm", "ratio": 1.25, "price": 1024},
        ],
        "Landscape": [
            {"size": "30x24cm", "ratio": 1.25, "price": 144},
            {"size": "40x32cm", "ratio": 1.25, "price": 256},
            {"size": "60x48cm", "ratio": 1.25, "price": 576},
            {"size": "80x64cm", "ratio": 1.25, "price": 1024},
        ],
        "Square": [
            {"size": "24x24cm", "ratio": 1.0, "price": 115.2},
            {"size": "40x40cm", "ratio": 1.0, "price": 320},
            {"size": "60x60cm", "ratio": 1.0, "price": 720},
            {"size": "80x80cm", "ratio": 1.0, "price": 1280},
        ],
    },
    "canvas": {
        "Portrait": [
            {"size": "100x150cm", "ratio": 0.67, "price": 750},
            {"size": "80x120cm", "ratio": 0.67, "price": 480},
            {"size": "60x90cm", "ratio": 0.67, "price": 270},
            {"size": "40x60cm", "ratio": 0.67, "price": 120},
            {"size": "105x140cm", "ratio": 0.75, "price": 735},
            {"size": "90x120cm", "ratio": 0.75, "price": 540},
            {"size": "60x80cm", "ratio": 0.75, "price": 240},
            {"size": "54x72cm", "ratio": 0.75, "price": 194.4},
            {"size": "120x150cm", "ratio": 0.8, "price": 900},
            {"size": "80x100cm", "ratio": 0.8, "price": 400},
            {"size": "60x75cm", "ratio": 0.8, "price": 225},
            {"size": "40x50cm", "ratio": 0.8, "price": 100},
            {"size": "100x140cm", "ratio": 0.71, "price": 700},
            {"size": "80x112cm", "ratio": 0.71, "price": 448},
            {"size": "60x84cm", "ratio": 0.71, "price": 252},
            {"size": "50x70cm", "ratio": 0.71, "price": 175},
        ],
    },
    "canvas": {
        "Landscape": [
            {"size": "150x100cm", "ratio": 1.5, "price": 750},
            {"size": "120x80cm", "ratio": 1.5, "price": 480},
            {"size": "90x60cm", "ratio": 1.5, "price": 270},
            {"size": "60x40cm", "ratio": 1.5, "price": 120},
            {"size": "140x105cm", "ratio": 1.33, "price": 735},
            {"size": "120x90cm", "ratio": 1.33, "price": 540},
            {"size": "80x60cm", "ratio": 1.33, "price": 240},
            {"size": "72x54cm", "ratio": 1.33, "price": 194.4},
            {"size": "150x120cm", "ratio": 1.25, "price": 900},
            {"size": "100x80cm", "ratio": 1.25, "price": 400},
            {"size": "75x60cm", "ratio": 1.25, "price": 225},
            {"size": "50x40cm", "ratio": 1.25, "price": 100},
            {"size": "140x100cm", "ratio": 1.4, "price": 700},
            {"size": "112x80cm", "ratio": 1.4, "price": 448},
            {"size": "84x60cm", "ratio": 1.4, "price": 252},
            {"size": "70x50cm", "ratio": 1.4, "price": 175}
        ]
    },
}


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
            option1_values.append(f"{dimensions['size']}")
            option1_prices.append(dimensions['price'])
    elif product_type.lower() == "canvas" and orientation in product_sizes[product_type.lower()]:
        option1_values = []
        option1_prices = []
        for dimensions in product_sizes[product_type.lower()][orientation]:
            size_parts = dimensions['size'].split('x')
            width_cm = float(size_parts[0])
            height_cm = float(size_parts[1])
            aspect_ratio_tolerance = dimensions['ratio'] * 0.05
            aspect_ratio_min = dimensions['ratio'] - aspect_ratio_tolerance
            aspect_ratio_max = dimensions['ratio'] + aspect_ratio_tolerance
            if abs(aspect_ratio - (width_cm / height_cm)) <= aspect_ratio_tolerance:
                option1_values.append(f"{dimensions['size']}")
                option1_prices.append(dimensions['price'])
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
        "option1_name": "Size",
        "option1_values": option1_values,
        "option1_prices": option1_prices,
    }

    return file_info


def test_extract_file_info():
    file_path = "1.33--1234--Acrylic--Test--1--Artist.jpg"
    expected_output = {
        "aspect_ratio": 1.33,
        "uuid": "1234",
        "product_type": "Acrylic",
        "title_var": "Test",
        "image_position_var": 1,
        "vendor": "Artist",
        "option1_values": [
            {"size": "120x90cm", "ratio": 1.33, "price": 540},
            {"size": "140x105cm", "ratio": 1.33, "price": 735},
            {"size": "72x54cm", "ratio": 1.33, "price": 194.4},
            {"size": "80x60cm", "ratio": 1.33, "price": 240}
        ]
    }

    print(extract_file_info(file_path))

test_extract_file_info()