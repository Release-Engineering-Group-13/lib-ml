# lib-ml
Package for preprocessing ML data

## Installation
Run the following in a terminal (you might need a virtual environment). Replace the VERSION_TAG at the end with a version, preferably the most recent (v1.0.0)
```bash
pip install git+https://github.com/Release-Engineering-Group-13/lib-ml.git@VERSION_TAG
```

## Usage
Functionality can be used by importing lib_ml.

To preprocess an entire dataset, you can call:
```
preprocess_dataset(dataset_folder = "data/raw/DL Dataset/", train_file="train.txt", test_file="test.txt", val_file="val.txt", output_folder = "data/interim"):
```
This will get the data from the specified input folder and files and output the result in the output_folder

To preprocess a single input, you can call:
```
preprocess_input(input)
```
This will simply return the result as char_index, tokenized_x