#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#import necessary modules/packages
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
import pandas as pd
import numpy as np
from jupyter_dash import JupyterDash
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

css = 'https://codepen.io/chriddyp/pen/bWLwgP.css'
app = JupyterDash(__name__, external_stylesheets=[css])
server = app.server

#reads in 2022 Centennial Park User Survey
df = pd.read_csv(r'C:\Users\mayam\Downloads\2022 Centennial Park User Survey (Responses)-2.xlsx - Form Responses 1.csv')


#cleaning data: creates dataframe of just locals that live 9 miles away or less and are/aren't aware of CPC
df_distance_exist = df[["How far do you travel to get to the Park?", "Were you aware that there is a nonprofit support group, Centennial Park Conservancy, that helps to underwrite Park improvements and arts & educational programs in the Parthenon and Park through donations and memberships?", "Are you a member of Centennial Park Conservancy?"]]
df_distance_exist = df_distance_exist.loc[df_distance_exist['How far do you travel to get to the Park?'] != '10+ miles away, but no more than 50 miles']
df_distance_exist = df_distance_exist.loc[df_distance_exist['How far do you travel to get to the Park?'] != 'Greater than 50 miles']
df_distance_exist = df_distance_exist.loc[df_distance_exist['How far do you travel to get to the Park?'] != 'From out of State, but in the U.S.']
df_distance_exist = df_distance_exist.loc[df_distance_exist['How far do you travel to get to the Park?'] != 'From another country']

#cleaning data: changes responses from "Yes" to "Know we exist" and "No" to "Don't know we exist" for visualization
df_distance_exist = df_distance_exist.replace("Yes", "Know we exist")
df_distance_exist = df_distance_exist.replace("No", "Don't know we exist")
#df_distance_exist['Local Member?'] = np.where(df_distance_exist['Are you a member of Centennial Park Conservancy?'] == "Yes", 'Member', 'Non-member')
#print(df_distance_exist)

#cleaning data: create dataset of locals who are members
df_distance_exist_members = df_distance_exist
df_distance_exist_members = df_distance_exist_members.loc[df_distance_exist_members['Are you a member of Centennial Park Conservancy?']!= "Don't know we exist"]

#cleaning data: create dataset of locals who are non-members
df_distance_exist_non_members = df_distance_exist
df_distance_exist_non_members = df_distance_exist_non_members.loc[df_distance_exist_non_members['Are you a member of Centennial Park Conservancy?']!= "Know we exist"]


#creates pie chart for percentage of all locals that are/aren't aware of CPC
count1 = df_distance_exist["Were you aware that there is a nonprofit support group, Centennial Park Conservancy, that helps to underwrite Park improvements and arts & educational programs in the Parthenon and Park through donations and memberships?"].value_counts()
dff = pd.DataFrame()
dff["names"] = [str(i) for i in count1.index]
dff["number"] = count1.values
fig_pie = px.pie(dff, values="number", names="names", title="Percentage of All Locals that Live 9 or Less Miles Away that Know/Don't Know CPC Exists")
#fig_pie.update_layout(template="plotly_dark")

#creates a pie chart for percentage of local members that are/aren't aware of CPC
count2 = df_distance_exist_members["Were you aware that there is a nonprofit support group, Centennial Park Conservancy, that helps to underwrite Park improvements and arts & educational programs in the Parthenon and Park through donations and memberships?"].value_counts()
dff2 = pd.DataFrame()
dff2["names"] = [str(i) for i in count2.index]
dff2["number"] = count2.values
fig_pie_members = px.pie(dff2, values="number", names="names", title="Percentage of Local Members that Live 9 or Less Miles Away that Know/Don't Know CPC Exists")

#creates a pie chart for percentage of local non-members that are/aren't aware of CPC
count3 = df_distance_exist_non_members["Were you aware that there is a nonprofit support group, Centennial Park Conservancy, that helps to underwrite Park improvements and arts & educational programs in the Parthenon and Park through donations and memberships?"].value_counts()
dff3 = pd.DataFrame()
dff3["names"] = [str(i) for i in count3.index]
dff3["number"] = count3.values
fig_pie_non_members = px.pie(dff3, values="number", names="names", title="Percentage of Local Non-members that Live 9 or Less Miles Away that Know/Don't Know CPC Exists")



#create dataset of only reasons why people visit the park
df_why_visit = df[["Why do you visit the Park? (check all that apply)"]]

#cleaning data to find counts of reasons why people visit the park
outdoor_count = df_why_visit["Why do you visit the Park? (check all that apply)"].str.count("Spend time in an outdoor green space")
outdoor_count = outdoor_count.sum()
#print(outdoor_count)

