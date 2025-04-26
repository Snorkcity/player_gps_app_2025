import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import pandas as pd
import os

# source file running it at home
# source_file = r'C:\Users\scott\OneDrive\NPLW-25\Data analytics\GPS\2025-Belconnen-NPLW-data.xlsx'

# Source file for web
# source_file = '2025-Belconnen-NPLW-data.xlsx'

# local
# source_file = r'C:\Users\scott\OneDrive\NPLW-25\Data analytics\GPS\2025-Belconnen-NPLW-data.xlsx'
# internet
source_file = '2025-Belconnen-NPLW-data.xlsx'


df = pd.read_excel(source_file, sheet_name='individual stats')

# Initialize the Dash app with a dark theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

# Updated layout with player-centric focus
app.layout = dbc.Container([
    # Header Banner with Logo on the Far Left
    dbc.Row(
        dbc.Col(html.Div([
            html.Img(src='/assets/test-clublogo.png', style={'height': '70px', 'margin-right': '20px'}),
            html.H1("2025 NPLW - GPS - Player-data", 
                    className='text-center text-white',
                    style={'font-family': 'Roboto', 'font-size': '36px', 'color': '#FFFFFF', 
                           'background': 'linear-gradient(to right, #000080, #87CEEB)',  # Gradient from navy to sky blue
                           'padding': '15px 30px', 'border-radius': '5px', 'flex-grow': '1'})
        ], style={'display': 'flex', 'align-items': 'center', 'justify-content': 'flex-start', 'background-color': '#000080', 'border-radius': '5px'}), width=12)
    ),

    # Add Spacing Between Banner and Charts
    html.Br(),

    # Player Selection Layout
    html.Div(children=[
        # Player Dropdown
        dcc.Dropdown(
            id='player-dropdown',
            options=[{'label': player, 'value': player} for player in sorted(df['Player Name'].unique())],
            placeholder='Select a Player',
            style={'width': '300px', 'color': 'black'}
        ),
        
        # Update Button
        html.Button(
            'Update Chart', 
            id='update-button', 
            className='btn btn-primary', 
            style={'marginLeft': '10px'}
        ),
    ], style={
        'display': 'flex',
        'justify-content': 'center',
        'align-items': 'center',
        'gap': '10px',
        'marginBottom': '20px'
    }),

    html.Br(),  # Adds a line break for spacing

    # Sprint Distance Chart
    dbc.Row([
        dbc.Col([
            # Segmented Control for sorting options specific to the Sprint Distance chart
            dbc.ButtonGroup(
                [
                    dbc.Button("Round Order", id="sprint-btn-date", n_clicks=0, color="primary", active=True),
                    dbc.Button("Lowest to Highest", id="sprint-btn-value", n_clicks=0, color="primary"),
                    dbc.Button("Form (Last 5 Rounds)", id="sprint-btn-form", n_clicks=0, color="primary"),
                ],
                size="sm",
                style={"margin-bottom": "10px"}
            ),
            dcc.Graph(id='sprint-distance-chart'),
        ], width=12)
    ], style={'margin-bottom': '30px'}),

    html.Br(),  # Adds a line break for spacing
    html.Br(),  # Adds a line break for spacing
    html.Br(),  # Adds a line break for spacing


    # Power Plays chart
    dbc.Row([
        dbc.Col([
            # Segmented Control for sorting options specific to the Power Plays chart
            dbc.ButtonGroup(
                [
                    dbc.Button("Round Order", id="btn-date", n_clicks=0, color="primary", active=True),
                    dbc.Button("Lowest to Highest", id="btn-value", n_clicks=0, color="primary"),
                    dbc.Button("Form (Last 5 Rounds)", id="btn-form", n_clicks=0, color="primary"),
                ],
                size="sm",
                style={"margin-bottom": "10px"}
            ),
            dcc.Graph(id='power-plays-chart'),
        ], width=12)
    ], style={'margin-bottom': '30px'}),

    html.Br(),  # Adds a line break for spacing
    html.Br(),  # Adds a line break for spacing
    html.Br(),  # Adds a line break for spacing

    # Player Load Chart Layout
    dbc.Row([
        dbc.Col([
            # Segmented Control for Player Load chart
            dbc.ButtonGroup(
                [
                    dbc.Button("Round Order", id="btn-player-load-date", n_clicks=0, color="primary", active=True),
                    dbc.Button("Lowest to Highest", id="btn-player-load-value", n_clicks=0, color="primary"),
                    dbc.Button("Form (Last 5 Rounds)", id="btn-player-load-form", n_clicks=0, color="primary"),
                ],
                size="sm",
                style={"margin-bottom": "10px"}
            ),
            dcc.Graph(id='player-load-chart'),
        ], width=12)
    ], style={'margin-bottom': '30px'}),

    html.Br(),  # Adds a line break for spacing
    html.Br(),  # Adds a line break for spacing
    html.Br(),  # Adds a line break for spacing

    # Top Speed Chart Layout
    dbc.Row([
        dbc.Col([
            # Segmented Control for Top Speed chart
            dbc.ButtonGroup(
                [
                    dbc.Button("Round Order", id="btn-top-speed-date", n_clicks=0, color="primary", active=True),
                    dbc.Button("Lowest to Highest", id="btn-top-speed-value", n_clicks=0, color="primary"),
                    dbc.Button("Form (Last 5 Rounds)", id="btn-top-speed-form", n_clicks=0, color="primary"),
                ],
                size="sm",
                style={"margin-bottom": "10px"}
            ),
            dcc.Graph(id='top-speed-chart'),
        ], width=12)
    ], style={'margin-bottom': '30px'}),


    html.Br(),  # Adds a line break for spacing
    html.Br(),  # Adds a line break for spacing
    html.Br(),  # Adds a line break for spacing

    # Distance Per Min Chart
    dbc.Row([
        dbc.Col([
            # Segmented Control for sorting options specific to the Distance Per Min chart
            dbc.ButtonGroup(
                [
                    dbc.Button("Round Order", id="btn-dpm-date", n_clicks=0, color="primary"),
                    dbc.Button("Lowest to Highest", id="btn-dpm-value", n_clicks=0, color="primary"),
                    dbc.Button("Form (Last 5 Rounds)", id="btn-dpm-form", n_clicks=0, color="primary"),
                ],
                size="sm",
                style={"margin-bottom": "10px"}
            ),
            dcc.Graph(id='distance-per-min-chart'),
        ], width=12)
    ], style={'margin-bottom': '30px'}),

    html.Br(),  # Adds a line break for spacing
    html.Br(),  # Adds a line break for spacing
    html.Br(),  # Adds a line break for spacing


    # Accelerations and Decelerations Chart Layout
dbc.Row([
    dbc.Col([
        # Segmented Control for Accel/Decel chart
        dbc.ButtonGroup(
            [
                dbc.Button("Round Order", id="btn-accel-decel-date", n_clicks=0, color="primary", active=True),
                dbc.Button("Lowest to Highest", id="btn-accel-decel-value", n_clicks=0, color="primary"),
                dbc.Button("Form (Last 5 Rounds)", id="btn-accel-decel-form", n_clicks=0, color="primary"),
            ],
            size="sm",
            style={"margin-bottom": "10px"}
        ),
        dcc.Graph(id='accel-decel-chart'),
    ], width=12)
], style={'margin-bottom': '30px'}),

html.Br(),  # Adds a line break for spacing
html.Br(),  # Adds a line break for spacing
html.Br(),  # Adds a line break for spacing
], fluid=True)  # Ensure this properly closes the layout


