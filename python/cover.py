import argparse
import glob
import os
import re

import camelot
import pandas as pd

PATH_DOWNLOADS = "../../../Downloads/bulletins/"
ROW_NAME = 5
ROW_PERIOD = 0

# takes a dataframe of the cover schedule
# returns (repl_lesson, repl_duty)
# where each list contains strings of teachers
def extract_teachers(df, row_name, row_period) :
    lessons = ["Period 1", "Period 2", "Period 3", "Period 4", "Period 5"]
    repls_lesson = []
    for lesson in lessons :
        # extract part of dataframe with certain period
        df_slice = df[df[row_period] == lesson]

        # list(set(...)) removes duplicates inside ...
        names_raw = list(set(df_slice[row_name]))

        # remove newline characters in names
        names = [re.sub(r"\n", lambda l: "", name) for name in names_raw]

        repls_lesson += names

    duties = ["break", "Lunch 1", "Lunch 2", "pastoral"]
    repls_duty = []
    for duty in duties :
        # extract part of dataframe with certain period
        df_slice = df[df[row_period] == duty]

        # list(set(...)) removes duplicates inside ...
        names_raw = list(set(df_slice[row_name]))

        # remove newline characters in names
        names = [re.sub(r"\n", lambda l: "", name) for name in names_raw]

        repls_duty += names

    return (repls_lesson, repls_duty)
    
def tally_pdf(filename_cover, dict_tally) :
    # load the pdf file
    print(f"reading: {filename_cover}...")
    tables = camelot.read_pdf(filename_cover, pages='1-end')
    print("pdf read!")

    covered_lesson = []
    covered_duty = []
    n_covers = 0        # total number of covered lessons
    
    # loop over the tables found in the pdf
    for table in tables:
        df = table.df
        # if the table has exactly 7 columns
        if len(df.columns) == 7:
            l, d = extract_teachers(df, ROW_NAME, ROW_PERIOD)

            covered_lesson += l
            covered_duty += d
    
    # count the tally for those who covered a lesson
    for name in covered_lesson :
        if name in dict_tally :
            dict_tally[name] += 1
        else :
            dict_tally[name] = 1
    
    # count the tally for those who covered a duty
    for name in covered_duty :
        if name in dict_tally :
            dict_tally[name] += 0.5
        else :
            dict_tally[name] = 0.5

    return dict_tally

if __name__ == "__main__" :
    covers = glob.glob(os.path.join(PATH_DOWNLOADS, "Bulletin*.pdf"))

    dict_tally = {}
    for cover in covers :
        dict_tally = tally_pdf(cover, dict_tally)
        print(dict_tally)

    _ = dict_tally.pop('Not Required')
    list_tally = list(dict_tally.items())
    list_tally.sort(key=lambda x:-x[1])
    df = pd.DataFrame(list_tally, columns=["Name", "Covers"])
    df.to_csv(os.path.join(PATH_DOWNLOADS, "covers.csv"))
    print("file saved, all completed!")