exercise_count = df_why_visit["Why do you visit the Park? (check all that apply)"].str.count("Exercise")
exercise_count = exercise_count.sum()
#print(exercise_count)

parthenon_count = df_why_visit["Why do you visit the Park? (check all that apply)"].str.count("Visit the Parthenon")
parthenon_count = parthenon_count.sum()
#print(parthenon_count)

arts_center_count = df_why_visit["Why do you visit the Park? (check all that apply)"].str.count("Visit Centennial Arts Center")
arts_center_count = arts_center_count.sum()
#print(arts_center_count)

performing_studios_count = df_why_visit["Why do you visit the Park? (check all that apply)"].str.count("Visit Centennial Performing Arts Studios")
performing_studios_count = performing_studios_count.sum()
#print(performing_studios_count)

events_count = df_why_visit["Why do you visit the Park? (check all that apply)"].str.count("Attend events")
events_count = events_count.sum()
#print(events_count)

picnic_count = df_why_visit["Why do you visit the Park? (check all that apply)"].str.count("Picnic")
picnic_count = picnic_count.sum()
#print(picnic_count)

walk_dog_count = df_why_visit["Why do you visit the Park? (check all that apply)"].str.count("Walk dog")
walk_dog_count = walk_dog_count.sum()
#print(walk_dog_count)

dog_park_count = df_why_visit["Why do you visit the Park? (check all that apply)"].str.count("Visit the dog park")
dog_park_count = dog_park_count.sum()
#print(dog_park_count)

feed_ducks_count = df_why_visit["Why do you visit the Park? (check all that apply)"].str.count("Feed the ducks")
feed_ducks_count = feed_ducks_count.sum()
#print(feed_ducks_count)

playground_count = df_why_visit["Why do you visit the Park? (check all that apply)"].str.count("Visit the playground")
playground_count = playground_count.sum()
#print(playground_count)

volleyball_count = df_why_visit["Why do you visit the Park? (check all that apply)"].str.count("Use the volleyball courts")
volleyball_count = volleyball_count.sum()
#print(volleyball_count)

sports_count = df_why_visit["Why do you visit the Park? (check all that apply)"].str.count("Play sports")
sports_count = sports_count.sum()
#print(sports_count)

#creates df with one column containing reasons and other column containing all the counts variables
why_visit_data = [["Spend time in an outdoor green space", outdoor_count],["Excercise", exercise_count], ["Visit the Parthenon", parthenon_count], ["Visit Centennial Arts Center", arts_center_count], ["Visit Centennial Performing Arts Studios", performing_studios_count], ["Attend events", events_count], ["Picnic", picnic_count], ["Walk dog", walk_dog_count], ["Visit the dog park", dog_park_count], ["Feed the ducks", feed_ducks_count], ["Visit the playground", playground_count], ["Use the volleyball courts", volleyball_count], ["Play sports", sports_count]]
df_why_visit_count = pd.DataFrame(why_visit_data, columns=["Reason", "Count"])
#print(df_why_visit_count)


#creates bar chart of reasons why people visit the park
fig_bar = px.bar(df_why_visit_count, x="Reason", y="Count", title="Why All People Visit Centennial Park", text_auto=True, color="Reason")
fig_bar.update_layout(xaxis={'categoryorder':'total descending'}) 

#cleaning data to create df of why local people visit the park
df_why_visit_local = df[["Why do you visit the Park? (check all that apply)", "How far do you travel to get to the Park?"]]
df_why_visit_local = df_why_visit_local.loc[df_why_visit_local['How far do you travel to get to the Park?'] != '10+ miles away, but no more than 50 miles']
df_why_visit_local = df_why_visit_local.loc[df_why_visit_local['How far do you travel to get to the Park?'] != 'Greater than 50 miles']
df_why_visit_local = df_why_visit_local.loc[df_why_visit_local['How far do you travel to get to the Park?'] != 'From out of State, but in the U.S.']
df_why_visit_local = df_why_visit_local.loc[df_why_visit_local['How far do you travel to get to the Park?'] != 'From another country']

#cleaning data to find counts of reasons why local people visit the park
outdoor_count_local = df_why_visit_local["Why do you visit the Park? (check all that apply)"].str.count("Spend time in an outdoor green space")
outdoor_count_local = outdoor_count_local.sum()

exercise_count_local = df_why_visit_local["Why do you visit the Park? (check all that apply)"].str.count("Exercise")
exercise_count_local = exercise_count_local.sum()

parthenon_count_local = df_why_visit_local["Why do you visit the Park? (check all that apply)"].str.count("Visit the Parthenon")
parthenon_count_local = parthenon_count_local.sum()

