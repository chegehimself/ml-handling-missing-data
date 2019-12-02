import pandas as pd

from database import DBConnection
from helpers import plot_chart
db = DBConnection().db_instance()

cursor = db.cursor()

cursor.execute("SELECT lifeexpectancy FROM country")

rows = cursor.fetchall()
df = pd.DataFrame([[item for item in row] for row in rows])
df.rename(columns={0: 'LifeExpectancy'}, inplace=True)
df = df.sort_values(['LifeExpectancy'], ascending=[1])

# plot bar chart
plot_chart(data_frame=df, exclude_row=['count', 'std'], exclude_columns=None)
