from setuptools import setup, find_packages
from typing import List

# Variable Declarationfor setup function
PROJECT_NAME = "News-Summarization-HuggingFace"
VERSION = "0.0.1"
AUTHOR = "Jobin Mathew"
DESCRIPTION = 'iNeuron Internship project based on Kaggle Dataset to Summarize News Articles'

REQUIREMENTS_FILE_NAME = "requirements.txt"

HYPHEN_E_DOT = "-e ."

def get_requirements_list()-> List[str]:
    """
    Function Name: get_requirements_list
    Description: This function returns list of requirements mentioned 
    in requirements.txt file

    returns List[str]
    """
    with open(REQUIREMENTS_FILE_NAME, encoding="latin-1") as requirements_file:
        requirements_list = requirements_file.readlines()
        requirements_list = [requirement_name.replace("\n", "") for requirement_name in requirements_list]

        if HYPHEN_E_DOT in requirements_list:
            requirements_list.remove(HYPHEN_E_DOT)

        return requirements_list

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=get_requirements_list()
)