arts_center_count_local = df_why_visit_local["Why do you visit the Park? (check all that apply)"].str.count("Visit Centennial Arts Center")
arts_center_count_local = arts_center_count_local.sum()

performing_studios_count_local = df_why_visit_local["Why do you visit the Park? (check all that apply)"].str.count("Visit Centennial Performing Arts Studios")
performing_studios_count_local = performing_studios_count_local.sum()

events_count_local = df_why_visit_local["Why do you visit the Park? (check all that apply)"].str.count("Attend events")
events_count_local = events_count_local.sum()

picnic_count_local = df_why_visit_local["Why do you visit the Park? (check all that apply)"].str.count("Picnic")
picnic_count_local = picnic_count_local.sum()

walk_dog_count_local = df_why_visit_local["Why do you visit the Park? (check all that apply)"].str.count("Walk dog")
walk_dog_count_local = walk_dog_count_local.sum()

dog_park_count_local = df_why_visit_local["Why do you visit the Park? (check all that apply)"].str.count("Visit the dog park")
dog_park_count_local = dog_park_count_local.sum()

feed_ducks_count_local = df_why_visit_local["Why do you visit the Park? (check all that apply)"].str.count("Feed the ducks")
feed_ducks_count_local = feed_ducks_count_local.sum()

playground_count_local = df_why_visit_local["Why do you visit the Park? (check all that apply)"].str.count("Visit the playground")
playground_count_local = playground_count_local.sum()

volleyball_count_local = df_why_visit_local["Why do you visit the Park? (check all that apply)"].str.count("Use the volleyball courts")
volleyball_count_local = volleyball_count_local.sum()

sports_count_local = df_why_visit_local["Why do you visit the Park? (check all that apply)"].str.count("Play sports")
sports_count_local = sports_count_local.sum()

why_visit_data_local = [["Spend time in an outdoor green space", outdoor_count_local],["Excercise", exercise_count_local], ["Visit the Parthenon", parthenon_count_local], ["Visit Centennial Arts Center", arts_center_count_local], ["Visit Centennial Performing Arts Studios", performing_studios_count_local], ["Attend events", events_count_local], ["Picnic", picnic_count_local], ["Walk dog", walk_dog_count_local], ["Visit the dog park", dog_park_count_local], ["Feed the ducks", feed_ducks_count_local], ["Visit the playground", playground_count_local], ["Use the volleyball courts", volleyball_count_local], ["Play sports", sports_count_local]]
df_why_visit_count_local = pd.DataFrame(why_visit_data_local, columns=["Reason", "Count"])

fig_bar_local = px.bar(df_why_visit_count_local, x="Reason", y="Count", title="Why Local People Visit Centennial Park", text_auto=True, color="Reason")
fig_bar_local.update_layout(xaxis={'categoryorder':'total descending'}) 

#cleaning data to create df of why non-local people visit the park
df_why_visit_non_local = df[["Why do you visit the Park? (check all that apply)", "How far do you travel to get to the Park?"]]
df_why_visit_non_local = df_why_visit_non_local.loc[df_why_visit_non_local['How far do you travel to get to the Park?'] != 'Less than a mile away']
df_why_visit_non_local = df_why_visit_non_local.loc[df_why_visit_non_local['How far do you travel to get to the Park?'] != '1 - 5 miles away']
df_why_visit_non_local = df_why_visit_non_local.loc[df_why_visit_non_local['How far do you travel to get to the Park?'] != '6 - 9 miles away']

#cleaning data to find counts of reasons why non-local people visit the park
outdoor_count_non_local = df_why_visit_non_local["Why do you visit the Park? (check all that apply)"].str.count("Spend time in an outdoor green space")
outdoor_count_non_local = outdoor_count_non_local.sum()

exercise_count_non_local = df_why_visit_non_local["Why do you visit the Park? (check all that apply)"].str.count("Exercise")
exercise_count_non_local = exercise_count_non_local.sum()

parthenon_count_non_local = df_why_visit_non_local["Why do you visit the Park? (check all that apply)"].str.count("Visit the Parthenon")
parthenon_count_non_local = parthenon_count_non_local.sum()

arts_center_count_non_local = df_why_visit_non_local["Why do you visit the Park? (check all that apply)"].str.count("Visit Centennial Arts Center")
arts_center_count_non_local = arts_center_count_non_local.sum()

performing_studios_count_non_local = df_why_visit_non_local["Why do you visit the Park? (check all that apply)"].str.count("Visit Centennial Performing Arts Studios")
performing_studios_count_non_local = performing_studios_count_non_local.sum()

