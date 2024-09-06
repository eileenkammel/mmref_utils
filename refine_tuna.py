# -*-coding:utf-8 -*-
# Author: Eileen Kammel, 811770
# Date: 2024-09-06 15:30:04

# As location plays no role in referencegame, all episodes with +LOC condition
# are removed. Descriptions have location in them so they dont serve my purpose.
# Currently removes files from furniture folder in sg condition only.

# Parse all episodes in corpus folder und remove
# those with +LOC condition

import os
import xml.etree.ElementTree as ET


def rm_loc():
    directory = "tuna/dist/corpus/singular/furniture"

    for filename in os.listdir(directory):
        if filename.endswith(".xml"):  # Only process XML files, not .dtd
            file_path = os.path.join(directory, filename)
            try:
                tree = ET.parse(file_path)
                root = tree.getroot()
                if root.attrib.get("CONDITION") == "+LOC":
                    os.remove(file_path)
                    print(f"Removed file: {filename}")
                else:
                    print(f"File {filename} does not match CONDITION='+LOC'.")
            except ET.ParseError:
                print(f"Failed to parse XML file: {filename}")

    print("Finished removing files with +LOC condition.")


if __name__ == "__main__":
    rm_loc()