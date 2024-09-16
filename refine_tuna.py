# -*-coding:utf-8 -*-
# Author: Eileen Kammel, 811770
# Date: 2024-09-06 15:30:04

# As location plays no role in referencegame, all episodes with +LOC condition
# are removed. Descriptions have location in them so they dont serve my.
# purpose. Currently removes files from furniture folder in sg condition only.

# Parse all episodes in corpus folder und remove
# those with +LOC condition and META-ATTRIBUTE in description.
# (META-ATTRIBUTE contains the location if mentioned in the description
# in the -LOC condition)


import os
import json


def rm_loc(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            file_path = os.path.join(directory, filename)

            with open(file_path, 'r') as json_file:
                try:
                    data = json.load(json_file)

                    if data["TRIAL"]["@CONDITION"] == "+LOC":
                        os.remove(file_path)
                        print(f"Removed file: {filename}")
                    elif "META-ATTRIBUTE" in data["TRIAL"]["DESCRIPTION"]:
                        os.remove(file_path)
                        print(f"Removed file: {filename}")

                except json.JSONDecodeError:

                    print(f"Error reading {filename}, skipping file.")
    print("All files with +LOC condition and META-ATTRIBUTE removed.")


if __name__ == "__main__":
    directory = "tuna"
    rm_loc(directory)
