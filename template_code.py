import pandas as pd


input_file = "data/template.csv"
output_folder = "template_output"

import os
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

dataframe = pd.read_csv(input_file)

for name,age in zip(dataframe["name"], dataframe["age"]):
    complete_output_folder = output_folder + "/" + name
    if not os.path.exists(complete_output_folder):
        os.makedirs(complete_output_folder)

    f = open(complete_output_folder + "/" + name + "_" + str(age) + ".txt", "a")
    f.write("{} is {} years old".format(name, age))
    f.close()
