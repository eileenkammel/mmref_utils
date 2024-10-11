# -*-coding:utf-8 -*-
# Author: Eileen Kammel, 811770
# Date: 2024-10-11 13:25:14

import os
import json
import shutil

# Create a directory for the test sets
path = "test_sets"
if not os.path.exists(path):
    os.makedirs(path)

three_ds_path = "test_sets/3DS"
if not os.path.exists(three_ds_path):
    os.makedirs(three_ds_path)

tuna_path = "test_sets/tuna"
if not os.path.exists(tuna_path):
    os.makedirs(tuna_path)


# 3DS

# read json file
with open("3DS/3ds_instances.json", "r") as f:
    data = json.load(f)

# pick 3 instances
instances = data["INSTANCES"]["one_attibute_id"][:3]
# make new insrtances json

new_data = {"INSTANCES": {"one_attibute_id": instances}}
new_data_path = os.path.join(three_ds_path, "3ds_instances.json")
with open(new_data_path, "w") as f:
    json.dump(new_data, f, indent=4)

# copy images
for stimuli in instances:
    images = [
        stimuli["target"],
        stimuli["distractor1"],
        stimuli["distractor2"]
    ]
    for image in images:
        image_path = os.path.join("3DS", image)
        if not os.path.exists(os.path.join(three_ds_path, image)):
            shutil.copy(image_path, os.path.join(three_ds_path, image))


# TUNA

# read json file
with open("tuna/instances.json", "r") as f:
    data = json.load(f)
# pick 3 instances
instances = data["INSTANCES"]["one_attibute_id"][:3]
# make new insrtances json
new_data = {"INSTANCES": {"one_attibute_id": instances}}
new_data_path = os.path.join(tuna_path, "instances.json")
with open(new_data_path, "w") as f:
    json.dump(new_data, f, indent=4)

# copy images
for stimuli in instances:
    images = [
        stimuli["target"],
        stimuli["distractor1"],
        stimuli["distractor2"]
    ]
    for image in images:
        image_path = os.path.join("tuna/imgs", image)
        if not os.path.exists(os.path.join(tuna_path, image)):
            shutil.copy(image_path, os.path.join(tuna_path, image))
