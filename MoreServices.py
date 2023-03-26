import pandas as pd
import plotly.express as px

df = pd.read_csv('CentennialReal.csv')

local = df.loc[(df["How far do you travel to get to the Park?"]=="Less than a mile away") | (df["How far do you travel to get to the Park?"]=="6 - 9 miles away") | (df["How far do you travel to get to the Park?"]=="1 - 5 miles away")]

count1 = local["Do you believe the Park could benefit from more ongoing activities or services?"].value_counts()

dff = pd.DataFrame()
dff["names"] = [str(i) for i in count1.index]
dff["number"] = count1.values
fig_pie = px.pie(dff, values="number", names="names", title="Percentage of Locals that Live 9 or Less Miles Away that Believe the Park Could Benefit from More Ongoing Activities")
fig_pie.show()