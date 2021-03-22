# FigureQA-synthetic-dataset-creation
Python script to run on FigureQA dataset in order to synthetically create dataset for Visuo-Linguistic tasks

Used the figureqa-train1-v1.tar.gz(2.12 GB) from the following link:
https://msropendata.com/datasets/85596452-0fe3-4335-bc00-ae83ee8ffcfd

The data.json has entries whose format is as below:

Entry_{I} is just the entry under which rest of the attributes fall. Image_index is the name of the image from the mentioned dataset
Graph_type is one of the five graph types used in FigureQA dataset
Passage: It is the generated passage according the image
Question: It asks about the added entity
Answer: Provides the true answer in a sentence form. It can be changed to just numeric form.

There are no special packages required to run the code. The code was written in python 3. Simply run the file from the terminal. Only the annotations file of the original dataset is required to be in the same directory.
