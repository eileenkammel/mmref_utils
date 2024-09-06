# -*-coding:utf-8 -*-
# Author: Eileen Kammel, 811770
# Date: 2024-09-06 15:51:03

# Because XML files are not easily human-readable,
# this script visualizes the TUNA stimuli in a html table.

import os

import xml.etree.ElementTree as ET
import csv
import pandas as pd
from bs4 import BeautifulSoup


def extract_relevant_info(input_file, output_name):
    # Prepare the CSV columns
    # T = Target, D1-D6 = Distractors, Description = expression for target
    csv_headers = ["T", "D1", "D2", "D3", "D4", "D5", "D6", "Description"]
    csv_data = []

    # Iterate over all XML files in the directory
    for filename in os.listdir(input_file):
        if filename.endswith(".xml"):  # Process only XML files, not .dtd
            file_path = os.path.join(input_file, filename)

            # Parse the XML file
            try:
                tree = ET.parse(file_path)
                root = tree.getroot()

                # Initialize data for the current row
                target_filename = None
                distractor_filenames = []
                description = ""

                # Extract target and distractors
                for entity in root.findall(".//ENTITY"):
                    entity_type = entity.attrib.get("TYPE")
                    file_name = entity.attrib.get("IMAGE")

                    if entity_type == "target":
                        target_filename = file_name
                    elif entity_type == "distractor":
                        distractor_filenames.append(file_name)

                # Extract STRING-DESCRIPTION (if available)
                description_tag = root.find(".//STRING-DESCRIPTION")
                if description_tag is not None:
                    description = description_tag.text
                    description = description.strip()

                # Ensure we have 6 distractors, pad if fewer
                distractor_filenames.extend([""] * (6 - len(distractor_filenames)))

                # Add the data to the CSV row
                csv_data.append([target_filename] + distractor_filenames[:6] + [description])

            except ET.ParseError:
                print(f"Failed to parse XML file: {filename}")

    # Write the extracted data to a CSV file
    with open(output_name, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(csv_headers)
        writer.writerows(csv_data)
    print(f"CSV generated: {output_name}")
    return output_name

# Visualize the data in a HTML table, text only


def create_html(csv_path, output_name):
    tuna_df = pd.read_csv(csv_path)
    tuna_html = tuna_df.to_html(index=False)
    # Save the HTML table to a file
    with open(output_name, "w") as file:
        file.write(tuna_html)
    print(f"HTML table generated: {output_name}")
    return output_name

# Make another html table, this time with images from file names


def create_html_images(text_html, image_path, output_name):
    with open(text_html, "r") as f:
        soup = BeautifulSoup(f, "html.parser")

    # Find the table in the HTML
    table = soup.find("table")
    for cell in table.find_all("td"):
        # Extract the filename from the cell
        filename = cell.get_text().strip()
        if filename:
            # Create a new tag for the image
            img_tag = soup.new_tag("img")
            img_tag["src"] = os.path.join(image_path, filename)
            img_tag["alt"] = filename
            # Replace the text cell with the image tag
            cell.clear()
            cell.append(img_tag)

    # Save the modified HTML table
    with open(output_name, "w") as f:
        f.write(str(soup))
    print(f"HTML table with images generated: {output_name}")


if __name__ == "__main__":
    directory = 'tuna/dist/corpus/singular/furniture'
    output_csv_name = "tuna.csv"
    output_html_name = "tuna.html"
    output_html_images = "tuna_images.html"
    tuna_images = "tuna/dist/images/furniture"
    tuna_csv = extract_relevant_info(directory, output_csv_name)
    tuna_html = create_html(tuna_csv, output_html_name)
    create_html_images(tuna_html, tuna_images, output_html_images)
