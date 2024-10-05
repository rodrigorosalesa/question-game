import json


def read_questions(json_file: str) -> dict:
    """
    Read the questions from the json file and return them as a dictionary.

    Args:
        json_file (str): The path to the json file.

    Returns:
        data (dict): The questions as a dictionary
    """
    with open(json_file) as f:
        data = json.load(f)
    return data