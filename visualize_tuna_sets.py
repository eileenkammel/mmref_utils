# -*-coding:utf-8 -*-
# Author: Eileen Kammel, 811770
# Date: 2024-09-06 15:51:03

# Make CSV and HTML tables from TUNA corpus to get
# an overview of the data.

import os
import json
import csv
from bs4 import BeautifulSoup
import pandas as pd


def extract_relevant_info(input_dir, output_name):
    # Prepare the CSV columns
    # TRIAL_ID = ID of Trial/filename
    # T = Target,
    # D1-D6 = Distractors,
    # Description = expression for target

    csv_header = ["TRIAL_ID", "T", "D1", "D2",
                  "D3", "D4", "D5", "D6", "Description"
                  ]
    csv_data = []

    for filename in os.listdir(input_dir):
        if filename.endswith(".json"):
            file_path = os.path.join(input_dir, filename)

            with open(file_path, "r") as file:
                data = json.load(file)

            trial_id = data["TRIAL"]["@ID"]
            description = data["TRIAL"]["STRING-DESCRIPTION"]
            target_image = None
            distractor_images = []

            entities = data["TRIAL"]["DOMAIN"]["ENTITY"]
            for entity in entities:
                if entity["@TYPE"] == "target":
                    target_image = entity["@IMAGE"]
                elif entity["@TYPE"] == "distractor":
                    distractor_images.append(entity["@IMAGE"])
        csv_data.append(
            [trial_id] + [target_image] + distractor_images[:6] + [description]
        )

    with open(output_name, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(csv_header)
        writer.writerows(csv_data)

    return output_name


# Visualize the data in a HTML table, text only


def create_html(csv_path, output_name):
    tuna_df = pd.read_csv(csv_path)
    tuna_html = tuna_df.to_html(index=False)

    with open(output_name, "w") as file:
        file.write(tuna_html)
    print(f"HTML table generated: {output_name}")
    return output_name


# Make another html table, this time with images from file names


def create_html_images(text_html, image_path, output_name):
    with open(text_html, "r") as f:
        soup = BeautifulSoup(f, "html.parser")

    table = soup.find("table")
    for cell in table.find_all("td"):

        filename = cell.get_text().strip()
        if filename:
            img_tag = soup.new_tag("img")
            img_tag["src"] = os.path.join(image_path, filename)
            img_tag["alt"] = filename

            cell.clear()
            cell.append(img_tag)

    with open(output_name, "w") as f:
        f.write(str(soup))
    print(f"HTML table with images generated: {output_name}")


if __name__ == "__main__":
    directory = "tuna"
    output_csv_name = "tuna.csv"
    output_html_name = "tuna.html"
    output_html_images = "tuna_images.html"
    tuna_images = "tuna_original/dist/images/furniture"
    tuna_csv = extract_relevant_info(directory, output_csv_name)
    tuna_html = create_html(tuna_csv, output_html_name)
    create_html_images(tuna_html, tuna_images, output_html_images)
