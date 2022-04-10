import random
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from multiprocessing import Process
import csv
import random
import time


def data_gen():
    x_value = 0
    total_1 = 1000
    total_2 = 1000

    fieldnames = ["x_value", "total_1", "total_2"]

    with open('data.csv', 'w') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()

    while True:

        with open('data.csv', 'a') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            info = {
                "x_value": x_value,
                "total_1": total_1,
                "total_2": total_2
            }

            csv_writer.writerow(info)
            print(x_value, total_1, total_2)

            x_value += 1
            total_1 = total_1 + random.randint(-6, 8)
            total_2 = total_2 + random.randint(-5, 6)

        time.sleep(1)


def animate_data():
    plt.style.use('fivethirtyeight')

    def animate(f):
        data = pd.read_csv('data.csv', header=0, delimiter=',')
        x = data['x_value']
        y = data['total_1']
        z = data['total_2']
        plt.cla()

        plt.plot(x, y, label='Channel 1')

        plt.legend(loc='upper left')
        plt.tight_layout()

    anim = FuncAnimation(plt.gcf(), animate, interval=1000)

    plt.show()


if __name__ == '__main__':
    p1 = Process(target=data_gen)
    p1.start()
    p2 = Process(target=animate_data)
    p2.start()
    p1.join()
    p2.join()
