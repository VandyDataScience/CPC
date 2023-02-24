from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px

app = Dash(__name__)

# upload data 
df = pd.read_csv('CentennialReal.csv')

# extract only the locals from the data frame
local = df.loc[(df["How far do you travel to get to the Park?"]=="Less than a mile away") | (df["How far do you travel to get to the Park?"]=="6 - 9 miles away") | (df["How far do you travel to get to the Park?"]=="1 - 5 miles away")]

# create subsest with just local memebers
localMems = local.loc[(local["Are you a member of Centennial Park Conservancy?"] == "Yes")]

# create subset with just local nonmebers
localNonMems = local.loc[(local["Are you a member of Centennial Park Conservancy?"] == "No")]

# function that creates a pie chart based on the given percentages of benefitting from ongoing services in a subset
def createChart(subset, name):
    count = subset["Do you believe the Park could benefit from more ongoing activities or services?"].value_counts()
    dff = pd.DataFrame()
    dff["names"] = [str(i) for i in count.index]
    dff["number"] = count.values
    fig_pie = px.pie(dff, values="number", names="names", title=f"Percentage of {name} that Believe the Park Could Benefit from More Ongoing Activities")
    return fig_pie.show() # this opens up a new page rather than showing it on the same page 

# add a drop down and graph to the host
app.layout = html.Div([
    html.H3("Subset of Locals"),
    dcc.Dropdown(["Local Members", "Local Nonmembers", "All Locals"], "All Locals", id = "subset-dropdown"),
    html.Div(id="dropdown-container"), 
    
    dcc.Graph(id="pie-chart")
])

@app.callback (
    Output('pie-chart', 'figure'),
    Input('subset-dropdown', 'value')
)

# update the graph based on dropdown selection
def update_output(value):
    if value == "All Locals":
        createChart(local, value)
    elif value == "Local Nonmembers":
        createChart(localNonMems, value)
    else:
        createChart(localMems, value)

if __name__ == "__main__":
    app.run_server(debug=True)