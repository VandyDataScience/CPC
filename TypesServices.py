import pandas as pd
import plotly.express as px

df = pd.read_csv('CentennialReal.csv')

local = df.loc[(df["How far do you travel to get to the Park?"]=="Less than a mile away") | (df["How far do you travel to get to the Park?"]=="6 - 9 miles away") | (df["How far do you travel to get to the Park?"]=="1 - 5 miles away")]

serviceTypeSeries = local["If yes, which activities or services would you most like to see? (select all that apply)"].squeeze()
print(serviceTypeSeries)

def countItem(item):
    series = serviceTypeSeries.str.contains(item, case=False)
    count = 0; 
    for i in series:
        if (i == True): 
            count +=1
    print(count)
    return count

events = countItem("Event")
foodBev = countItem("More food and beverage options")
restroom = countItem("public restrooms")
tours = countItem("Walking/golf cart tours")
carousel = countItem("Carousel")
safety = countItem("safety")
concerts = countItem("concerts")
doggyBag = countItem("doggy bag dispensers")
trees = countItem("more trees")
sustainableLandscaping = countItem("sustainable landscaping")

dff = pd.DataFrame({'lab':['Events', 'More Food and Beverages', 'Public Restrooms', 'Tours', 'Carousel', 'More Safety', 'Concerts', 'Doggy Bag Dispensers', 'More Trees', 'Sustainable Landscaping'], 'val':[events, foodBev, restroom, tours, carousel, safety, concerts, doggyBag, trees, sustainableLandscaping]})

fig_bar = px.bar(dff, x='lab', y='val', title='Activities or Services that Locals Want to See More Of', labels={
                     "lab": "Type of Service",
                     "val": "Number of People",
                 },)
fig_bar.show()

