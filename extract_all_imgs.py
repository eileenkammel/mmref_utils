# -*-coding:utf-8 -*-
# Author: Eileen Kammel, 811770
# Date: 2024-09-15 12:46:12

# Get a full list of all remaining images and their attributes

import os
import json
import shutil


def extract_imgs():
    # Create a directory for the extracted images
    path = "tuna/imgs"
    if not os.path.exists(path):
        os.makedirs(path)
    old_img_path = "tuna_original/dist/images/furniture"
    img_counter = 0
    imgs_seen = set()
    img = {"IMAGES": []}
    # go through all episodes and write unique images in file
    for filename in os.listdir("tuna"):
        if filename.endswith(".json"):
            file_path = os.path.join("tuna", filename)
            with open(file_path, "r") as json_file:
                for entity in json.load(json_file)["TRIAL"]["DOMAIN"]["ENTITY"]:
                    img_id = entity["@ID"]
                    img_filename = entity["@IMAGE"]
                    img_path = os.path.join(old_img_path, img_filename)
                    # change filename to mask content
                    img_new_filename = f"{img_counter}.png"
                    # check if image is already seen
                    if img_id not in imgs_seen:
                        imgs_seen.add(img_id)
                        img_counter += 1
                        # replace filename
                        entity["@IMAGE"] = img_new_filename
                        img["IMAGES"].append(entity)
                        # copy image to new directory
                        if os.path.exists(img_path):
                            shutil.copy(img_path, os.path.join(path, img_new_filename))
            # delete file after reading
            os.remove(file_path)
    all_imgs = os.path.join(path, "all_imgs.json")
    with open(all_imgs, "w") as json_file:
        json.dump(img, json_file, indent=4)


if __name__ == "__main__":
    extract_imgs()
