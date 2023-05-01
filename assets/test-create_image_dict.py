from create_dict import create_image_dict

def test_create_image_dict():
    image_path = "C:/Users/Saurabh/Documents/Python Scripts/Products/Products/T-Shirt-Spring flower-02-tshirtab.jpg"
    public_id = "test_public_id"
    image_dict = create_image_dict(image_path, public_id)
    print(image_dict)

test_create_image_dict()