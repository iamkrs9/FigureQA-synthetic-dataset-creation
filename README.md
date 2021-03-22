# FigureQA-synthetic-dataset-creation
Python script to run on FigureQA dataset in order to synthetically create dataset for Visuo-Linguistic tasks

Used the figureqa-train1-v1.tar.gz(2.12 GB) from the following link:
https://msropendata.com/datasets/85596452-0fe3-4335-bc00-ae83ee8ffcfd

The data.json has entries whose format is as below:

1) Entry_{I} is just the entry under which rest of the attributes fall. Image_index is the name of the image from the mentioned dataset
2) Graph_type is one of the five graph types used in FigureQA dataset
3) Passage: It is the generated passage according the image
4) Question: It asks about the added entity
5) Answer: Provides the true answer in a sentence form. It can be changed to just numeric form.

There are no special packages required to run the code. The code was written in python 3. Simply run the file from the terminal. Only the annotations file of the original dataset is required to be in the same directory.
