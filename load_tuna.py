# -*-coding:utf-8 -*-
# Author: Eileen Kammel, 811770
# Date: 2024-09-06 13:18:29

# Download and unzip TUNA corpus
import os
import zipfile
import requests


def download_tuna():
    url = "http://www.abdn.ac.uk/ncs/documents/corpus.zip"
    tuna = requests.get(url)
    tuna.raise_for_status()
    with open("corpus.zip", "wb") as f:
        f.write(tuna.content)
    with zipfile.ZipFile("corpus.zip", "r") as zip_ref:
        zip_ref.extractall("tuna_original")
    os.remove("corpus.zip")
    print("TUNA corpus downloaded and unzipped.")


if __name__ == "__main__":
    # Check if not already downloaded
    if not os.path.exists("tuna_original"):
        download_tuna()
    else:
        print("TUNA corpus already downloaded.")