# end of layout section

# start of chart section

def create_power_plays_chart(df_filtered, selected_player, sort_order):
    # Filter data for Power Plays from the 'game' split
    df_power_plays = df_filtered[df_filtered['Split Name'] == 'game'][['Player Name', 'Round', 'Date', 'Power Plays', 'Mins played']]

    # Calculate the Power Plays per 10 minutes
    df_power_plays['PP per 10min'] = ((df_power_plays['Power Plays'] / df_power_plays['Mins played']) * 10).replace([float('inf'), -float('inf')], 0).fillna(0).round(0).astype(int)

    # Sort by Date for default order, or by value if specified
    if sort_order == 'date':
        df_power_plays = df_power_plays.sort_values(by=['Date'])
    elif sort_order == 'value':
        df_power_plays = df_power_plays.sort_values('Power Plays', ascending=True)
    elif sort_order == 'form':
        df_power_plays = df_power_plays.sort_values(by='Date', ascending=False).head(5).sort_values(by='Date', ascending=True)
        
    # Create Plotly line chart
    fig = go.Figure(data=[
        go.Scatter(
            x=df_power_plays['Round'],  # Display Rounds on the x-axis
            y=df_power_plays['Power Plays'],
            mode='lines+markers',
            line=dict(color='#0000FF', width=3),  # Strong blue line with width 3
            marker=dict(size=8),  # Larger markers for better visibility
            hoverinfo='text',
            hovertext=[
                f"Round: {round_name}<br>Date: {date}<br>Power Plays: {int(float(val) or 0)} PP<br>PP per 10min: {int(float(pp_per_10min) or 0)}<br>Mins Played: {int(float(mins) or 0)} min"
                for round_name, date, val, pp_per_10min, mins in zip(
                    df_power_plays['Round'],
                    df_power_plays['Date'].dt.strftime('%d-%m-%Y'),  # Format date as needed
                    df_power_plays['Power Plays'],
                    df_power_plays['PP per 10min'],
                    df_power_plays['Mins played']  # Total minutes played
                )
            ]

        )
    ])
    
    # Update layout for a clean look and consistent title styling
    fig.update_layout(
        title={
            'text': f'<b>Power Plays - {selected_player}</b>',
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'size': 24, 'family': 'Roboto', 'color': 'white'}  # Consistent title styling
        },
        xaxis_title='Round',
        yaxis_title='Power Plays',
        plot_bgcolor='#1e1e1e',
        paper_bgcolor='#1e1e1e',
        font=dict(color='white', family='Roboto'),
        xaxis=dict(
            showline=True,
            showgrid=False,
            tickfont=dict(family='Roboto', size=12, color='white')
        ),
        yaxis=dict(
            showline=True,
            gridcolor='gray',
            zeroline=True,
            showgrid=True,
            tickfont=dict(family='Roboto', size=12, color='white')
        ),
        margin=dict(l=40, r=40, t=40, b=40)  # Adjust margins as needed
    )

    return fig

