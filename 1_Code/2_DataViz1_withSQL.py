# -*- coding: utf-8 -*-
"""
@author: wraithrune

Data Visual 1 - Interactive Dashbord of Bar chart - Country Level Statistics
Linked to SQL Database instead of loading

Load in Pre-Processed Data: population_by_country_2020.csv

Reference
1.	Population by Country – 2020: https://www.kaggle.com/datasets/tanuprabhu/population-by-country-2020?resource=download 

Using Pandas Library
"""

# Step 1 - Import Dash, Pandas, Plotly
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

# Step 2 - Database connection configuration
db_config = {
    'user': 'weaver', 
    'password': 'web101SG',  
    'host': 'localhost',
    'database': 'dbsingaporepoly', 
}

# Step 3 - Create the SQLAlchemy engine
engine = create_engine(f"mysql+mysqlconnector://{db_config['user']}:{db_config['password']}@{db_config['host']}/{db_config['database']}")

# Step 4 - Query to load the processed data from the MySQL table
query = "SELECT * FROM population_by_country_2020"

# Step 5 - Load the data into a pandas DataFrame
vPopData = pd.read_sql(query, engine)

# Step 6 - Remove rows with 'NA' values in important columns
vPopData = vPopData.dropna(subset=['Population (2020)', 'Fert. Rate', 'Migrants (net)', 'Med. Age', 'Urban Pop %', 'World Share'])

# Step 7 - Initialize the Dash app
app = dash.Dash(__name__)

# Step 8 - Retrieve unique countries
all_countries = vPopData['Country (or dependency)'].unique()

# Step 9 - Setup the Web App
app.layout = html.Div([
    html.H1("Country Statistics Dashboard"),
    
    dcc.Dropdown(
        id='attribute-dropdown',
        options=[
            {'label': 'Population (2020)', 'value': 'Population (2020)'},
            {'label': 'Fertility Rate', 'value': 'Fert. Rate'},
            {'label': 'Migrants (net)', 'value': 'Migrants (net)'},
            {'label': 'Median Age', 'value': 'Med. Age'},
            {'label': 'Urban Pop %', 'value': 'Urban Pop %'},
            {'label': 'World Share', 'value': 'World Share'}
        ],
        value='Med. Age',  
        clearable=False
    ),
    
    dcc.Checklist(
        id='country-checklist',
        options=[{'label': country, 'value': country} for country in all_countries],
        value=all_countries[:20], 
        inline=True
    ),
    
    dcc.Graph(id='bar-chart')
])

# Step 10 - Setup the callback to update the bar chart
@app.callback(
    Output('bar-chart', 'figure'),
    [Input('attribute-dropdown', 'value'),
     Input('country-checklist', 'value')]
)

# Step 11 - Setup function to update bar chart
def update_bar_chart(selected_attribute, selected_countries):
    # Filter the data to include only the selected countries
    vPopData_filtered = vPopData[vPopData['Country (or dependency)'].isin(selected_countries)]
    
    # Sort the data by the selected attribute in ascending order
    vPopData_sorted = vPopData_filtered.sort_values(by=selected_attribute, ascending=True)
    
    # Create a bar chart
    fig = px.bar(vPopData_sorted, x='Country (or dependency)', y=selected_attribute, 
                 color='Country (or dependency)', title=f'{selected_attribute} for Selected Countries')
    
    fig.update_layout(xaxis_title="Country", yaxis_title=selected_attribute, showlegend=False)
    
    return fig

# Step 12 - RUn the app
if __name__ == '__main__':
    app.run_server(debug=True)
