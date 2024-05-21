import setuptools # type: ignore

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ ="0.0.0"

REPO_NAME = "NLP_Text_Summarizer"
AUTHOR_USER_NAME = "Arcotsaikiran"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "arcotsaikiran1611@gmail.com"


setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text Summarizer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Arcotsaikiran/NLP_Text_Summarizer",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",

    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)
    