# Updated Function to create the Sprint Distance Chart
def create_sprint_distance_chart(df_filtered, selected_player, sort_order):
    # Filter data for 1st half, 2nd half, and game splits
    df_1st_half = df_filtered[df_filtered['Split Name'] == '1st.half'][['Round', 'Date', 'Sprint Distance (m)', 'Mins played']]
    df_2nd_half = df_filtered[df_filtered['Split Name'] == '2nd.half'][['Round', 'Date', 'Sprint Distance (m)', 'Mins played']]
    df_game = df_filtered[df_filtered['Split Name'] == 'game'][['Round', 'Date', 'Sprint Distance (m)', 'Mins played']]

    # Rename columns to distinguish between halves
    df_1st_half = df_1st_half.rename(columns={'Sprint Distance (m)': 'Sprint Distance (m) 1st Half', 'Mins played': 'Mins played 1st Half'})
    df_2nd_half = df_2nd_half.rename(columns={'Sprint Distance (m)': 'Sprint Distance (m) 2nd Half', 'Mins played': 'Mins played 2nd Half'})

    # Merge 1st and 2nd half data on 'Round' and 'Date'
    df_sprint = pd.merge(df_1st_half, df_2nd_half, on=['Round', 'Date'], how='outer')

    # Merge total minutes played from the game split
    df_sprint = pd.merge(df_sprint, df_game[['Round', 'Date', 'Mins played']], on=['Round', 'Date'], how='left')
    df_sprint = df_sprint.rename(columns={'Mins played': 'Total Mins played'})

    # Calculate total sprint distance and averages for hover
    df_sprint['Total Sprint Distance'] = df_sprint['Sprint Distance (m) 1st Half'].fillna(0) + df_sprint['Sprint Distance (m) 2nd Half'].fillna(0)
    df_sprint['Avg per min 1st Half'] = (df_sprint['Sprint Distance (m) 1st Half'] / df_sprint['Mins played 1st Half']).fillna(0).astype(int)
    df_sprint['Avg per min 2nd Half'] = (df_sprint['Sprint Distance (m) 2nd Half'] / df_sprint['Mins played 2nd Half']).fillna(0).astype(int)
    df_sprint['Total Avg per min'] = (df_sprint['Total Sprint Distance'] / df_sprint['Total Mins played']).fillna(0).astype(int)

    # Sorting based on the selected sort order

    if sort_order == 'value':
        df_sprint = df_sprint.sort_values('Total Sprint Distance', ascending=True)
    elif sort_order == 'form':
        # Filter the 'game' split data and sort by date to get the last 5 rounds
        df_sprint = df_sprint.sort_values(by='Date', ascending=False).drop_duplicates(subset=['Round']).head(5).sort_values(by='Date')
    else:  # Default is to sort by date
        df_sprint = df_sprint.sort_values(by='Date', ascending=True)

    # Create the stacked bar chart
    fig = go.Figure(data=[
        go.Bar(
            name='1st Half',
            x=df_sprint['Round'],
            y=df_sprint['Sprint Distance (m) 1st Half'],
            marker_color='#87CEEB',  # Sky blue
            hoverinfo='text',
            hovertext=[
                f"1st Half Sprint Distance: {int(float(val) or 0)} m<br>"
                f"1st Half Minutes: {int(float(mins) or 0)} min<br>"
                f"Avg per min: {int(float(avg_per_min) or 0)} m/min<br>"
                f"Total Sprint Distance: {int(float(total) or 0)} m"
                for val, mins, avg_per_min, total in zip(
                    df_sprint['Sprint Distance (m) 1st Half'].fillna(0), 
                    df_sprint['Mins played 1st Half'].fillna(0), 
                    df_sprint['Avg per min 1st Half'].fillna(0), 
                    df_sprint['Total Sprint Distance'].fillna(0)
                )
            ]

        ),
        go.Bar(
            name='2nd Half',
            x=df_sprint['Round'],
            y=df_sprint['Sprint Distance (m) 2nd Half'],
            marker_color='#000080',  # Navy blue
            hoverinfo='text',
            hovertext=[
                f"2nd Half Sprint Distance: {int(float(val) or 0)} m<br>"
                f"2nd Half Minutes: {int(float(mins) or 0)} min<br>"
                f"2nd Half Avg per min: {int(float(avg_per_min) or 0)} m/min<br>"
                f"Total Sprint Distance: {int(float(total) or 0)} m<br>"
                f"Total Minutes Played: {int(float(total_mins) or 0)} min<br>"
                f"Total Avg per min: {int(float(total_avg_per_min) or 0)} m/min"
                for val, mins, avg_per_min, total, total_mins, total_avg_per_min in zip(
                    df_sprint['Sprint Distance (m) 2nd Half'].fillna(0), 
                    df_sprint['Mins played 2nd Half'].fillna(0), 
                    df_sprint['Avg per min 2nd Half'].fillna(0), 
                    df_sprint['Total Sprint Distance'].fillna(0), 
                    df_sprint['Total Mins played'].fillna(0), 
                    df_sprint['Total Avg per min'].fillna(0)
                )
            ]

        )
    ])

    # Update layout with dark theme and professional styling
    fig.update_layout(
        barmode='stack',
        title={
            'text': f'<b>Sprint Distance - 1st Half vs 2nd Half - {selected_player}</b>',
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'size': 24, 'family': 'Roboto', 'color': 'white'}
        },
        xaxis_title='Round',
        yaxis_title='Sprint Distance (m)',
        xaxis=dict(
            showline=True,
            showgrid=False,
            showticklabels=True,
            linecolor='white',
            linewidth=2,
            ticks='outside',
            tickfont=dict(family='Roboto', size=14, color='white')
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor='gray',
            zeroline=True,
            showline=True,
            linewidth=2,
            linecolor='white',
            tickfont=dict(family='Roboto', size=14, color='white')
        ),
        plot_bgcolor='#1e1e1e',  # Dark theme background for the plot area
        paper_bgcolor='#1e1e1e', # Dark theme background for the entire page
        legend=dict(
            x=0.8,
            y=1.1,
            bgcolor='rgba(0, 0, 0, 0)',
            bordercolor='rgba(0, 0, 0, 0)',
            font=dict(family='Roboto', size=12, color='white')
        ),
        margin=dict(l=20, r=20, t=60, b=20)  # Tighter margins for a clean look
    )
    return fig


