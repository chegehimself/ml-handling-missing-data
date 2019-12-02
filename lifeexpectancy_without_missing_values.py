import chart_studio.plotly as py
import plotly.graph_objs as go
import pandas as pd
import numpy
from helpers import plot_chart

from database import DBConnection

db = DBConnection().db_instance()

cursor = db.cursor()

cursor.execute("SELECT lifeexpectancy FROM country")

rows = cursor.fetchall()
df = pd.DataFrame([[item for item in row] for row in rows])
df.rename(columns={0: 'LifeExpectancy'}, inplace=True)
df = df.sort_values(['LifeExpectancy'], ascending=[1])
df[['LifeExpectancy']] = df[['LifeExpectancy']].replace(0, numpy.NaN)
df.fillna(df.mean(), inplace=True)
print(df.describe())
plot_chart(data_frame=df, exclude_row=['count', 'std'], exclude_columns=None)