events_count_non_local = df_why_visit_non_local["Why do you visit the Park? (check all that apply)"].str.count("Attend events")
events_count_non_local = events_count_non_local.sum()

picnic_count_non_local = df_why_visit_non_local["Why do you visit the Park? (check all that apply)"].str.count("Picnic")
picnic_count_non_local = picnic_count_non_local.sum()

walk_dog_count_non_local = df_why_visit_non_local["Why do you visit the Park? (check all that apply)"].str.count("Walk dog")
walk_dog_count_non_local = walk_dog_count_non_local.sum()

dog_park_count_non_local = df_why_visit_non_local["Why do you visit the Park? (check all that apply)"].str.count("Visit the dog park")
dog_park_count_non_local = dog_park_count_non_local.sum()

feed_ducks_count_non_local = df_why_visit_non_local["Why do you visit the Park? (check all that apply)"].str.count("Feed the ducks")
feed_ducks_count_non_local = feed_ducks_count_non_local.sum()

playground_count_non_local = df_why_visit_non_local["Why do you visit the Park? (check all that apply)"].str.count("Visit the playground")
playground_count_non_local = playground_count_non_local.sum()

volleyball_count_non_local = df_why_visit_non_local["Why do you visit the Park? (check all that apply)"].str.count("Use the volleyball courts")
volleyball_count_non_local = volleyball_count_non_local.sum()

sports_count_non_local = df_why_visit_non_local["Why do you visit the Park? (check all that apply)"].str.count("Play sports")
sports_count_non_local = sports_count_non_local.sum()

why_visit_data_non_local = [["Spend time in an outdoor green space", outdoor_count_non_local],["Excercise", exercise_count_non_local], ["Visit the Parthenon", parthenon_count_non_local], ["Visit Centennial Arts Center", arts_center_count_non_local], ["Visit Centennial Performing Arts Studios", performing_studios_count_non_local], ["Attend events", events_count_non_local], ["Picnic", picnic_count_non_local], ["Walk dog", walk_dog_count_non_local], ["Visit the dog park", dog_park_count_non_local], ["Feed the ducks", feed_ducks_count_non_local], ["Visit the playground", playground_count_non_local], ["Use the volleyball courts", volleyball_count_non_local], ["Play sports", sports_count_non_local]]
df_why_visit_count_non_local = pd.DataFrame(why_visit_data_non_local, columns=["Reason", "Count"])

fig_bar_non_local = px.bar(df_why_visit_count_non_local, x="Reason", y="Count", title="Why Non-local People Visit Centennial Park", text_auto=True, color="Reason")
fig_bar_non_local.update_layout(xaxis={'categoryorder':'total descending'}) 


app.layout = html.Div([
    html.H1('CPC Dashboard Rough Draft - Maya'),
    dcc.Dropdown(
        id = 'graph-type',
        placeholder='Select graph type',
        options= [
            {'label' : 'All Locals', 'value' : 'all_locals'},
            {'label' : 'Local Members', 'value' : 'local_members'},
            {'label' : 'Local Non-Members', 'value': 'local_non_members'}
        ]
    ),
    dcc.Graph(id='graph'),
    
    dcc.Dropdown(
        id = 'graph-type2',
        placeholder='Select graph type',
        options= [
            {'label' : 'All Visitors', 'value' : 'all_people'},
            {'label' : 'Local Visitors', 'value' : 'local_people'},
            {'label' : 'Non-local Visitors', 'value': 'non_local_people'}
        ]
    ),
    dcc.Graph(id='graph2')
])

#callback for pie chart based on local membership
@app.callback(
    Output('graph', 'figure'),
    [Input('graph-type', 'value')]
)
def choose_graph_type(graph_type):
    if graph_type is None:
        raise dash.exceptions.PreventUpdate()
    if graph_type == 'all_locals':
        return fig_pie
    elif graph_type == 'local_members':
        return fig_pie_members
    elif graph_type == 'local_non_members':
        return fig_pie_non_members
    return None

#callback for bar chart based on local/non-local
@app.callback(
    Output('graph2', 'figure'),
    [Input('graph-type2', 'value')]
)
def choose_graph_type2(graph_type2):
    if graph_type2 is None:
        raise dash.exceptions.PreventUpdate()
    if graph_type2 == 'all_people':
        return fig_bar
    elif graph_type2 == 'local_people':
        return fig_bar_local
    elif graph_type2 == 'non_local_people':
        return fig_bar_non_local
    return None



if __name__ == '__main__':
    app.run_server(mode="external")


# In[ ]:





# In[ ]:





# In[ ]:




