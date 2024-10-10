# -*-coding:utf-8 -*-
# Author: Eileen Kammel, 811770
# Date: 2024-10-10 14:28:11

import os
import json
import shutil

# determine which images have been used for the stiumuli and
# copy them to new directory

# read json file
with open("3DS/3ds_instances.json", "r") as f:
    data = json.load(f)

path = "3DS/stimuli_images"
if not os.path.exists(path):
    os.makedirs(path)

for stimuli in data["INSTANCES"]["one_attibute_id"]:
    images = [
        stimuli["target"],
        stimuli["distractor1"],
        stimuli["distractor2"]
    ]
    for image in images:
        image_path = os.path.join("3DS/", image)
        if not os.path.exists(os.path.join(path, image)):
            shutil.copy(image_path, os.path.join(path, image))