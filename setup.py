from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = " -e ."
def get_requirements(file_path: str) -> List[str]:
    """
    Get requirements from requirements.txt file.
    """

    with open(file_path, "r") as file:
        requirements = file.readlines()
        requirements = [r.replace("/n", "") for r in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name = "first_end_to_end_project",
    version = "0.0.1",
    author = "Kaushal Jain",
    author_email = "kaushaljain7000@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt'),

)