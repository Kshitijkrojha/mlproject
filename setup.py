from setuptools import setup, find_packages
from typing import List
HYPEN_E_DOT='-e .'
def get_requirements(file_path: str) ->List[str]:
    """Read the requirements file and return the list of requirements."""
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    packages=find_packages(), ## this will automatically call all the _init_.py files in the subdirectories
    author='kshitij',
    author_email='arhivamth11@gmail.com',
    install_requires=get_requirements('requirements.txt'),
)