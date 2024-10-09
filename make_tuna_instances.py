# -*-coding:utf-8 -*-
# Author: Eileen Kammel, 811770
# Date: 2024-10-02 15:44:36


import json
import random
import itertools


def define_id(n):
    # Return all possible combinations of n attributes
    # by attribut list indices
    attribute_list = [0, 1, 2, 3]
    ids = itertools.combinations(attribute_list, n)
    return list(ids)


def extract_attributes(image):
    # Return a list of all attributes of an image
    return [
        image["ATTRIBUTE"]["@COLOUR"],
        image["ATTRIBUTE"]["@ORIENTATION"],
        image["ATTRIBUTE"]["@TYPE"],
        image["ATTRIBUTE"]["@SIZE"],
    ]


def determine_id_style(id):
    id_style = {
        (0,): "colour",
        (1,): "orientation",
        (2,): "type",
        (3,): "size",
        (0, 1): "colour_orientation",
        (0, 2): "colour_type",
        (0, 3): "colour_size",
        (1, 2): "orientation_type",
        (1, 3): "orientation_size",
        (2, 3): "type_size",
        (0, 1, 2): "colour_orientation_type",
        (0, 1, 3): "colour_orientation_size",
        (0, 2, 3): "colour_type_size",
        (1, 2, 3): "orientation_type_size",
    }
    return id_style[id]


def find_distractors(target_attributes, target_id):
    # Return two distractors that fit the target_id
    all_img = json.load(open("tuna/imgs/all_imgs.json", "r"))
    attribute_idx = set([0, 1, 2, 3])
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
            image_filename = image["@IMAGE"]
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
                ):
                    possible_distractors.append(image_filename)
        # return two random distractors if they exist, else skip
        try:
            possible_distractors = random.sample(possible_distractors, 2)
            return possible_distractors
        except ValueError:
            print("Not enough distractors found!")
            return None

    elif len(target_id) == 2:
        possible_distractors1 = []
        possible_distractors2 = []
        # attributes that are not in the target_id by idx
        non_id_attributes = list(attribute_idx.difference(target_id))
        target_id = list(target_id)
        # index of the target attribute(s)
        a1_idx = target_id[0]
        a2_idx = target_id[1]
        # loop over all images and find distractors
        for image in all_img["IMAGES"]:
            image_filename = image["@IMAGE"]
            image_attributes = extract_attributes(image)
            # skip img which have same attribute(s) as target id
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
                ):
                    possible_distractors1.append(image_filename)
                # find second distractor candidates
                elif (
                    image_attributes[a1_idx] != target_attributes[a1_idx]
                    and image_attributes[a2_idx] == target_attributes[a2_idx]
                    and image_attributes[non_id_attributes[0]]
                    == target_attributes[non_id_attributes[0]]
                    and image_attributes[non_id_attributes[1]]
                    == target_attributes[non_id_attributes[1]]
                ):
                    possible_distractors2.append(image_filename)
        # return one random distractor from each list if they exist, else skip
        try:
            possible_distractors1 = random.sample(possible_distractors1, 1)
            possible_distractors2 = random.sample(possible_distractors2, 1)
            distractors = possible_distractors1 + possible_distractors2
            return distractors if len(distractors) == 2 else None
        except ValueError:
            print("Not enough distractors found!")
            return None
    # not possible with only 2 distractors
    # elif len(target_id) == 3:
    #     a1_idx = target_id[0]
    #     a2_idx = target_id[1]
    #     a3_idx = target_id[2]
    # return two random distractors


def make_stimuli_sets():

    json_instances = {"INSTANCES": []}

    episode_num = 0.0

    # loop over all_img.json, image will be target
    all_img = json.load(open("tuna/imgs/all_imgs.json", "r"))

    for img in all_img["IMAGES"]:
        t_filename = img["@IMAGE"]
        # get the target attributes
        all_attributes = extract_attributes(img)

        # find ids for target with all
        # possible lengths & combinations of attributes (1-3)
        for i in range(1, 3):
            # find all possible ids
            ids = define_id(i)
            # get distractors for all ids
            for id in ids:
                distractors = find_distractors(all_attributes, id)
                if distractors is not None:
                    distractor1 = distractors[0]
                    distractor2 = distractors[1]
                    episode = {
                        "@EPISODE": episode_num,
                        "TARGET": t_filename,
                        "Distractor1": distractor1,
                        "Distractor2": distractor2,
                        "ID": determine_id_style(id),
                    }

                    json_instances["INSTANCES"].append(episode)

                    episode_num += 1

    with open("tuna/instances.json", "w") as json_file:
        json.dump(json_instances, json_file, indent=4)
    print("All instances saved successfully!")


if __name__ == "__main__":
    make_stimuli_sets()
