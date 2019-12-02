"""
TODO: Refactor code in this file
"""
import matplotlib.pyplot as plt


def plot_chart(data_frame, exclude_row, exclude_columns):
    # plot bar chart
    if exclude_row:
        df = data_frame.describe().drop(labels=exclude_row, axis=0)
        ax = df.plot(kind='bar', title="Representation", figsize=(15, 10), legend=True, fontsize=12)
        ax.set_xlabel("X", fontsize=12)
        ax.set_ylabel("Y", fontsize=12)
        # avoid scientific notation 👇
        # plt.ticklabel_format(style='plain', axis='y')
        return plt.show()
    if exclude_columns:
        df = data_frame.describe().drop(labels=exclude_columns, axis=1)
        ax = df.plot(kind='bar', title="Representation", figsize=(15, 10), legend=True, fontsize=12)
        ax.set_xlabel("X", fontsize=12)
        ax.set_ylabel("Y", fontsize=12)
        # avoid scientific notation 👇
        # plt.ticklabel_format(style='plain', axis='y')
        return plt.show()
    return print('Error')
