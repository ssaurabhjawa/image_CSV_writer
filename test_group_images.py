from group_images import group_images
def test_group_images():
    # Create a list of image dictionaries with different handles and image positions
    images = [
        {"handle": "product1", "image_position": 1, "url": "https://example.com/image1.jpg"},
        {"handle": "product1", "image_position": 2, "url": "https://example.com/image2.jpg"},
        {"handle": "product2", "image_position": 1, "url": "https://example.com/image3.jpg"},
        {"handle": "product3", "image_position": 1, "url": "https://example.com/image4.jpg"},
        {"handle": "product3", "image_position": 2, "url": "https://example.com/image5.jpg"}
    ]
    print(images)

    # Call the group_images function to group the images by product handle
    grouped_images = group_images(images)
    print(grouped_images)

    # Check that the grouped images dictionary contains the correct keys and values
    assert grouped_images == {
        "product1": {"Image Src": ["https://example.com/image1.jpg"]},
        "product2": {"Image Src": ["https://example.com/image3.jpg"]},
        "product3": {"Image Src": ["https://example.com/image4.jpg", "https://example.com/image5.jpg"]}
    }

test_group_images()