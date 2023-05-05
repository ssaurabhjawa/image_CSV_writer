# def variant_level_dictionary(image_filename, output_folder_path, option, price):
#     file_path = os.path.join(output_folder_path, image_filename)
#     public_id = upload_to_cloudinary(file_path)
#     # Extract image information from filename
#     file_info = extract_file_info(image_filename)
#     aspect_ratio = file_info["aspect_ratio"]
#     uuid = file_info["uuid"]
#     product_type = file_info["product_type"]
#     title = file_info["title_var"]
#     image_position = file_info["image_position_var"]
#     artist= file_info["vendor"]

#     # Create a dictionary for the image with all the CSV fields
#     image_dict = {
#         "Handle":uuid ,
#         "Title": title,
#         "Body (HTML)": "",
#         "Vendor": artist,
#         "Product Category": "",
#         "Type": product_type,
#         "Tags": "Miscellaneous",
#         "Published": "TRUE",
#         "Option1 Name": "Size",
#         "Option1 Value":option,
#         "Option2 Name": "",
#         "Option2 Value": "",
#         "Option3 Name": "",
#         "Option3 Value": "",
#         "Variant Price":price if price else "",
#         "Image Src": get_image_url_from_cloudinary(public_id),  # Use the Cloudinary URL
#         "Image Alt Text": title,
#         "Gift Card": "FALSE",
#         "SEO Title": "",
#         "SEO Description": "",
#         "Variant Image": "",
#         "Variant Weight Unit": "kg",
#         "Variant Tax Code": "",
#         "Cost per item": "",
#         "Included / United Arab Emirates": "TRUE",
#         "Included / International": "FALSE",
#         "Price / International": "",
#         "Compare At Price / International": "",
#         "Status": "active",
#         "image_position": image_position,
#          }

#     return image_dict