# Function to create the Distance Per Min Chart for the player-centric view
def create_distance_per_min_chart(df_filtered, selected_player, sort_order):
    # Filter data for 1st half, 2nd half, and game with 'Split Name' included
    df_1st_half = df_filtered[df_filtered['Split Name'] == '1st.half'][['Round', 'Date', 'Split Name', 'Distance Per Min (m/min)']]
    df_2nd_half = df_filtered[df_filtered['Split Name'] == '2nd.half'][['Round', 'Date', 'Split Name', 'Distance Per Min (m/min)']]
    df_game = df_filtered[df_filtered['Split Name'] == 'game'][['Round', 'Date', 'Split Name', 'Distance Per Min (m/min)', 'Mins played']]

    # Merge data for Distance Per Min, ensuring 'Split Name' is retained
    df_distance_per_min = pd.merge(
        df_1st_half,
        df_2nd_half,
        on=['Round', 'Date'],
        suffixes=(' 1st Half', ' 2nd Half')
    )

    df_distance_per_min = pd.merge(
        df_distance_per_min, 
        df_game, 
        on=['Round', 'Date'], 
        how='outer'
    )

    df_distance_per_min = df_distance_per_min.rename(columns={'Distance Per Min (m/min)': 'Game'})

    # Default order is chronological
    df_distance_per_min = df_distance_per_min.sort_values('Date', ascending=True)

    # Apply sorting based on the selected sort order
    if sort_order == 'value':
        df_distance_per_min = df_distance_per_min.sort_values('Game', ascending=True)  # Sort lowest to highest
    elif sort_order == 'form':
        # Ensure 'Split Name' is present and filter for 'game'
        df_distance_per_min_form = df_distance_per_min[df_distance_per_min['Split Name'] == 'game']
        df_distance_per_min = df_distance_per_min_form.sort_values(by='Date', ascending=False).head(5)
        df_distance_per_min = df_distance_per_min.sort_values(by='Date', ascending=True)  # Most recent on the right

    # Handle NaN values to prevent conversion errors
    df_distance_per_min = df_distance_per_min.fillna(0)

    # Create a bar chart for the total game values only
    fig = go.Figure(data=[
        go.Bar(
            name='Game',
            x=df_distance_per_min['Round'],
            y=df_distance_per_min['Game'],
            marker_color='#1E90FF',  # Dark blue for total game
            hoverinfo='text',
            hovertext=[
                f"Total: {int(game)} m/min<br>2nd Half: {int(second_half)} m/min<br>1st Half: {int(first_half)} m/min<br>Mins Played: {int(total_mins)} min"
                for game, second_half, first_half, total_mins in zip(
                    df_distance_per_min['Game'], 
                    df_distance_per_min.get(f'Distance Per Min (m/min) 2nd Half', 0),
                    df_distance_per_min.get(f'Distance Per Min (m/min) 1st Half', 0),
                    df_distance_per_min['Mins played']
                )
            ]
        )
    ])

    # Update layout with professional styling
    fig.update_layout(
        title={
            'text': f'<b>Distance Per Min - {selected_player}</b>',
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'size': 24, 'family': 'Roboto', 'color': 'white'}
        },
        xaxis_title='Round',
        yaxis_title='Distance Per Min (m/min)',
        plot_bgcolor='#1e1e1e',
        paper_bgcolor='#1e1e1e',
        font=dict(color='white', family='Roboto'),
        xaxis=dict(
            showline=True,
            showgrid=False,
            tickfont=dict(family='Roboto', size=12, color='white')
        ),
        yaxis=dict(
            showline=True,
            gridcolor='gray',
            zeroline=True,
            showgrid=True,
            tickfont=dict(family='Roboto', size=12, color='white')
        ),
        margin=dict(l=40, r=40, t=40, b=40),
        legend=dict(
            x=0.8,
            y=1.1,
            bgcolor='rgba(0, 0, 0, 0)',
            bordercolor='rgba(0, 0, 0, 0)',
            font=dict(family='Roboto', size=12, color='white')
        )
    )

    return fig

