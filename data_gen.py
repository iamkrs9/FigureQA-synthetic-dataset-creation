import json
import random

with open('annotations.json') as json_file:
    data = json.load(json_file)

with open('variable_names.txt') as vnames:
    list_color = json.load(vnames)
list_color_toadd = ['Royal Green', 'Crimson Red', 'Oceanic Blue', 'Black', 'White', 'Magenta', 'Yellow', 'Baby Pink']


def data_gen(num):
    dict_json = {}
    for i in range(num):
        current = random.choice(data)
        data.remove(current)

        if current['type'] == 'pie':
            added = random.choice(list_color_toadd)
            random_choice = random.choice(range(len(current['models'])))
            selected = current['models'][random_choice]['name']
            dict_json['Entry_{}'.format(i)] = []
            dict_json['Entry_{}'.format(i)].append("dataset_id: figureqa-train1-v1")
            dict_json['Entry_{}'.format(i)].append("Image_index: {}".format(current['image_index']))
            dict_json['Entry_{}'.format(i)].append("Graph_type: {}".format(current['type']))
            dict_json['Entry_{}'.format(i)].append("Passage: There is a new entity {} such that it is half that of {}"
                                                   .format(added, selected))
            dict_json['Entry_{}'.format(i)].append("Question: What would be {}'s size in % of the whole pie".format(added))
            answer_pie = (((current['models'][random_choice]['end'] - current['models'][random_choice]['start'])/2)*100)/6.28
            dict_json['Entry_{}'.format(i)].append("Answer: It would be {} % of the whole pie".format(answer_pie))

        if current['type'] == 'line':
            added = random.choice(list_color_toadd)
            random_choice = random.choice(range(len(current['models'])))
            selected = current['models'][random_choice]['name']
            dict_json['Entry_{}'.format(i)] = []
            dict_json['Entry_{}'.format(i)].append("dataset_id: figureqa-train1-v1")
            dict_json['Entry_{}'.format(i)].append("Image_index: {}".format(current['image_index']))
            dict_json['Entry_{}'.format(i)].append("Graph_type: {}".format(current['type']))
            dict_json['Entry_{}'.format(i)].append("Passage: A new line about {} follows the trend of {} exactly the "
                                                   "same".format(added, selected))
            y_value = current['models'][random_choice]['y'][-1]
            dict_json['Entry_{}'.format(i)].append("Question: What would be {}'s x-value at y = {}?".format(added, y_value))
            answer_line = current['models'][random_choice]['x'][-1]
            dict_json['Entry_{}'.format(i)].append("Answer: It would be {}".format(answer_line))

        if current['type'] == 'dot_line':
            added = random.choice(list_color_toadd)
            random_choice = random.choice(range(len(current['models'])))
            selected = current['models'][random_choice]['name']
            dict_json['Entry_{}'.format(i)] = []
            dict_json['Entry_{}'.format(i)].append("dataset_id: figureqa-train1-v1")
            dict_json['Entry_{}'.format(i)].append("Image_index: {}".format(current['image_index']))
            dict_json['Entry_{}'.format(i)].append("Graph_type: {}".format(current['type']))
            dict_json['Entry_{}'.format(i)].append("Passage: There is new entity {} such that its x-axis points are "
                                                   "shifted by 2 units to the right compared to x-axis points of {}".format(added, selected))
            random_choice_y = random.choice(range(len(current['models'][random_choice]['y'])))
            y_value = current['models'][random_choice]['y'][random_choice_y]
            dict_json['Entry_{}'.format(i)].append("Question: What would be {}'s x value when its y value is {}?".format(added, y_value))
            answer_dot_line = current['models'][random_choice]['x'][random_choice_y] + 2
            dict_json['Entry_{}'.format(i)].append("Answer: It would be {}".format(answer_dot_line))

        if current['type'] == 'vbar_categorical':
            added = random.choice(list_color_toadd)
            random_choice = random.choice(range(len(current['models'][0]['labels'])))
            selected = current['models'][0]['labels'][random_choice]
            dict_json['Entry_{}'.format(i)] = []
            dict_json['Entry_{}'.format(i)].append("dataset_id: figureqa-train1-v1")
            dict_json['Entry_{}'.format(i)].append("Image_index: {}".format(current['image_index']))
            dict_json['Entry_{}'.format(i)].append("Graph_type: {}".format(current['type']))
            dict_json['Entry_{}'.format(i)].append("Passage: {} is such that it is 10 units greater than {}".format(added, selected))
            dict_json['Entry_{}'.format(i)].append("Question: What would be {}'s maximum value?".format(added))
            answer_vbar = current['models'][0]['y'][random_choice] + 10
            dict_json['Entry_{}'.format(i)].append("Answer: The value of {} would be {}".format(added, answer_vbar))

        if current['type'] == 'hbar_categorical':
            added = random.choice(list_color_toadd)
            random_choice = random.choice(range(len(current['models'][0]['labels'])))
            selected = current['models'][0]['labels'][random_choice]
            dict_json['Entry_{}'.format(i)] = []
            dict_json['Entry_{}'.format(i)].append("dataset_id: figureqa-train1-v1")
            dict_json['Entry_{}'.format(i)].append("Image_index: {}".format(current['image_index']))
            dict_json['Entry_{}'.format(i)].append("Graph_type: {}".format(current['type']))
            dict_json['Entry_{}'.format(i)].append("Passage: {} is such that it is 2 units less than {}".format(added, selected))
            dict_json['Entry_{}'.format(i)].append("Question: What would be {}'s maximum value?".format(added))
            answer_hbar = current['models'][0]['x'][random_choice] - 2
            dict_json['Entry_{}'.format(i)].append("Answer: The value of {} would be {}".format(added, answer_hbar))

    with open('data.json', 'w') as outfile:
        json.dump(dict_json, outfile, indent=2)


data_gen(1000)