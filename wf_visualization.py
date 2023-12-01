import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def visualize(df):
    df = df.drop(df.columns[0], axis=1)
    # extra column from preprocessing step(Unnamed; 0,1,2,3){it was indexing in a new column}

    # Quantitative features
    min_array = []
    max_array = []
    median_array = []

    # Dont have most frequent categories in the dataset read Description in project_exploration.md
    # finding highest expenditure in a quarter year and lowest expenditure in a quarter year
    # Qualitative features
    hi_exp = []
    lo_exp = []

    x = np.array(df.columns)
    flag = len(df)
    y = len(x)-1
    for i in x[1:]:
        a = np.array(df[i])
        min_array.append(np.min(a))
        max_array.append(np.max(a))
        median_array.append(np.median(a))

    for i in range(flag):
        a = np.array(df.iloc[i])
        a = a[1:]
        hi_exp.append(np.max(a))
        lo_exp.append(np.min(a))

    output_text = min_array, max_array, median_array, hi_exp, lo_exp
    file_name = "data_processed\summary.txt"

    with open(file_name, "w") as file:
        for i in output_text:
            file.write(str(i))
            file.write("\n")
            file.write("\n")

    qua_vis_1 = [min_array, max_array, median_array]
    qua_df = pd.DataFrame(qua_vis_1)
    corr_mat = qua_df.corr()

    output_text = str(corr_mat)
    file_name = "data_processed\correlations.txt"

    with open(file_name, "w") as file:
        file.write(output_text)

    plt.scatter(min_array, max_array)
    plt.title("Min_array, Max_array")
    plt.xlabel("Min array")
    plt.ylabel("Max array")
    plt.savefig("visuals\quantitative_scatter_Min-Max.png")

    plt.scatter(min_array, median_array)
    plt.title("Min_array, Median_array")
    plt.xlabel("Min array")
    plt.ylabel("Median array")
    plt.savefig("visuals\quantitative_scatter_Min-Median.png")

    plt.scatter(median_array, max_array)
    plt.title("Median_array, Max_array")
    plt.xlabel("Median array")
    plt.ylabel("Max array")
    plt.savefig("visuals\quantitative_scatter_Median-Max.png")

    year = df['Title']

    plt.hist(lo_exp, bins=30)
    plt.xlabel("Year")
    plt.ylabel("Lowest Expenditure per year")
    plt.title("Histogram")
    plt.xticks(lo_exp, year)
    # X axes labels are tough to make out due to large quantity of values(1156)
    plt.savefig("visuals\qualitative_histogram_expenditure(Low).png")

    plt.hist(hi_exp, bins=30)
    plt.xlabel("Year")
    plt.ylabel("Highest Expenditure per year")
    plt.title("Histogram")
    plt.xticks(hi_exp, year)
    # X axes labels are tough to make out due to large quantity of values(1156)
    plt.savefig("visuals\qualitative_histogram_expenditure(High).png")

    plt.show()