# Updated Function to create the Top Speed Chart for player-centric view
def create_top_speed_chart(df_filtered, selected_player, sort_order):
    try:
        # Extract data for each half and game
        df_1st_half = df_filtered[df_filtered['Split Name'] == '1st.half'][['Round', 'Top Speed (m/s)', 'Date']]
        df_2nd_half = df_filtered[df_filtered['Split Name'] == '2nd.half'][['Round', 'Top Speed (m/s)', 'Date']]
        df_game = df_filtered[df_filtered['Split Name'] == 'game'][['Round', 'Top Speed (m/s)', 'Mins played', 'Date']]
        
        # Rename columns to prevent overlap during merging
        df_1st_half = df_1st_half.rename(columns={'Top Speed (m/s)': 'Top Speed (m/s) 1st Half', 'Date': 'Date 1st Half'})
        df_2nd_half = df_2nd_half.rename(columns={'Top Speed (m/s)': 'Top Speed (m/s) 2nd Half', 'Date': 'Date 2nd Half'})
    except KeyError as e:
        print(f"Error: Missing column {e} in the DataFrame.")
        return

    # Merge data for Top Speed
    df_top_speed = pd.merge(
        df_1st_half,
        df_2nd_half,
        on='Round',
        how='outer'
    )
    df_top_speed = pd.merge(df_top_speed, df_game, on='Round', how='left')

    for col in ['Mins played', 'Mins played 1st Half', 'Mins played 2nd Half', 'Total Mins played']:
        if col in df_top_speed.columns:
            df_top_speed[col] = pd.to_numeric(df_top_speed[col], errors='coerce').fillna(0).astype(int)

    # Ensure column names are correctly inferred
    df_top_speed = df_top_speed.infer_objects(copy=False)

    # Apply sorting based on the selected option
    if sort_order == 'form':
        # Sort by date to get the most recent 5 rounds, then sort those by date ascending
        df_top_speed = df_top_speed.sort_values(by='Date', ascending=False).head(5).sort_values(by='Date', ascending=True)
    elif sort_order == 'value':
        # Sort by the Top Speed value from the game data (Split Name = 'game')
        df_top_speed = df_top_speed.sort_values(by='Top Speed (m/s)', ascending=True)
    else:
        # Default sort by Date in ascending order
        df_top_speed = df_top_speed.sort_values(by='Date', ascending=True)

    # Debugging: Check data order
    print("Top Speed Data Sorted by:", df_top_speed[['Round', 'Top Speed (m/s)', 'Date']].to_string(index=False))

    # Create the bar chart
    fig = go.Figure(data=[
        go.Bar(
            name='1st Half',
            x=df_top_speed['Round'],
            y=df_top_speed['Top Speed (m/s) 1st Half'],
            marker_color='#87CEEB',  # Sky blue
            hoverinfo='text',
            hovertext=[
                f"1st Half: {speed_1st:.1f} m/s<br>2nd Half: {speed_2nd:.1f} m/s<br>Total Minutes Played: {int(mins) if not pd.isna(mins) else 0} min"
                for speed_1st, speed_2nd, mins in zip(
                    df_top_speed['Top Speed (m/s) 1st Half'],
                    df_top_speed['Top Speed (m/s) 2nd Half'],
                    df_top_speed['Mins played']
                )
            ]
        ),
        go.Bar(
            name='2nd Half',
            x=df_top_speed['Round'],
            y=df_top_speed['Top Speed (m/s) 2nd Half'],
            marker_color='#4682B4',  # Dark blue
            hoverinfo='text',
            hovertext=[
                f"2nd Half: {speed_2nd:.1f} m/s<br>1st Half: {speed_1st:.1f} m/s<br>Total Minutes Played: {int(float(mins) or 0)} min"
                for speed_2nd, speed_1st, mins in zip(
                    df_top_speed['Top Speed (m/s) 2nd Half'],
                    df_top_speed['Top Speed (m/s) 1st Half'],
                    df_top_speed['Mins played']
                )
            ]

        )
    ])

    fig.update_layout(
        barmode='group',
        title={
            'text': 'Top Speed Comparison',
            'font': {'color': 'white'}  # Set the title font color to white
        },
        xaxis_title='Round',
        yaxis_title='Top Speed (m/s)',
        plot_bgcolor='#1e1e1e',
        paper_bgcolor='#1e1e1e',
        font=dict(color='white', family='Roboto'),  # Set the overall font color to white
        xaxis=dict(
            showline=True,
            showgrid=False,
            tickfont=dict(family='Roboto', size=12, color='white')  # Set x-axis labels to white
        ),
        yaxis=dict(
            showline=True,
            gridcolor='gray',
            zeroline=True,
            tickfont=dict(family='Roboto', size=12, color='white')  # Set y-axis labels to white
        )
    )


    return fig

