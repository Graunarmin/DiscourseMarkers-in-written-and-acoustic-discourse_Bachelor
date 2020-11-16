import pandas as pd
from matplotlib import pyplot as plt


def basic_plot():
    plt.style.use('seaborn')

    data = pd.read_csv('data_1.csv')
    ages = data['Age']
    dev_salaries = data['All_Devs']
    py_salaries = data['Python']
    js_salaries = data['JavaScript']

    plt.plot(ages, py_salaries, label='Python')
    plt.plot(ages, js_salaries, label='JavaScript')

    plt.plot(ages, dev_salaries, color='#444444',
             linestyle='--', label='All Devs')

    plt.legend()
    plt.title("Median Salary (USD) by Age")
    plt.xlabel('Ages')
    plt.ylabel('Median Salary (USD)')

    plt.tight_layout()
    plt.show()


def with_subplots():
    plt.style.use('seaborn')

    data = pd.read_csv('data_1.csv')
    ages = data['Age']
    dev_salaries = data['All_Devs']
    py_salaries = data['Python']
    js_salaries = data['JavaScript']
    py_salaries_2 = data['Python']

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, sharey=True, sharex=True)

    ax1.plot(ages, dev_salaries, color='#444444',
             linestyle='--', label='All Devs')

    ax2.plot(ages, py_salaries, label='Python')
    ax3.plot(ages, js_salaries, label='JavaScript')
    ax4.plot(ages, py_salaries_2, label='Python2')

    ax1.legend()

    ax1.set_title("Median Salary (USD) by Age")
    ax1.set_ylabel('Median Salary (USD)')

    ax2.legend()

    ax3.legend()

    ax3.set_xlabel('Ages')
    ax3.set_ylabel('Median Salary (USD)')

    ax4.legend()

    ax4.set_xlabel('Ages')

    plt.tight_layout()
    plt.show()


# ------------ MAIN -------------
def main():
    with_subplots()


if __name__ == '__main__':
    main()