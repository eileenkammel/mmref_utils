# -*-coding:utf-8 -*-
# Author: Eileen Kammel, 811770
# Date: 2024-09-10 13:05:35


import os
import json
import csv

# Search for target and distractor images in JSON files to get impression of
# data and if every image is used as taget and distractor the like.
# Write to two CSV files for further analysis.


def identify_imgs(input_dir, output_name_targets, output_name_distractors):
    csv_header = ["episode_id", "img_id", "filenname", "description"]
    csv_header_distractors = ["episode_id", "img_id", "filename"]
    csv_data = []
    csv_data_distractors = []
    episode_id = ""
    img_id = ""
    img_filename = ""
    description = ""
    img_id_distractor = ""
    img_filename_distractor = ""

    for filename in os.listdir(input_dir):
        if filename.endswith(".json"):
            file_path = os.path.join(input_dir, filename)
            with open(file_path, "r") as json_file:
                try:
                    data = json.load(json_file)
                    episode_id = data["TRIAL"]["@ID"]
                    for entity in data["TRIAL"]["DOMAIN"]["ENTITY"]:
                        if entity["@TYPE"] == "target":
                            img_id = entity["@ID"]
                            img_filename = entity["@IMAGE"]
                            description = data["TRIAL"]["STRING-DESCRIPTION"]
                            csv_data.append(
                                [episode_id] + [img_id]
                                + [img_filename] + [description]
                            )
                        else:
                            img_id_distractor = entity["@ID"]
                            img_filename_distractor = entity["@IMAGE"]
                            csv_data_distractors.append(
                                [episode_id]
                                + [img_id_distractor]
                                + [img_filename_distractor]
                            )
                except json.JSONDecodeError:
                    print(f"Error reading {filename}, skipping file.")
    with open(output_name_targets, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(csv_header)
        writer.writerows(csv_data)
    with open(output_name_distractors, "w", newline="") as csv_file2:
        writer = csv.writer(csv_file2)
        writer.writerow(csv_header_distractors)
        writer.writerows(csv_data_distractors)
    print(f"CSVs generated: {output_name} & {output_name_distractors}")


if __name__ == "__main__":
    input_dir = "/Users/eileen/B.Sc. Thesis/repos/mmref_utils/tuna"
    output_name = "tuna_target_imgs.csv"
    output_name_distractors = "tuna_distractor_imgs.csv"
    identify_imgs(input_dir, output_name, output_name_distractors)