# Updated Function to create the Player Load Chart
def create_player_load_chart(df_filtered, selected_player, sort_order):
    # Filter data for the game split
    df_game = df_filtered[df_filtered['Split Name'] == 'game']

    # Apply sorting based on the selected option
    if sort_order == 'form':
        # Sort by date to get the most recent 5 rounds, then sort those by date ascending
        df_game = df_game.sort_values(by='Date', ascending=False).head(5).sort_values(by='Date', ascending=True)
    elif sort_order == 'date':
        # Sort by Date in ascending order
        df_game = df_game.sort_values(by='Date', ascending=True)
    else:  # 'value' sort order, sort Player Load lowest to highest
        df_game = df_game.sort_values(by='Player Load', ascending=True)

    # Create the line chart
    fig = go.Figure(data=[
        go.Scatter(
            x=df_game['Round'],
            y=df_game['Player Load'],
            mode='lines+markers',
            line=dict(color='#4682B4', width=3),  # Navy blue line
            marker=dict(size=8),  # Larger markers for better visibility
            hoverinfo='text',
            hovertext=[
                f"Round: {round_value}<br>"
                f"Player Load: {int(player_load)}<br>"
                f"Energy: {int(energy)} kcal<br>"
                f"Impacts: {int(impacts)}<br>"
                f"Power Score: {power_score:.1f} w/kg<br>"
                f"Work Ratio: {work_ratio:.1f}<br>"
                f"Total Minutes Played: {int(total_minutes)} min"
                for round_value, player_load, energy, impacts, power_score, work_ratio, total_minutes in zip(
                    df_game['Round'],
                    df_game['Player Load'],
                    df_game['Energy (kcal)'],
                    df_game['Impacts'],
                    df_game['Power Score (w/kg)'],
                    df_game['Work Ratio'],
                    df_game['Mins played']
                )
            ]
        )
    ])

    # Update layout for professional styling
    fig.update_layout(
        title={
            'text': '<b>Player Load Comparison</b>',
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'size': 24, 'family': 'Roboto', 'color': 'white'}
        },
        xaxis_title='Round',
        yaxis_title='Player Load',
        plot_bgcolor='#1e1e1e',
        paper_bgcolor='#1e1e1e',
        font=dict(color='white', family='Roboto'),
        xaxis=dict(
            showline=True,
            showgrid=False,
            tickfont=dict(family='Roboto', size=12, color='white')
        ),
        yaxis=dict(
            showline=True,
            gridcolor='gray',
            zeroline=True,
            tickfont=dict(family='Roboto', size=12, color='white')
        ),
        margin=dict(l=40, r=40, t=40, b=40)
    )

    return fig

# Updated Function to create the Accel/Decel Chart
def create_accel_decel_chart(df_filtered, selected_player, sort_order):
    # Filter data for the game split
    df_game = df_filtered[df_filtered['Split Name'] == 'game']

    # Calculate total accelerations and decelerations >3m/s/s
    acceleration_columns = [
        'Accelerations Zone Count: 3 - 4 m/s/s',
        'Accelerations Zone Count: > 4 m/s/s'
    ]
    deceleration_columns = [
        'Deceleration Zone Count: 3 - 4 m/s/s',
        'Deceleration Zone Count: > 4 m/s/s'
    ]

    # Summing acceleration and deceleration counts before sorting or filtering
    df_game['Total Accelerations >3m/s/s'] = df_game[acceleration_columns].sum(axis=1)
    df_game['Total Decelerations >3m/s/s'] = df_game[deceleration_columns].sum(axis=1)

    # Check if the columns are correctly created
    if 'Total Accelerations >3m/s/s' not in df_game.columns:
        print("Error: 'Total Accelerations >3m/s/s' column not found.")
        return go.Figure()  # Return an empty figure if the column is missing

    # Apply sorting based on the selected option
    if sort_order == 'form':
        # Sort by date to get the most recent 5 rounds, then sort those by date ascending
        df_game = df_game.sort_values(by='Date', ascending=False).head(5).sort_values(by='Date', ascending=True)
    elif sort_order == 'date':
        # Sort by Date in ascending order
        df_game = df_game.sort_values(by='Date', ascending=True)
    else:  # 'value' sort order, sort by total accelerations
        df_game = df_game.sort_values(by='Total Accelerations >3m/s/s', ascending=True)

    # Check if df_game is empty after filtering and sorting
    if df_game.empty:
        print("No data available for the selected sorting order and player.")
        return go.Figure()  # Return an empty figure if there's no data

    # Initialize the figure
    fig = go.Figure(data=[
        go.Bar(
            name='Accelerations',
            x=df_game['Round'],
            y=df_game['Total Accelerations >3m/s/s'],
            marker_color='#1E90FF',  # Dodger blue
            hoverinfo='text',
            hovertext=[
                f"Round: {round_val}<br>Accelerations: {int(val)}"
                for round_val, val in zip(df_game['Round'], df_game['Total Accelerations >3m/s/s'])
            ]
        ),
        go.Bar(
            name='Decelerations',
            x=df_game['Round'],
            y=df_game['Total Decelerations >3m/s/s'],
            marker_color='#6495ED',  # Cornflower blue
            hoverinfo='text',
            hovertext=[
                f"Round: {round_val}<br>Decelerations: {int(val)}"
                for round_val, val in zip(df_game['Round'], df_game['Total Decelerations >3m/s/s'])
            ]
        )
    ])

    # Update layout for professional styling
    fig.update_layout(
        barmode='group',
        title={
            'text': '<b>Accelerations/Decelerations >3m/s/s</b>',
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'size': 24, 'family': 'Roboto', 'color': 'white'}
        },
        xaxis_title='Round',
        yaxis_title='Count',
        plot_bgcolor='#1e1e1e',
        paper_bgcolor='#1e1e1e',
        font=dict(color='white', family='Roboto'),
        xaxis=dict(
            showline=True,
            showgrid=False,
            tickfont=dict(family='Roboto', size=12, color='white')
        ),
        yaxis=dict(
            showline=True,
            gridcolor='gray',
            zeroline=True,
            showgrid=True,
            tickfont=dict(family='Roboto', size=12, color='white')
        ),
        margin=dict(l=40, r=40, t=40, b=40),
        legend=dict(
            x=0.8,
            y=1.1,
            bgcolor='rgba(0, 0, 0, 0)',
            bordercolor='rgba(0, 0, 0, 0)',
            font=dict(family='Roboto', size=12, color='white')
        )
    )

    return fig


