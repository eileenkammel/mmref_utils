# -*-coding:utf-8 -*-
# Author: Eileen Kammel, 811770
# Date: 2024-10-08 12:21:58

import json
import random
import itertools


def define_id(n):
    # Return all possible combinations of n attributes
    # by attribut list indices
    attribute_list = [0, 1, 2, 3, 4, 5]
    ids = itertools.combinations(attribute_list, n)
    return list(ids)


def extract_attributes(image):
    # Return a list of all attributes of an image
    return [
        image["ATTRIBUTE"]["floor_hue"],
        image["ATTRIBUTE"]["wall_hue"],
        image["ATTRIBUTE"]["object_hue"],
        image["ATTRIBUTE"]["scale"],
        image["ATTRIBUTE"]["shape"],
        image["ATTRIBUTE"]["orientation"],
    ]


def determine_id_style(id):
    id_style = {
        (0,): "floor_hue",
        (1,): "wall_hue",
        (2,): "object_hue",
        (3,): "scale",
        (4,): "shape",
        (5,): "orientation",
        (0, 1): "floor_hue_wall_hue",
        (0, 2): "floor_hue_object_hue",
        (0, 3): "floor_hue_scale",
        (0, 4): "floor_hue_shape",
        (0, 5): "floor_hue_orientation",
        (1, 2): "wall_hue_object_hue",
        (1, 3): "wall_hue_scale",
        (1, 4): "wall_hue_shape",
        (1, 5): "wall_hue_orientation",
        (2, 3): "object_hue_scale",
        (2, 4): "object_hue_shape",
        (2, 5): "object_hue_orientation",
        (3, 4): "scale_shape",
        (3, 5): "scale_orientation",
        (4, 5): "shape_orientation",
        (0, 1, 2): "floor_hue_wall_hue_object_hue",
        (0, 1, 3): "floor_hue_wall_hue_scale",
        (0, 1, 4): "floor_hue_wall_hue_shape",
        (0, 1, 5): "floor_hue_wall_hue_orientation",
        (0, 2, 3): "floor_hue_object_hue_scale",
        (0, 2, 4): "floor_hue_object_hue_shape",
        (0, 2, 5): "floor_hue_object_hue_orientation",
        (0, 3, 4): "floor_hue_scale_shape",
        (0, 3, 5): "floor_hue_scale_orientation",
        (0, 4, 5): "floor_hue_shape_orientation",
        (1, 2, 3): "wall_hue_object_hue_scale",
        (1, 2, 4): "wall_hue_object_hue_shape",
        (1, 2, 5): "wall_hue_object_hue_orientation",
        (1, 3, 4): "wall_hue_scale_shape",
        (1, 3, 5): "wall_hue_scale_orientation",
        (1, 4, 5): "wall_hue_shape_orientation",
        (2, 3, 4): "object_hue_scale_shape",
        (2, 3, 5): "object_hue_scale_orientation",
        (2, 4, 5): "object_hue_shape_orientation",
        (3, 4, 5): "scale_shape_orientation",
        (0, 1, 2, 3): "floor_hue_wall_hue_object_hue_scale",
        (0, 1, 2, 4): "floor_hue_wall_hue_object_hue_shape",
        (0, 1, 2, 5): "floor_hue_wall_hue_object_hue_orientation",
        (0, 1, 3, 4): "floor_hue_wall_hue_scale_shape",
        (0, 1, 3, 5): "floor_hue_wall_hue_scale_orientation",
        (0, 1, 4, 5): "floor_hue_wall_hue_shape_orientation",
        (0, 2, 3, 4): "floor_hue_object_hue_scale_shape",
        (0, 2, 3, 5): "floor_hue_object_hue_scale_orientation",
        (0, 2, 4, 5): "floor_hue_object_hue_shape_orientation",
        (0, 3, 4, 5): "floor_hue_scale_shape_orientation",
        (1, 2, 3, 4): "wall_hue_object_hue_scale_shape",
        (1, 2, 3, 5): "wall_hue_object_hue_scale_orientation",
        (1, 2, 4, 5): "wall_hue_object_hue_shape_orientation",
        (1, 3, 4, 5): "wall_hue_scale_shape_orientation",
        (2, 3, 4, 5): "object_hue_scale_shape_orientation",
        (0, 1, 2, 3, 4): "floor_hue_wall_hue_object_hue_scale_shape",
        (0, 1, 2, 3, 5): "floor_hue_wall_hue_object_hue_scale_orientation",
        (0, 1, 2, 4, 5): "floor_hue_wall_hue_object_hue_shape_orientation",
        (0, 1, 3, 4, 5): "floor_hue_wall_hue_scale_shape_orientation",
        (0, 2, 3, 4, 5): "floor_hue_object_hue_scale_shape_orientation",
        (1, 2, 3, 4, 5): "wall_hue_object_hue_scale_shape_orientation",
        (0, 1, 2, 3, 4, 5): "floor_hue_wall_hue_object_hue_scale_shape_orientation",
    }
    return id_style[id]


