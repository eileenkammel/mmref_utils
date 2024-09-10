import xmltodict
import json
import os

# Function to convert XML to JSON
def xml_to_json(xml_string):
    # Parse XML to a Python dictionary
    xml_dict = xmltodict.parse(xml_string)

    # Convert the dictionary to a JSON string
    json_string = json.dumps(xml_dict, indent=3)

    return json_string


# Conveert all episodes in the furniture category to JSON

def convert_all_furniture(directory):
    path = "tuna/"
    if not os.path.exists(path):
        os.makedirs(path)

    for filename in os.listdir(directory):
        if filename.endswith(".xml"):
            file_path = os.path.join(directory, filename)
            with open(file_path, "r") as xml_file:
                xml_data = xml_file.read()

            json_data = xml_to_json(xml_data)
            output_name = filename[:-4]+(".json")
            with open("tuna/" + output_name, "w") as json_file:
                json_file.write(json_data)

    print("All XML converted to JSON successfully!")


if __name__ == "__main__":
    directory = "tuna_original/dist/corpus/singular/furniture"
    convert_all_furniture(directory)