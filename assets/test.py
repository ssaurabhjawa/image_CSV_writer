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
import unittest


def generate_handle(product_info):
    handle = f"{product_info[0]}-{product_info[1]}".lower().replace(' ', '-')
    unique_id = str(uuid.uuid4()).split('-')[-1]
    handle = f"{handle}-{unique_id}"
    return handle


def create_product_size_dict(product_type):
    # Define the product sizes for each product type
    # product_sizes = {
    #     "canvas": {
    #         "Landscape": [
    #             {"width": 16, "height": 13, "ratio": 1.230769231},
    #             {"width": 22, "height": 18, "ratio": 1.222222222},
    #             {"width": 30, "height": 24, "ratio": 1.25},
    #         ],
    #         "Portrait": [
    #             {"width": 19, "height": 10, "ratio": 1.9},
    #             {"width": 24, "height": 12, "ratio": 2},
    #             {"width": 36, "height": 19, "ratio": 1.894736842},
    #         ],
    #         "Square": [
    #             {"width": 13, "height": 13},
    #             {"width": 18, "height": 18},
    #             {"width": 24, "height": 24},
    #         ],
    #     },
    #     "acrylic": {
    #         "Landscape": [
    #             {"width": 10, "height": 8, "ratio": 1.25},
    #             {"width": 19, "height": 13, "ratio": 1.461538462},
    #             {"width": 24, "height": 18, "ratio": 1.333333333},
    #             {"width": 36, "height": 24, "ratio": 1.5},
    #         ],
    #         "Portrait": [
    #             {"width": 8, "height": 10, "ratio": 0.8},
    #             {"width": 13, "height": 19, "ratio": 0.6842105263},
    #             {"width": 18, "height": 24, "ratio": 0.75},
    #             {"width": 24, "height": 36, "ratio": 0.6666666667},
    #         ],
    #         "Square": [
    #             {"width": 10, "height": 10, "ratio": 1},
    #             {"width": 20, "height": 20, "ratio": 1},
    #             {"width": 30, "height": 30, "ratio": 1},
    #         ],
    #     },
    #     "poster": {
    #         "Portrait": [
    #             {"width": 13, "height": 17, "ratio": 0.7647058824},
    #             {"width": 18, "height": 24, "ratio": 0.75},
    #             {"width": 24, "height": 34, "ratio": 0.7058823529},
    #         ],
    #         "Landscape": [
    #             {"width": 9, "height": 12, "ratio": 0.75},
    #             {"width": 12, "height": 16, "ratio": 0.75},
    #             {"width": 18, "height": 24, "ratio": 0.75},
    #             {"width": 30, "height": 40, "ratio": 0.75},
    #         ],
    #     },
    #     "art_prints": {
    #         "Portrait": [
    #             {"width": 13, "height": 16, "ratio": 0.8125},
    #             {"width": 18, "height": 22, "ratio": 0.8181818182},
    #             {"width": 24, "height": 30, "ratio": 0.8},
    #         ],
    #     },
    # }

    product_sizes = {
    "canvas": {
        "Landscape": {
            "16x13": 1.230769231,
            "22x18": 1.222222222,
            "30x24": 1.25,
        },
        "Portrait": {
            "19x10": 1.9,
            "24x12": 2,
            "36x19": 1.894736842,
        },
        "Square": {
            "13x13": 1,
            "18x18": 1,
            "24x24": 1,
        },
    },
    "acrylic": {
        "Landscape": {
            "10x8": 1.25,
            "19x13": 1.461538462,
            "24x18": 1.333333333,
            "36x24": 1.5,
        },
        "Portrait": {
            "8x10": 0.8,
            "13x19": 0.6842105263,
            "18x24": 0.75,
            "24x36": 0.6666666667,
        },
        "Square": {
            "10x10": 1,
            "20x20": 1,
            "30x30": 1,
        },
    },
    "poster": {
        "Portrait": {
            "13x17": 0.7647058824,
            "18x24": 0.75,
            "24x34": 0.7058823529,
        },
        "Landscape": {
            "9x12": 0.75,
            "12x16": 0.75,
            "18x24": 0.75,
            "30x40": 0.75,
        },
    },
    "art_prints": {
        "Portrait": {
            "13x16": 0.8125,
            "18x22": 0.8181818182,
            "24x30": 0.8,
        },
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

    return option1_name, option1_value, product_size_dict

class TestCreateProductSizeDict(unittest.TestCase):
    def test_create_product_size_dict(self):
        product_type = 'canvas'
        expected_option1_name = 'Size'
        expected_option1_values = ['Landscape (16, 13, 1.230769231)', 'Landscape (22, 18, 1.222222222)', 'Landscape (30, 24, 1.25)', 'Portrait (19, 10, 1.9)', 'Portrait (24, 12, 2)', 'Portrait (36, 19, 1.894736842)', 'Square (13, 13)', 'Square (18, 18)', 'Square (24, 24)']
        expected_product_size_dict = {
            'canvas--Mountains--Landscape.jpg': {'handle': 'canvas-mountains-landscape', 'title': 'Mountains', 'product_type': 'canvas', 'size': 'Landscape', 'option1_name': 'Size', 'option1_value': 'Landscape (16, 13, 1.230769231)'},
            'canvas--Mountains--Portrait.jpg': {'handle': 'canvas-mountains-portrait', 'title': 'Mountains', 'product_type': 'canvas', 'size': 'Portrait', 'option1_name': 'Size', 'option1_value': 'Portrait (19, 10, 1.9)'},
            'canvas--Mountains--Square.jpg': {'handle': 'canvas-mountains-square', 'title': 'Mountains', 'product_type': 'canvas', 'size': 'Square', 'option1_name': 'Size', 'option1_value': 'Square (13, 13)'}
        }

        option1_name, option1_values, product_size_dict = create_product_size_dict(product_type)

        self.assertEqual(option1_name, expected_option1_name)
        self.assertEqual(option1_values, expected_option1_values)
        self.assertEqual(product_size_dict, expected_product_size_dict)

if __name__ == '__main__':
    unittest.main()