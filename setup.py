from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="lib_ml",
    description="URL Phishing data preprocessing library",
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Release-Engineering-Group-13/lib-ml",
    author="Maarten van Bijsterveldt",
    author_email="M.P.vanBijsterveldt@student.tudelft.nl",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'joblib',
        'tensorflow',
        'scikit-learn',
        'sklearn-preprocessing',
    ],
    python_requires=">=3.10",
)