import csv
import pandas as pd

def data_clean():
    new_rows_list = []
    with open("data/recipeData.csv", "r", errors="ignore") as fd:
        reader = csv.reader(fd)
        cnt = 0
        for row in reader:
            if cnt < 100:
                new_rows_list.append(row)
                cnt += 1
    fd.close

    with open("data/new_recipeData.csv", "w") as fp:
        for row in new_rows_list:
            fp.write(",".join(row) + "\n")
    fp.close()


    data = pd.read_csv("data/new_recipeData.csv",delimiter = ",")
    return data
