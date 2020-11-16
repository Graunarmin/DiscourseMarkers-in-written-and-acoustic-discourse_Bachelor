from matplotlib import pyplot as plt


def plot_piechart():
    plt.style.use('fivethirtyeight')

    slices = [60, 40]
    labels = ["Sixty", "Fourty"]
    colors = ['#1DB954', '#e62b1e']

    # matplotlib wedge für die "Trennstriche" zwischen den Farben
    plt.pie(slices, labels=labels, colors=colors, wedgeprops={'edgecolor': 'black'})

    plt.title("Awesome Pie Chart")
    plt.tight_layout()
    plt.show()


def plot_more_awesome_piechart():
    # Language Popularity
    slices = [59219, 55466, 47544, 36443, 35917]
    labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java', ]

    # list of floats that show how much a certain slide is supposed to be emphasized
    explode = [0, 0, 0, 0.1, 0]

    plt.pie(slices, labels=labels,
            explode=explode, shadow=True, startangle=100, autopct='%1.1f%%')

    plt.title("Awesome Pie Chart")
    plt.tight_layout()
    plt.show()


def main():
    # plot_piechart()
    plot_more_awesome_piechart()


if __name__ == '__main__':
    main()