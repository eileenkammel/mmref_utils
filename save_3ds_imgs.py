# -*-coding:utf-8 -*-
# Author: Eileen Kammel, 811770
# Date: 2024-09-24 12:55:26

import os
import pickle as pkl
import json
from PIL import Image


# Basic json object structure. Add new json
# for each image to list

# {
#     "IMAGES": [{
#         "@ID": 1,
#         "@FILENAME": 1,
#         "ATTRIBUTES": {
#             "floor_hue": 1,
#             "wall_hue": 1,
#             "object_hue": 1,
#             "scale": 1,
#             "shape": 1,
#             "orientation": 1,
#         },
#     }]
# }

# Load the dataset by unpickeling

images, labels = pkl.load(open("3DS/3ds_subset.pkl", "rb"))

# Save images as png (jpg has to much loss, I tried it) and make
# corresponding json that saves filename and attributes
# for each image

data_set = zip(images, labels)

json_data = {"IMAGES": []}

for i, (image, label) in enumerate(data_set):
    filename = f"{i}.png"
    json_data["IMAGES"].append(
        {
            "@ID": i,
            "@FILENAME": filename,
            "ATTRIBUTES": {
                "floor_hue": label[0],
                "wall_hue": label[1],
                "object_hue": label[2],
                "scale": label[3],
                "shape": label[4],
                "orientation": label[5],
            },
        }
    )
    img = Image.fromarray(image.astype("uint8"), "RGB")
    image_path = os.path.join("3DS/", filename)
    img.save(image_path)

with open("3DS/3ds_subset.json", "w") as f:
    json.dump(json_data, f, indent=4)
