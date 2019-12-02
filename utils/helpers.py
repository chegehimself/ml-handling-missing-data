import matplotlib.pyplot as plt


def plot_chart(data_frame, exclude_row, title, axis):
    """
    Plots a bar chart
    """
    df = data_frame.describe().drop(labels=exclude_row, axis=axis)
    ax = df.plot(kind='bar', title=title, figsize=(15, 10), legend=True, fontsize=12)
    ax.set_xlabel("X", fontsize=12)
    ax.set_ylabel("Y", fontsize=12)
    return plt.show()
