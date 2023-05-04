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
#==================================================================
#      Step 5. Merge Dictionary
#==================================================================

def merge_image_dicts(images):
    # Create a dictionary to store the merged images
    merged_dict = {}

    # Loop through each image dictionary in the list
    for image in images:
        handle = image["Handle"]

        # If the handle is not in the merged_dict, create a new entry
        if handle not in merged_dict:
            merged_dict[handle] = image.copy()
            merged_dict[handle]["Image Src"] = [merged_dict[handle]["Image Src"]] # Convert to list
        # If the handle is already in the merged_dict, append the "Image Src" to the existing list
        else:
            merged_dict[handle]["Image Src"].append(image["Image Src"])

    # Return a list of the merged dictionaries
    return list(merged_dict.values())


import json

def group_images_by_handle(image_dicts):
    # Merge the image dictionaries based on the "Handle" field
    merged_images = merge_image_dicts(image_dicts)

    # Group the merged image dictionaries by handle
    grouped_images = {}
    for image in merged_images:
        handle = image["Handle"]
        if handle not in grouped_images:
            grouped_images[handle] = [image]
        else:
            grouped_images[handle].append(image)

    # Return a dictionary of lists of image dictionaries grouped by handle
    print(json.dumps(grouped_images, indent=4))
    return grouped_images


def process_and_merge():
    # Invoke process_directory function to populate imagesList
    process_directory()
    # Merge the dictionaries for images with the same handle
    merged_images = group_images_by_handle(imagesList)
    # Print the merged images to verify the results
    print(merged_images)



#==================================================================

