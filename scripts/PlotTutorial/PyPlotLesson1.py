import matplotlib.pyplot as plt


def example1():
    plt.plot([1, 2, 3, 4])
    plt.ylabel('some numbers')
    names = ['group_a', 'group_b', 'group_c']
    values = [1, 10, 100]

    plt.figure(figsize=(9, 3))

    plt.subplot(131)
    plt.bar(names, values)
    # plt.subplot(132)
    # plt.scatter(names, values)
    # plt.subplot(133)
    # plt.plot(names, values)
    plt.suptitle('Categorical Plotting')
    plt.show()


# https://www.youtube.com/watch?v=UO98lJQ3QGI
def example_one_line():
    # Median Developer Salaries by Age
    dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

    dev_y = [38496, 42000, 46752, 49320, 53200,
             56000, 62316, 64928, 67317, 68748, 73752]

    # Make a simple plot
    plt.plot(dev_x, dev_y)

    # Create Labels for x and y achsis
    plt.xlabel('Ages')
    plt.ylabel('Median Salary (USD)')

    # Create a Title for the Plot
    plt.title('Median Salary (USD) by Age')

    # Draw the Plot in a seperate window
    plt.show()


def example_two_lines():

    # Use the ages as x for both y-value sets
    ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

    # Median Developer Salaries by Age
    dev_y = [38496, 42000, 46752, 49320, 53200,
             56000, 62316, 64928, 67317, 68748, 73752]

    # Make a simple plot with a black, dashed line
    # https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html
    plt.plot(ages_x, dev_y, color='#444444', linestyle='--', marker='.', label='All Devs')

    # Median Python Developer Salaries by Age
    py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998,
                70003, 70000, 71496, 75370, 83640]

    # Draw the second line in blue
    plt.plot(ages_x, py_dev_y, color='#5a7d9a', label='Python Devs')

    # Create Labels for x and y achsis
    plt.xlabel('Ages')
    plt.ylabel('Median Salary (USD)')

    # Create a Title for the Plot
    plt.title('Median Salary (USD) by Age')

    # Add a Legend that is "filled" by the 'label' arguments given to the plot() Functions
    plt.legend()

    # Draw the Plot in a seperate window
    plt.show()


def example_3_lines():

    # print out the available styles
    print(plt.style.available)

    # Use a style
    plt.style.use('fivethirtyeight')

    # Use the ages as x for both y-value sets
    ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

    # https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html

    # Median Python Developer Salaries by Age
    py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998,
                70003, 70000, 71496, 75370, 83640]
    # Draw the second line in blue
    plt.plot(ages_x, py_dev_y, color='#5a7d9a', linewidth=3, label='Python Devs')

    # Median JavaScript Developer Salaries by Age
    js_dev_y = [37810, 43515, 46823, 49293, 53437,
                56373, 62375, 66674, 68745, 68746, 74583]
    # Draw the second line in blue
    plt.plot(ages_x, js_dev_y, color='#adad3b', linewidth=3, label='JavaScript Devs')

    # Median Developer Salaries by Age
    dev_y = [38496, 42000, 46752, 49320, 53200,
             56000, 62316, 64928, 67317, 68748, 73752]
    # Make a simple plot with a black, dashed line
    plt.plot(ages_x, dev_y, color='#444444', linestyle='--', marker='.', label='All Devs')

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
    plt.savefig('awesomeplot.png')

    # Draw the Plot in a seperate window
    plt.show()


# ------------ MAIN -------------
def main():
    example_3_lines()


if __name__ == '__main__':
    main()