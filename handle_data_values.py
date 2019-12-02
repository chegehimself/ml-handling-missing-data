import numpy
import pandas as pd
from utils.helpers import plot_chart
from utils.database import DBConnection


class HandleDataValues(object):

    def __init__(self, param):
        self.param = param
        self.db = DBConnection().db_instance()
        self.cursor = self.db.cursor()

    def with_missing_values(self):
        """
        :return: plot of a bar chart for data with missing values
        """
        self.cursor.execute(f"SELECT {self.param} FROM country")

        rows = self.cursor.fetchall()
        df = pd.DataFrame([[item for item in row] for row in rows])
        df.rename(columns={0: f'{self.param}'}, inplace=True)
        df = df.sort_values([f'{self.param}'], ascending=[1])

        # plot bar chart
        print(df.describe())
        plot_chart(data_frame=df, exclude_row=['count', 'std'], title=f'{self.param} with missing values', axis=0)

    def without_missing_values(self):
        """
        :return:  plot of a bar chart for data without missing values
        """
        self.cursor.execute(f"SELECT {self.param} FROM country")

        rows = self.cursor.fetchall()
        df = pd.DataFrame([[item for item in row] for row in rows])
        df.rename(columns={0: f'{self.param}'}, inplace=True)
        df = df.sort_values([f'{self.param}'], ascending=[1])
        df[[f'{self.param}']] = df[[f'{self.param}']].replace(0, numpy.NaN)
        df.fillna(df.mean(), inplace=True)
        print(df.describe())
        plot_chart(data_frame=df, exclude_row=['count', 'std'], title=f'{self.param} without missing values', axis=0)

