import os

from box import ConfigBox
from box.exceptions import BoxValueError
import yaml
from ensure import ensure_annotations
import json
import joblib
from pathlib import Path
from typing import Any
import base64
from cnnClassifier import logger


@ensure_annotations
def read_yaml(filepath: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its contents as a ConfigBox object.

    Args:
        filepath (Path): Path to the YAML file.

    Returns:
        ConfigBox: Contents of the YAML file as a ConfigBox object.
    """
    try:
        with open(filepath, "r") as file:
            content = yaml.safe_load(file)
            logger.info(f"YAML file loaded successfully: {filepath}")
            return ConfigBox(content)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File not found: {filepath}") from e
    except yaml.YAMLError as e:
        raise ValueError(f"Error parsing YAML file: {filepath}") from e


@ensure_annotations
def create_directories(paths: list, verbose: bool = True):
    """
    Creates directories if they do not exist.

    Args:
        paths (list): List of directory paths to create.
        verbose (bool): If True, prints the created directories.
    """
    for path in paths:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created: {path}")


@ensure_annotations
def save_json(filepath: Path, data: dict):
    """
    Saves a dictionary to a JSON file.

    Args:
        filepath (Path): Path to the JSON file.
        data (dict): Dictionary to save.
    """
    with open(filepath, "w") as file:
        json.dump(data, file, indent=4)
        logger.info(f"JSON file saved successfully: {filepath}")


@ensure_annotations
def load_json(filepath: Path) -> ConfigBox:
    """
    Loads a dictionary from a JSON file.

    Args:
        filepath (Path): Path to the JSON file.

    Returns:
        ConfigBox: Contents of the JSON file as a ConfigBox object.
    """
    with open(filepath, "r") as file:
        data = json.load(file)
        logger.info(f"JSON file loaded successfully: {filepath}")
        return ConfigBox(data)


@ensure_annotations
def save_bin(filepath: Path, data: Any):
    """
    Saves data to a binary file using joblib.

    Args:
        filepath (Path): Path to the binary file.
        data (Any): Data to save.
    """
    joblib.dump(value=data, filename=filepath)
    logger.info(f"Binary file saved successfully: {filepath}")


@ensure_annotations
def load_bin(filepath: Path) -> Any:
    """
    Loads data from a binary file using joblib.

    Args:
        filepath (Path): Path to the binary file.

    Returns:
        Any: Data loaded from the binary file.
    """
    data = joblib.load(filepath)
    logger.info(f"Binary file loaded successfully: {filepath}")
    return data


@ensure_annotations
def get_size(filepath: Path) -> str:
    """
    Returns the size of a file in kilobytes.
    If the file does not exist, returns "0 KB".

    Args:
        filepath (Path): Path to the file.

    Returns:
        str: Size of the file in kilobytes, formatted as a string.
    """
    if not os.path.exists(filepath):
        return "0 KB"
    size_in_kb = round(os.path.getsize(filepath) / 1024)
    return f"~ {size_in_kb} KB"


def decode_image(image_str, filepath: Path) -> None:
    """
    Decodes a base64-encoded image string and saves it to a file.

    Args:
        image_str (str): Base64-encoded image string.
        filepath (Path): Path to save the decoded image.
    """
    try:
        image_data = base64.b64decode(image_str)
        with open(filepath, "wb") as file:
            file.write(image_data)
            logger.info(f"Image saved successfully: {filepath}")
    except Exception as e:
        logger.error(f"Error saving image: {e}")
        raise e


def encode_image_into_base64(cropped_image_path: Path) -> str:
    """
    Encodes an image file into a base64 string.

    Args:
        cropped_image_path (Path): Path to the image file.

    Returns:
        str: Base64-encoded string of the image.
    """
    try:
        with open(cropped_image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
            logger.info(f"Image encoded successfully: {cropped_image_path}")
            return encoded_string
    except Exception as e:
        logger.error(f"Error encoding image: {e}")
        raise e
