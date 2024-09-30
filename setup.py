import io
import os

from setuptools import find_packages, setup

# Package meta-data.
NAME = "githooks"
DESCRIPTION = "Git hooks for Python projects."
URL = "https://github.com/huangsam/githooks"
EMAIL = "samhuang91@gmail.com"
AUTHOR = "Sam Huang"
REQUIRES_PYTHON = ">=3.0.0"
VERSION = None

# What packages are required for this module to be executed?
REQUIRED = ["flake8", "gitpython"]
SETUP_REQUIRED = ["pytest-runner"]
TEST_REQUIRED = ["pytest"]

# What packages are optional?
EXTRAS = {}

# Current directory of the setup.py script
here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
        long_description = "\n" + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    with open(os.path.join(here, NAME, "__version__.py")) as f:
        exec(f.read(), about)
else:
    about["__version__"] = VERSION

# Where the magic happens:
setup(
    name=NAME,
    version=about["__version__"],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=("tests",)),
    install_requires=REQUIRED,
    setup_requires=SETUP_REQUIRED,
    tests_require=TEST_REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.12",
    ],
)
