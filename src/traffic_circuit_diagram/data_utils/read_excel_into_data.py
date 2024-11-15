import pandas as pd
import tkinter as tk
from tkinter import filedialog
import os
import csv
from traffic_circuit_diagram.file_handling_helper import open_file_picker
from traffic_circuit_diagram.file_handling_helper import open_folder_picker

def output_pipe_delimited_txt_file(diagram_df):
    #Just replace this with a file picker
    acceptable_input = False
    while (not acceptable_input):
        outgoing_file_name = input("Write Output File Name Without Extension:\n")
        user_validation = input("Is this the file you wanted? (submit n to try again): ")
        if user_validation != "n":
            acceptable_input = True
    folder_location = open_folder_picker()
    full_outgoing_file_name = os.path.join(folder_location, outgoing_file_name+'.txt')
    with open(full_outgoing_file_name, "w", newline="\n") as f:
        writer = csv.writer(f, delimiter='|')
        for row in diagram_df.itertuples(index=False):
            writer.writerow([x for x in row if pd.notna(x)])

def main():
    file_path_to_data = open_file_picker(file_type  = "excel")
    diagram_df = pd.read_excel(file_path_to_data, header = None)
    output_pipe_delimited_txt_file(diagram_df)

if __name__ == "__main__":
    main()