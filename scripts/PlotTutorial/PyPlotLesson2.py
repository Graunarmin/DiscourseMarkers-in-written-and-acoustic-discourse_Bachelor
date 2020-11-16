import matplotlib.pyplot as plt
import numpy as np
import csv
from collections import Counter
import pandas as pd


# https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html
# https://www.youtube.com/watch?v=nKxLfUrkLE8
# Font Pfad: /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf
# https://stackoverflow.com/questions/3899980/how-to-change-the-font-size-on-a-matplotlib-plot

def lines_over_barchart():
    # Mix Barchart and Linechart

    # print out the available styles
    # print(plt.style.available)

    # Use a style
    plt.style.use('fivethirtyeight')

    # Use the ages as x for both y-value sets
    ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

    # Median Python Developer Salaries by Age
    py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998,
                70003, 70000, 71496, 75370, 83640]
    # Draw the Python line in blue
    plt.plot(ages_x, py_dev_y, color='#5a7d9a', linewidth=3, label='Python Devs')

    # Median JavaScript Developer Salaries by Age
    js_dev_y = [37810, 43515, 46823, 49293, 53437,
                56373, 62375, 66674, 68745, 68746, 74583]
    # Draw the JavaScript Line in yellow
    plt.plot(ages_x, js_dev_y, color='#adad3b', linewidth=3, label='JavaScript Devs')

    # Median Developer Salaries by Age
    dev_y = [38496, 42000, 46752, 49320, 53200,
             56000, 62316, 64928, 67317, 68748, 73752]
    # Make a simple plot with a black, dashed line
    plt.bar(ages_x, dev_y, color='#444444', label='All Devs')

    # Create Labels for x and y achsis
    plt.xlabel('Ages')
    plt.ylabel('Median Salary (USD)')

    # Create a Title for the Plot
    plt.title('Median Salary (USD) by Age')

    # Add a Legend that is "filled" by the 'label' arguments given to the plot() Functions
    plt.legend()

    # Add a Grid so it's better readable
    # Some styles already habe a grid!
    plt.grid(True)

    # Padding (makes it look better)
    plt.tight_layout()

    # save png automatically
    # plt.savefig('awesomeplot.png')

    # Draw the Plot in a seperate window
    plt.show()


def barchart():
    # print out the available styles
    # print(plt.style.available)

    # Use a style
    plt.style.use('fivethirtyeight')

    # Use the ages as x for both y-value sets
    ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

    # Create a numpy array of indexes so we can shift the bars so that they are not
    # on top of each other but side by side
    x_indexes = np.arange(len(ages_x))

    # bar width
    width = 0.25

    # Median Developer Salaries by Age
    dev_y = [38496, 42000, 46752, 49320, 53200,
             56000, 62316, 64928, 67317, 68748, 73752]
    # Make a simple plot with a black, dashed line
    plt.bar(x_indexes - width, dev_y, width=width, color='#444444', label='All Devs')

    # Median Python Developer Salaries by Age
    py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998,
                70003, 70000, 71496, 75370, 83640]
    # Draw the Python line in blue
    plt.bar(x_indexes, py_dev_y, width=width, color='#5a7d9a', linewidth=3, label='Python Devs')

    # Median JavaScript Developer Salaries by Age
    js_dev_y = [37810, 43515, 46823, 49293, 53437,
                56373, 62375, 66674, 68745, 68746, 74583]
    # Draw the JavaScript Line in yellow
    plt.bar(x_indexes + width, js_dev_y, width=width, color='#adad3b', linewidth=3, label='JavaScript Devs')

    # Create Labels for x and y achsis
    plt.xlabel('Ages')
    plt.ylabel('Median Salary (USD)')

    # Create a Title for the Plot
    plt.title('Median Salary (USD) by Age')

    # Add a Legend that is "filled" by the 'label' arguments given to the plot() Functions
    plt.legend()

    # use the x_indexes for the ticks, BUT the ages for the labels
    plt.xticks(ticks=x_indexes, labels=ages_x)

    # Add a Grid so it's better readable
    # Some styles already habe a grid!
    plt.grid(True)

    # Padding (makes it look better)
    plt.tight_layout()

    # save png automatically
    # plt.savefig('awesomeplot.png')

    # Draw the Plot in a seperate window
    plt.show()


def load_data_from_csv():
    with open("data.csv", 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        # Counters count the number of occurences
        language_counter = Counter()
        for row in csv_reader:
            # update the Counter with every new row
            language_counter.update(row['LanguagesWorkedWith'].split(';'))

    create_lists(language_counter)


def load_data_with_pandas():
    data = pd.read_csv('data.csv')
    ids = data['Responder_id']
    lang_responses = data['LanguagesWorkedWith']

    language_counter = Counter()

    for response in lang_responses:
        language_counter.update(response.split(';'))

    create_lists(language_counter)


def create_lists(language_counter):
    # most_common(x) prints the x most common occurences as a list of tuples (language, count)
    # print(language_counter.most_common(15))

    languages = []
    popularity = []

    for item in language_counter.most_common(15):
        languages.append(item[0])
        popularity.append(item[1])

    # reverse the lists so the most used languages is on top
    languages.reverse()
    popularity.reverse()

    print(languages)
    print(popularity)
    horizontal_bar_chart(languages, popularity)


def horizontal_bar_chart(languages, popularity):

    # title_font = {'fontname': 'Casper'}
    plt.rcParams["font.family"] = "Casper"
    # print out the available styles
    # print(plt.style.available)
    plt.style.use('fivethirtyeight')

    # barh creates a horizontal bar chart. Remember to exchange x and y labels!
    plt.barh(languages, popularity)

    # Create a Title for the Plot
    # plt.title('Most Popular Programming Languages', **title_font)
    plt.title('Most Popular Programming Languages')

    # plt.ylabel('Programming Languages')
    plt.xlabel('People who use')

    # Padding (makes it look better)
    plt.tight_layout()

    # save png automatically
    # plt.savefig('awesomeplot.png')

    # Draw the Plot in a seperate window
    plt.show()


# ------------ MAIN -------------
def main():
    # barchart()
    # load_data_from_csv()
    load_data_with_pandas()


if __name__ == '__main__':
    main()
