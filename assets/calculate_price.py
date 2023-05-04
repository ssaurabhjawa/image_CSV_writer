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