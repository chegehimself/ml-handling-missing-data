import pandas as pd

from database import DBConnection
from helpers import plot_chart
db = DBConnection().db_instance()

cursor = db.cursor()

cursor.execute("SELECT population FROM country")

rows = cursor.fetchall()
df = pd.DataFrame([[item for item in row] for row in rows])
df.rename(columns={0: 'population'}, inplace=True)
df = df.sort_values(['population'], ascending=[1])
print(df.describe())
# plot bar chart
plot_chart(data_frame=df, exclude_row=['count', 'std'], exclude_columns=None)
