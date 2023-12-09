from setuptools import find_packages,setup
from typing import List
Hyphien_e_dot = '-e .'

def get_requirement(file_path:str)->List[str]:

    requirement = []
    with open (file_path) as file_obj:
        requirement = file_obj.readlines()
        requirement = [req.replace ("\n","")for req in requirement]
        if Hyphien_e_dot in requirement:
            requirement.remove(Hyphien_e_dot)
    return requirement

setup(
    name='mlproject',
    version='0.0.1',
    author='sarib',
    author_email='mstrsarib@gmail.com',
    packages=find_packages(),
    install_requires=get_requirement('requirement.txt')
)
   

    
