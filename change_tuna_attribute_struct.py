# -*-coding:utf-8 -*-
# Author: Eileen Kammel, 811770
# Date: 2024-10-06 14:24:40

import json


def change_tuna_attribute_struct(all_img_json_path):
    with open(all_img_json_path, "r+") as file:
        data = json.load(file)

        for img in data["IMAGES"]:
            attributes = img["ATTRIBUTE"]

            # make one json for all attributes instead of several
            new_attributes = {}
            for attribute in attributes:
                if attribute["@NAME"] == "colour":
                    new_attributes["@COLOUR"] = attribute["@VALUE"]
                elif attribute["@NAME"] == "orientation":
                    new_attributes["@ORIENTATION"] = attribute["@VALUE"]
                elif attribute["@NAME"] == "type":
                    new_attributes["@TYPE"] = attribute["@VALUE"]
                elif attribute["@NAME"] == "size":
                    new_attributes["@SIZE"] = attribute["@VALUE"]
            # Replace the list of jsons with the new single json
            img["ATTRIBUTE"] = new_attributes
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()

    print("The file has been updated.")


if __name__ == "__main__":
    change_tuna_attribute_struct("tuna/imgs/all_imgs.json")
