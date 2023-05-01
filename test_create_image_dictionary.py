from create_dict import create_img_dictionary
import os
product_sizes = {
    "Canvas": {
        "Landscape": ["16x12", "20x16", "24x18"],
        "Portrait": ["12x16", "16x20", "18x24"]
    },
    "Mug": {
        "Landscape": ["11oz", "15oz"],
        "Portrait": ["11oz", "15oz"]
    }
}

def test_create_img_dictionary():
    file_name = "1.0--9cc4fa--Canvas--animal Letters9898--1.png"
    img_dict = create_img_dictionary(file_name)
    print(img_dict)

test_create_img_dictionary()

