import os
import setuptools

def get_requirements(filepath: str) -> list[str]:
    """
    Returns a list of requirements from the given file.
    """
    if not os.path.exists(filepath):
        return []
    with open(filepath, "r") as file:
        requirements = file.read().splitlines()
    if "-e ." in requirements:
        requirements.remove("-e .")
    return requirements

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.1.0"

AUTHOR_NAME = "Sujeet Gund"
AUTHOR_USERNAME = "sujeetgund"
AUTHOR_EMAIL = "sujeetgund@gmail.com"

REPO_NAME = "kidney-disease-classification"
SRC_REPO_NAME = "cnnClassifier"


setuptools.setup(
    name=SRC_REPO_NAME,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small package for kidney disease classification",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}",
    project_urls={
        "Issues": f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=get_requirements("requirements.txt"),
)
