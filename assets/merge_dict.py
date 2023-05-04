images = [
    {'handle': 'product1', 'image_position': 1, 'image_src': ['url1']},
    {'handle': 'product1', 'image_position': 2, 'image_src': ['url2']},
    {'handle': 'product2', 'image_position': 1, 'image_src': ['url3']},
    {'handle': 'product3', 'image_position': 1, 'image_src': ['url4']},
    {'handle': 'product3', 'image_position': 2, 'image_src': ['url5']},
]




def merge_images(images):
    merged_images = {}
    for image in images:
        handle = image['handle']
        position = image['image_position']
        if handle not in merged_images:
            merged_images[handle] = {
                'handle': handle,
                'image_position': position,
                'image_src': image['image_src']
            }
        else:
            merged_images[handle]['image_src'].extend(image['image_src'])
    return list(merged_images.values())


    return merged_list




merged_images = merge_images(images)
print(merged_images)


# def group_images(images):
#     # Sort the images by image position
#     images_sorted = sorted(images, key=lambda x: x['image_position'])
    
#     # Group the images by handle and merge the image URLs
#     handle_groups = {}
#     for image in images_sorted:
#         handle = image['handle']
#         image_src = image['image_src']
        
#         if handle not in handle_groups:
#             handle_groups[handle] = {'handle': handle, 'image_position': image['image_position'], 'image_src': image_src}
#         else:
#             handle_groups[handle]['image_src'].extend(image_src)
            
#     return list(handle_groups.values())