# start of callbacks section


# Define the callback to update the Power Plays chart
@app.callback(
    Output('power-plays-chart', 'figure'),
    [Input('update-button', 'n_clicks'),
     Input('btn-date', 'n_clicks'),
     Input('btn-value', 'n_clicks'),
     Input('btn-form', 'n_clicks')],
    [dash.dependencies.State('player-dropdown', 'value')]
)
def update_power_plays_chart(n_clicks, btn_date, btn_value, btn_form, selected_player):
    # Determine the most recently clicked button to set the sort order
    ctx = dash.callback_context
    if not ctx.triggered:
        sort_order = 'date'
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        if button_id == 'btn-value':
            sort_order = 'value'
        elif button_id == 'btn-form':
            sort_order = 'form'
        else:
            sort_order = 'date'

    # Filter data for the selected player across all rounds
    df_filtered = df[df['Player Name'] == selected_player]

    # Apply sorting based on the selected option
    if sort_order == 'form':
        df_filtered = df_filtered[df_filtered['Split Name'] == 'game']
        df_filtered = df_filtered.sort_values(by='Date', ascending=False).head(5)
        df_filtered = df_filtered.sort_values(by='Date', ascending=False)
    elif sort_order == 'date':
        df_filtered = df_filtered.sort_values(by=['Date'])
    else:  # 'value' sort order
        df_filtered = df_filtered.sort_values('Power Plays', ascending=True)

    # Create and return the Power Plays chart
    return create_power_plays_chart(df_filtered, selected_player, sort_order)

# Define the callback to update the Sprint Distance chart
@app.callback(
    Output('sprint-distance-chart', 'figure'),
    [Input('update-button', 'n_clicks'),
     Input('sprint-btn-date', 'n_clicks'),
     Input('sprint-btn-value', 'n_clicks'),
     Input('sprint-btn-form', 'n_clicks')],
    [dash.dependencies.State('player-dropdown', 'value')]
)
def update_sprint_chart(n_clicks, btn_date, btn_value, btn_form, selected_player):
    # Determine the most recently clicked button to set the sort order
    ctx = dash.callback_context
    if not ctx.triggered:
        sort_order = 'date'
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        if button_id == 'sprint-btn-value':
            sort_order = 'value'
        elif button_id == 'sprint-btn-form':
            sort_order = 'form'
        else:
            sort_order = 'date'

    # Filter data for the selected player across all rounds
    df_filtered = df[df['Player Name'] == selected_player]

    # Create and return the Sprint Distance chart
    return create_sprint_distance_chart(df_filtered, selected_player, sort_order)


# Define the callback to update the Player Load chart
@app.callback(
    Output('player-load-chart', 'figure'),
    [Input('update-button', 'n_clicks'),
     Input('btn-player-load-date', 'n_clicks'),
     Input('btn-player-load-value', 'n_clicks'),
     Input('btn-player-load-form', 'n_clicks')],
    [dash.dependencies.State('player-dropdown', 'value')]
)
def update_player_load_chart(n_clicks, btn_date, btn_value, btn_form, selected_player):
    # Determine the most recently clicked button to set the sort order
    ctx = dash.callback_context
    if not ctx.triggered:
        sort_order = 'date'
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        if button_id == 'btn-player-load-value':
            sort_order = 'value'
        elif button_id == 'btn-player-load-form':
            sort_order = 'form'
        else:
            sort_order = 'date'

    # Filter data for the selected player across all rounds
    df_filtered = df[df['Player Name'] == selected_player]

    # Apply sorting based on the selected option
    if sort_order == 'form':
        df_filtered = df_filtered[df_filtered['Split Name'] == 'game']
        df_filtered = df_filtered.sort_values(by='Date', ascending=False).head(5)
        df_filtered = df_filtered.sort_values(by='Date', ascending=False)
    elif sort_order == 'date':
        df_filtered = df_filtered.sort_values(by=['Date'])
    else:  # 'value' sort order
        df_filtered = df_filtered.sort_values('Player Load', ascending=True)

    # Create and return the Player Load chart
    return create_player_load_chart(df_filtered, selected_player, sort_order)


