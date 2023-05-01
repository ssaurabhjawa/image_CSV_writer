from pricing_dict import productType_dict, artist_royalty_dict


def calculate_price(width, height, product_type, art_source, artist_royalty=0, artist_name=None):
    price_per_sq_m = productType_dict.get(product_type)

    if not price_per_sq_m:
        return None

    width_m = width / 100
    height_m = height / 100

    if art_source == "AI":
        price = width_m * height_m * price_per_sq_m
    elif art_source == "Artist":
        artist_royalty_fee = price_per_sq_m * width_m * height_m * artist_royalty
        price = price_per_sq_m * width_m * height_m + artist_royalty_fee
    elif art_source == "Shutterstock":
        price = price_per_sq_m * width_m * height_m + 257
    else:
        return None

    return round(price, 2)




def test_calculate_price():
    # Test AI pricing for Canvas
    print(calculate_price(60.96, 91.44, "Canvas", "AI"))

    # Test Artist pricing for Canvas with artist royalty
    print(calculate_price(60.96, 91.44, "Canvas", "Artist", artist_name="Artist 1"))

    # Test Shutterstock pricing for Acrylic
    print(calculate_price(50, 50, "Acrylic", "Shutterstock"))

    # Test unknown product type
    print(calculate_price(50, 50, "Unknown", "AI") is None)

    # Test unknown artist name
    print(calculate_price(50, 50, "Canvas", "Artist", artist_name="Unknown") is None)




if __name__ == "__main__":
    test_calculate_price()
    print("Everything passed")

