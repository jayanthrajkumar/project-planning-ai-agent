"""
Utility functions for loading YAML configurations.
"""

import yaml


def load_yaml(file_path):
    """
    Load YAML file and return dictionary.
    """
    with open(file_path, "r") as file:
        return yaml.safe_load(file)