# Define the callback to update the Accelerations and Decelerations chart
# Define the callback to update the Accelerations and Decelerations chart
@app.callback(
    Output('accel-decel-chart', 'figure'),
    [Input('update-button', 'n_clicks'),
     Input('btn-accel-decel-date', 'n_clicks'),
     Input('btn-accel-decel-value', 'n_clicks'),
     Input('btn-accel-decel-form', 'n_clicks')],
    [dash.dependencies.State('player-dropdown', 'value')]
)
def update_accel_decel_chart(n_clicks, btn_date, btn_value, btn_form, selected_player):
    # Determine the most recently clicked button to set the sort order
    ctx = dash.callback_context
    if not ctx.triggered:
        sort_order = 'date'
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        if button_id == 'btn-accel-decel-value':
            sort_order = 'value'
        elif button_id == 'btn-accel-decel-form':
            sort_order = 'form'
        else:
            sort_order = 'date'

    # Filter data for the selected player across all rounds
    df_filtered = df[df['Player Name'] == selected_player]

    # **Ensure columns are created before sorting or filtering**
    acceleration_columns = [
        'Accelerations Zone Count: 3 - 4 m/s/s',
        'Accelerations Zone Count: > 4 m/s/s'
    ]
    deceleration_columns = [
        'Deceleration Zone Count: 3 - 4 m/s/s',
        'Deceleration Zone Count: > 4 m/s/s'
    ]

    # Create the necessary columns within the callback to ensure they exist
    df_filtered['Total Accelerations >3m/s/s'] = df_filtered[acceleration_columns].sum(axis=1)
    df_filtered['Total Decelerations >3m/s/s'] = df_filtered[deceleration_columns].sum(axis=1)

    # Check if the columns were created successfully
    if 'Total Accelerations >3m/s/s' not in df_filtered.columns:
        print("Error: 'Total Accelerations >3m/s/s' column not found in the DataFrame.")
        return go.Figure()  # Return an empty figure if the column is missing

    # Now call the chart creation function
    return create_accel_decel_chart(df_filtered, selected_player, sort_order)



# Define the callback to update the Distance Per Min chart
@app.callback(
    Output('distance-per-min-chart', 'figure'),
    [Input('update-button', 'n_clicks'),
     Input('btn-dpm-date', 'n_clicks'),
     Input('btn-dpm-value', 'n_clicks'),
     Input('btn-dpm-form', 'n_clicks')],
    [dash.dependencies.State('player-dropdown', 'value')]
)
def update_distance_per_min_chart(n_clicks, btn_date, btn_value, btn_form, selected_player):
    # Determine the most recently clicked button to set the sort order
    ctx = dash.callback_context
    if not ctx.triggered:
        sort_order = 'date'
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        if button_id == 'btn-dpm-value':
            sort_order = 'value'
        elif button_id == 'btn-dpm-form':
            sort_order = 'form'
        else:
            sort_order = 'date'

    # Filter data for the selected player across all rounds
    df_filtered = df[df['Player Name'] == selected_player]

    # Apply sorting based on the selected option
    if sort_order == 'form':
        # Filter to include only rows where Split Name is 'game'
        df_filtered = df_filtered[df_filtered['Split Name'] == 'game']
        
        # Sort by date to get the last 5 recent unique rounds, strictly in date order
        df_filtered = df_filtered.sort_values(by='Date', ascending=False)  # Sort by date, most recent first
        df_filtered = df_filtered.head(5)  # Select the last 5 rounds by date, reverse order for form view
        df_filtered = df_filtered.sort_values(by='Date', ascending=False)  # Keep the order most recent right

    elif sort_order == 'date':
        df_filtered = df_filtered.sort_values(by=['Date'])  # Default sort by date

    else:  # 'value' sort order
        df_filtered = df_filtered.sort_values('Distance Per Min (m/min)', ascending=True)  # Sort by value from lowest to highest

    # Create and return the Distance Per Min chart
    return create_distance_per_min_chart(df_filtered, selected_player, sort_order)


# Callback to update the Top Speed chart
# Define the callback to update the Top Speed chart
# Updated callback for Top Speed Chart with correct button IDs
@app.callback(
    Output('top-speed-chart', 'figure'),
    [Input('update-button', 'n_clicks'),
     Input('btn-top-speed-date', 'n_clicks'),
     Input('btn-top-speed-value', 'n_clicks'),
     Input('btn-top-speed-form', 'n_clicks')],
    [dash.dependencies.State('player-dropdown', 'value')]
)
def update_top_speed_chart(n_clicks, btn_date, btn_value, btn_form, selected_player):
    # Determine sort order based on the last clicked button
    ctx = dash.callback_context
    if not ctx.triggered:
        sort_order = 'date'
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        if button_id == 'btn-top-speed-value':
            sort_order = 'value'
        elif button_id == 'btn-top-speed-form':
            sort_order = 'form'
        else:
            sort_order = 'date'
    
    # Filter data for the selected player
    df_filtered = df[df['Player Name'] == selected_player]

    # Create and return the Top Speed chart based on the determined order
    return create_top_speed_chart(df_filtered, selected_player, sort_order)



# Run the app
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8050)),
        debug=True
    )

