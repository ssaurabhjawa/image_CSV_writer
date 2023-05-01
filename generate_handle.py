import uuid
# Create new Entry widget for product type
def generate_handle(product_info):
    handle = f"{product_info[0]}-{product_info[1]}".lower().replace(' ', '-')
    unique_id = str(uuid.uuid4()).split('-')[-1]
    handle = f"{handle}-{unique_id}"
    return handle