def find_distractors(target_attributes, target_id):
    # Return two distractors that fit the target_id
    all_img = json.load(open("3DS/3ds_subset.json", "r"))
    attribute_idx = set([0, 1, 2, 3, 4, 5])
    target_id = set(target_id)
    if len(target_id) == 1:
        possible_distractors = []
        # attributes that are not in the target_id by idx
        non_id_attributes = list(attribute_idx.difference(target_id))
        target_id = list(target_id)
        # index of the target attribute(s)
        a1_idx = target_id[0]
        # loop over all images and find distractors
        for image in all_img["IMAGES"]:
            image_filename = image["@FILENAME"]
            # get the attributes of the potential distractor
            image_attributes = extract_attributes(image)
            # skip img which have same attribute(s) as target id
            if image_attributes[a1_idx] == target_attributes[a1_idx]:
                continue
            # rest of the attributes must be the same
            else:
                if (
                    image_attributes[non_id_attributes[0]]
                    == target_attributes[non_id_attributes[0]]
                    and image_attributes[non_id_attributes[1]]
                    == target_attributes[non_id_attributes[1]]
                    and image_attributes[non_id_attributes[2]]
                    == target_attributes[non_id_attributes[2]]
                    and image_attributes[non_id_attributes[3]]
                    == target_attributes[non_id_attributes[3]]
                    and image_attributes[non_id_attributes[4]]
                    == target_attributes[non_id_attributes[4]]
                ):
                    possible_distractors.append(image_filename)
        try:
            possible_distractors = random.sample(possible_distractors, 2)
            return possible_distractors
        except ValueError:
            #print("No distractors found.")
            return None
    elif len(target_id) == 2:
        possible_distractors1 = []
        possible_distractors2 = []
        non_id_attributes = list(attribute_idx.difference(target_id))
        target_id = list(target_id)
        a1_idx = target_id[0]
        a2_idx = target_id[1]
        for image in all_img["IMAGES"]:
            image_filename = image["@FILENAME"]
            image_attributes = extract_attributes(image)
            if (
                image_attributes[a1_idx] == target_attributes[a1_idx]
                and image_attributes[a2_idx] == target_attributes[a2_idx]
            ):
                continue
            else:
                # find first distractor candidates
                if (
                    image_attributes[a1_idx] == target_attributes[a1_idx]
                    and image_attributes[a2_idx] != target_attributes[a2_idx]
                    and image_attributes[non_id_attributes[0]]
                    == target_attributes[non_id_attributes[0]]
                    and image_attributes[non_id_attributes[1]]
                    == target_attributes[non_id_attributes[1]]
                    and image_attributes[non_id_attributes[2]]
                    == target_attributes[non_id_attributes[2]]
                    and image_attributes[non_id_attributes[3]]
                    == target_attributes[non_id_attributes[3]]
                ):
                    possible_distractors1.append(image_filename)

                # find second distractor candidates

                if (
                    image_attributes[a1_idx] != target_attributes[a1_idx]
                    and image_attributes[a2_idx] == target_attributes[a2_idx]
                    and image_attributes[non_id_attributes[0]]
                    == target_attributes[non_id_attributes[0]]
                    and image_attributes[non_id_attributes[1]]
                    == target_attributes[non_id_attributes[1]]
                    and image_attributes[non_id_attributes[2]]
                    == target_attributes[non_id_attributes[2]]
                    and image_attributes[non_id_attributes[3]]
                    == target_attributes[non_id_attributes[3]]
                ):
                    possible_distractors2.append(image_filename)
        # return one random distractor from each list if they exist, else skip
        try:
            possible_distractors1 = random.sample(possible_distractors1, 1)
            possible_distractors2 = random.sample(possible_distractors2, 1)
            distractors = possible_distractors1 + possible_distractors2
            return distractors if len(distractors) == 2 else None
        except ValueError:
            #print("Not enough distractors found.")
            return None


def make_stimuli_sets():

    json_instances = {"INSTANCES": []}

    episode_num = 0.0

    # loop over 3DS/3ds_subset.json, image will be target
    all_img = json.load(open("3DS/3ds_subset.json", "r"))

    # pick 100 random targets, to speed up the process
    random.shuffle(all_img["IMAGES"])
    all_img["IMAGES"] = all_img["IMAGES"][:100]

    for img in all_img["IMAGES"]:
        target_filename = img["@FILENAME"]
        target_attributes = extract_attributes(img)
        # loop over all possible ids
        for i in range(1, 3):
            ids = define_id(i)
            for id in ids:
                distractors = find_distractors(target_attributes, id)
                if distractors is not None:
                    episode = {
                        "@ID": episode_num,
                        "@TARGET": target_filename,
                        "ID_STYLE": determine_id_style(id),
                        "Distractor1": distractors[0],
                        "Distractor2": distractors[1],
                    }
                    json_instances["INSTANCES"].append(episode)

                    episode_num += 1
        if episode_num % 10 == 0:
            print(f"Processed {episode_num} episodes")

    with open("3DS/3ds_instances.json", "w") as json_file:
        json.dump(json_instances, json_file, indent=4)
    print("All instances saved successfully!")


if __name__ == "__main__":
    make_stimuli_sets()
