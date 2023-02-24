from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px

app = Dash(__name__)

# upload data
df = pd.read_csv('CentennialReal.csv')

# extract only the locals from the data frame
local = df.loc[(df["How far do you travel to get to the Park?"]=="Less than a mile away") | (df["How far do you travel to get to the Park?"]=="6 - 9 miles away") | (df["How far do you travel to get to the Park?"]=="1 - 5 miles away")]

# create a subset of members
members = local.loc[(local["Are you a member of Centennial Park Conservancy?"]=="Yes")]

# create a subset of nonmembers
nonmembers = local.loc[(local["Are you a member of Centennial Park Conservancy?"]=="No")]

# calculate what different subsets want to see for activities
serviceTypeAll = local["If yes, which activities or services would you most like to see? (select all that apply)"].squeeze()

serviceTypeMembers = members["If yes, which activities or services would you most like to see? (select all that apply)"].squeeze()

serviceTypeNonmembers = nonmembers["If yes, which activities or services would you most like to see? (select all that apply)"].squeeze()

# add a dropdown and a graph to the host 
app.layout = html.Div([
    html.H3("Subset of Locals"),
    dcc.Dropdown(["Local Members", "Local Nonmembers", "All Locals"], "All Locals", id = "subset-dropdown"),
    html.Div(id="dropdown-container"), 
    
    dcc.Graph(id="services-bar")
])

@app.callback (
    #Output('dropdown-container', 'children'),
    Output("services-bar", "figure"),
    Input("subset-dropdown", "value")
)

# logic to determine which graph should be displayed
def update_output(value):
    if value == "All Locals":
        createGraph(serviceTypeAll, value)
    elif value == "Local Nonmembers":
        createGraph(serviceTypeNonmembers, value)
    else:
        createGraph(serviceTypeMembers, value)

# count how many of a specific response exist in a given subset
def countItem(item, subset):
    series = subset.str.contains(item, case=False)
    count = 0; 
    for i in series:
        if (i == True): 
            count +=1
    return count

# create a bar graph based on the subset of responses 
def createGraph(subset, name):
    events = countItem("Event", subset)
    foodBev = countItem("More food and beverage options", subset)
    restroom = countItem("public restrooms", subset)
    tours = countItem("Walking/golf cart tours", subset)
    carousel = countItem("Carousel", subset)
    safety = countItem("safety", subset)
    concerts = countItem("concerts", subset)
    doggyBag = countItem("doggy bag dispensers", subset)
    trees = countItem("more trees", subset)
    sustainableLandscaping = countItem("sustainable landscaping", subset)

    dff = pd.DataFrame({'lab':['Events', 'More Food and Beverages', 'Public Restrooms', 'Tours', 'Carousel', 'More Safety', 'Concerts', 'Doggy Bag Dispensers', 'More Trees', 'Sustainable Landscaping'], 'val':[events, foodBev, restroom, tours, carousel, safety, concerts, doggyBag, trees, sustainableLandscaping]})

    fig_bar = px.bar(dff, x='lab', y='val', title=f'Activities or Services that {name} Want to See More Of', labels={
                         "lab": "Type of Service",
                         "val": "Number of People",
                     },)
    return fig_bar.show() # this does not actually update the page but opens up a new page


if __name__ == '__main__':
    app.run_server(debug=True)