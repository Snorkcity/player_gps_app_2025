import dash
from dash import dcc, html, Input, Output, State, callback
import pandas as pd
from dash import dash_table
from dash import ctx
from dash import Dash
import plotly.express as px
import gspread
import plotly.graph_objects as go
from oauth2client.service_account import ServiceAccountCredentials
import dash_bootstrap_components as dbc
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from datetime import datetime
from io import BytesIO
import os


source_file = '2025-Belconnen-NPLW-data.xlsx'


df = pd.read_excel(source_file, sheet_name='individual stats')

# Initialize the Dash app with a dark theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

# Updated layout with player-centric focus
# Reusable font and button styles
base_font = {
    "fontFamily": "Segoe UI",
    "fontSize": "14px"
}

title_font = {
    "fontFamily": "Segoe UI Black",
    "fontSize": "18px"
}

button_style = {
    "backgroundColor": "skyblue",
    "color": "black",
    "border": "none",
    "padding": "10px 16px",
    "marginRight": "10px",
    "borderRadius": "6px",
    "fontWeight": "bold",
    "fontFamily": "Segoe UI",
    "cursor": "pointer",
    "boxShadow": "2px 2px 5px rgba(0, 0, 0, 0.3)",
    "textAlign": "left"
}

# App Layout
app.layout = dbc.Container([

    # ✅ Clean title (matches Season Stats style)
    html.H1(
        "NPLW - GPS Player Data - 2025",
        style={
            "backgroundColor": "#1E3A5F",  # ← updated blue
            "textAlign": "center",
            "color": "#FFFFFF",
            "fontFamily": title_font["fontFamily"],
            "fontSize": "32px",
            "padding": "10px 0",
            "margin": "0"
        }
    ),
    # html.Hr(style={"borderColor": "white"})  ← Removed this

    # ✅ Spacer after title
    html.Div(style={"height": "20px"}),


    # ✅ Player dropdown
    html.Div([
        html.Label("Select a Player", style={
            "color": "white",
            "fontSize": "16px",
            "fontFamily": base_font["fontFamily"],
            "fontWeight": "bold"  # 👈 Added bold text
        }),
        dcc.Dropdown(
            id='player-dropdown',
            options=[{'label': player, 'value': player} for player in sorted(df['Player Name'].unique())],
            placeholder='Select a Player',
            style={
                "width": "220px",
                "color": "black",
                "margin": "0 auto",
                "textAlign": "center",
                "fontFamily": base_font["fontFamily"],
                "fontSize": "14px",
                "fontWeight": "bold"  # 👈 Also added here
            }
        )
    ], style={"textAlign": "center", "padding": "10px"}),


    html.Br(),

    # Sprint Distance
    html.Div([
        html.Div([
            html.Button("Round Order", id="sprint-btn-date", n_clicks=0, style=button_style),
            html.Button("Lowest to Highest", id="sprint-btn-value", n_clicks=0, style=button_style),
            html.Button("Form (Last 5 Rounds)", id="sprint-btn-form", n_clicks=0, style=button_style)
        ], style={"textAlign": "left", "padding": "10px", "paddingLeft": "40px"}),
        dcc.Graph(id="sprint-distance-chart", style={"backgroundColor": "black"})
    ], style={
        "backgroundColor": "#1E3A5F",
        "padding": "20px",
        "border": "1px solid white",
        "borderRadius": "10px",
        "marginBottom": "20px"
    }),

    # Power Plays
    html.Div([
        html.Div([
            html.Button("Round Order", id="btn-date", n_clicks=0, style=button_style),
            html.Button("Lowest to Highest", id="btn-value", n_clicks=0, style=button_style),
            html.Button("Form (Last 5 Rounds)", id="btn-form", n_clicks=0, style=button_style)
        ], style={"textAlign": "left", "padding": "10px", "paddingLeft": "40px"}),
        dcc.Graph(id="power-plays-chart", style={"backgroundColor": "black"})
    ], style={
        "backgroundColor": "#1E3A5F",
        "padding": "20px",
        "border": "1px solid white",
        "borderRadius": "10px",
        "marginBottom": "20px"
    }),

    # Player Load
    html.Div([
        html.Div([
            html.Button("Round Order", id="btn-player-load-date", n_clicks=0, style=button_style),
            html.Button("Lowest to Highest", id="btn-player-load-value", n_clicks=0, style=button_style),
            html.Button("Form (Last 5 Rounds)", id="btn-player-load-form", n_clicks=0, style=button_style)
        ], style={"textAlign": "left", "padding": "10px", "paddingLeft": "40px"}),
        dcc.Graph(id="player-load-chart", style={"backgroundColor": "black"})
    ], style={
        "backgroundColor": "#1E3A5F",
        "padding": "20px",
        "border": "1px solid white",
        "borderRadius": "10px",
        "marginBottom": "20px"
    }),

    # Top Speed
    html.Div([
        html.Div([
            html.Button("Round Order", id="btn-top-speed-date", n_clicks=0, style=button_style),
            html.Button("Lowest to Highest", id="btn-top-speed-value", n_clicks=0, style=button_style),
            html.Button("Form (Last 5 Rounds)", id="btn-top-speed-form", n_clicks=0, style=button_style)
        ], style={"textAlign": "left", "padding": "10px", "paddingLeft": "40px"}),
        dcc.Graph(id="top-speed-chart", style={"backgroundColor": "black"})
    ], style={
        "backgroundColor": "#1E3A5F",
        "padding": "20px",
        "border": "1px solid white",
        "borderRadius": "10px",
        "marginBottom": "20px"
    }),

    # Distance Per Minute
    html.Div([
        html.Div([
            html.Button("Round Order", id="btn-dpm-date", n_clicks=0, style=button_style),
            html.Button("Lowest to Highest", id="btn-dpm-value", n_clicks=0, style=button_style),
            html.Button("Form (Last 5 Rounds)", id="btn-dpm-form", n_clicks=0, style=button_style)
        ], style={"textAlign": "left", "padding": "10px", "paddingLeft": "40px"}),
        dcc.Graph(id="distance-per-min-chart", style={"backgroundColor": "black"})
    ], style={
        "backgroundColor": "#1E3A5F",
        "padding": "20px",
        "border": "1px solid white",
        "borderRadius": "10px",
        "marginBottom": "20px"
    }),

    # Accelerations/Decelerations
    html.Div([
        html.Div([
            html.Button("Round Order", id="btn-accel-decel-date", n_clicks=0, style=button_style),
            html.Button("Lowest to Highest", id="btn-accel-decel-value", n_clicks=0, style=button_style),
            html.Button("Form (Last 5 Rounds)", id="btn-accel-decel-form", n_clicks=0, style=button_style)
        ], style={"textAlign": "left", "padding": "10px", "paddingLeft": "40px"}),
        dcc.Graph(id="accel-decel-chart", style={"backgroundColor": "black"})
    ], style={
        "backgroundColor": "#1E3A5F",
        "padding": "20px",
        "border": "1px solid white",
        "borderRadius": "10px",
        "marginBottom": "20px"
    }),

    

    ], style={
    "backgroundColor": "#1E3A5F",
    "minHeight": "100vh",
    "paddingBottom": "30px",
    "paddingTop": "20px"
}, fluid=True)  # ✅ This closes the dbc.Container


# end of layout section

# start of chart section

# this creates/builds the chart for power plays, it is not the layout or the callback.
def create_power_plays_chart(df_filtered, selected_player, sort_order):
    # Filter data
    df_power_plays = df_filtered[df_filtered['Split Name'] == 'game'][['Player Name', 'Round', 'Date', 'Power Plays', 'Mins played']]

    # Calculate per 10 mins
    df_power_plays['PP per 10min'] = (
        (df_power_plays['Power Plays'] / df_power_plays['Mins played']) * 10
    ).replace([float('inf'), -float('inf')], 0).fillna(0).round(0).astype(int)

    # Sort logic
    if sort_order == 'date':
        df_power_plays = df_power_plays.sort_values(by='Date')
    elif sort_order == 'value':
        df_power_plays = df_power_plays.sort_values(by='Power Plays', ascending=True)
    elif sort_order == 'form':
        df_power_plays = df_power_plays.sort_values(by='Date', ascending=False).head(5).sort_values(by='Date', ascending=True)

    # Chart
    fig = go.Figure(data=[
        go.Scatter(
            x=df_power_plays['Round'],
            y=df_power_plays['Power Plays'],
            mode='lines+markers',
            line=dict(color='#00BFFF', width=3),  # Sky Blue
            marker=dict(size=8),
            hoverinfo='text',
            hovertext=[
                f"Round: {round_name}<br>Date: {date}<br>Power Plays: {int(val)}<br>PP per 10min: {int(pp10)}<br>Mins Played: {int(mins)}"
                for round_name, date, val, pp10, mins in zip(
                    df_power_plays['Round'],
                    df_power_plays['Date'].dt.strftime('%d-%m-%Y'),
                    df_power_plays['Power Plays'],
                    df_power_plays['PP per 10min'],
                    df_power_plays['Mins played']
                )
            ]
        )
    ])

    # Layout styling
    fig.update_layout(
        title={
            'text': f"<b>Power Plays - {selected_player}</b>",
            'font': dict(family="Segoe UI Black", size=24, color="white"),
            'x': 0.5,
            'y': 0.95,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        xaxis_title="Round",
        yaxis_title="Power Plays",
        font=dict(family="Segoe UI", size=14, color="white"),
        plot_bgcolor="#1e1e1e",
        paper_bgcolor="#1e1e1e",
        xaxis=dict(
            showline=True,
            showgrid=False,
            tickfont=dict(size=12, color="white"),
            linecolor='white'
        ),
        yaxis=dict(
            showline=True,
            gridcolor="gray",
            zeroline=True,
            tickfont=dict(size=12, color="white"),
            linecolor='white'
        ),
        hoverlabel=dict(font=dict(family="Segoe UI")),
        margin=dict(l=20, r=20, t=60, b=20),
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
            'font': {'size': 24, 'family': 'Segoe UI Black', 'color': 'white'}
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
            tickfont=dict(family='Segoe UI', size=14, color='white')
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor='gray',
            zeroline=True,
            showline=True,
            linewidth=2,
            linecolor='white',
            tickfont=dict(family='Segoe UI', size=14, color='white')
        ),
        plot_bgcolor='#1e1e1e',  # Dark theme background for the plot area
        paper_bgcolor='#1e1e1e', # Dark theme background for the entire page
        legend=dict(
            x=0.8,
            y=1.1,
            bgcolor='rgba(0, 0, 0, 0)',
            bordercolor='rgba(0, 0, 0, 0)',
            font=dict(family='Segoe UI', size=14, color='white')
        ),
        margin=dict(l=20, r=20, t=60, b=20)  # Tighter margins for a clean look
    )
    return fig


# Function to create the Distance Per Min Chart for the player-centric view
def create_distance_per_min_chart(df_filtered, selected_player, sort_order):
    # Filter relevant splits
    df_1st_half = df_filtered[df_filtered['Split Name'] == '1st.half'][['Round', 'Date', 'Distance Per Min (m/min)']]
    df_2nd_half = df_filtered[df_filtered['Split Name'] == '2nd.half'][['Round', 'Date', 'Distance Per Min (m/min)']]
    df_game = df_filtered[df_filtered['Split Name'] == 'game'][['Round', 'Date', 'Distance Per Min (m/min)', 'Mins played']]

    # Rename for clarity
    df_1st_half = df_1st_half.rename(columns={'Distance Per Min (m/min)': '1st Half'})
    df_2nd_half = df_2nd_half.rename(columns={'Distance Per Min (m/min)': '2nd Half'})
    df_game = df_game.rename(columns={'Distance Per Min (m/min)': 'Game'})

    # Merge all data
    df_merged = pd.merge(df_game, df_1st_half, on=['Round', 'Date'], how='left')
    df_merged = pd.merge(df_merged, df_2nd_half, on=['Round', 'Date'], how='left')

    # Handle sort
    if sort_order == 'value':
        df_merged = df_merged.sort_values('Game', ascending=True)
    elif sort_order == 'form':
        df_merged = df_merged.sort_values('Date', ascending=False).head(5).sort_values('Date')
    else:
        df_merged = df_merged.sort_values('Date')

    # Fill missing values
    df_merged = df_merged.fillna(0)

    # Chart
    fig = go.Figure(data=[
        go.Bar(
            name='Game',
            x=df_merged['Round'],
            y=df_merged['Game'],
            marker_color='#1E90FF',  # Blue
            hoverinfo='text',
            hovertext=[
                f"Total: {int(game)} m/min<br>"
                f"2nd Half: {int(second)} m/min<br>"
                f"1st Half: {int(first)} m/min<br>"
                f"Mins Played: {int(mins)} min"
                for game, second, first, mins in zip(
                    df_merged['Game'], 
                    df_merged['2nd Half'], 
                    df_merged['1st Half'], 
                    df_merged['Mins played']
                )
            ]
        )
    ])

    # Layout styling
    fig.update_layout(
        title=dict(
            text=f"<b>Distance Per Min - {selected_player}</b>",
            x=0.5,
            xanchor='center',
            font=dict(size=24, family='Segoe UI Black', color='white')
        ),
        xaxis_title='Round',
        yaxis_title='Distance Per Min (m/min)',
        font=dict(family='Segoe UI', size=14, color='white'),
        plot_bgcolor='#1e1e1e',
        paper_bgcolor='#1e1e1e',
        xaxis=dict(
            showline=True,
            showgrid=False,
            tickfont=dict(size=14, family='Segoe UI', size=14, color='white')
        ),
        yaxis=dict(
            showline=True,
            gridcolor='gray',
            zeroline=True,
            tickfont=dict(size=14, family='Segoe UI', size=14, color='white')
        ),
        margin=dict(l=20, r=20, t=60, b=20),
        legend=dict(
            x=0.8,
            y=1.1,
            bgcolor='rgba(0,0,0,0)',
            font=dict(family='Segoe UI', size=14, color='white')
        ),
        hoverlabel=dict(font=dict(family='Segoe UI'))
    )

    return fig


# Updated Function to create the Top Speed Chart for player-centric view
def create_top_speed_chart(df_filtered, selected_player, sort_order):
    try:
        # Extract data for each half and game
        df_1st_half = df_filtered[df_filtered['Split Name'] == '1st.half'][['Round', 'Top Speed (m/s)', 'Date']]
        df_2nd_half = df_filtered[df_filtered['Split Name'] == '2nd.half'][['Round', 'Top Speed (m/s)', 'Date']]
        df_game = df_filtered[df_filtered['Split Name'] == 'game'][['Round', 'Top Speed (m/s)', 'Mins played', 'Date']]
        
        df_1st_half = df_1st_half.rename(columns={'Top Speed (m/s)': 'Top Speed (m/s) 1st Half', 'Date': 'Date 1st Half'})
        df_2nd_half = df_2nd_half.rename(columns={'Top Speed (m/s)': 'Top Speed (m/s) 2nd Half', 'Date': 'Date 2nd Half'})
    except KeyError as e:
        print(f"Error: Missing column {e} in the DataFrame.")
        return go.Figure()

    # Merge 1st and 2nd half speeds, then add game minutes
    df_top_speed = pd.merge(df_1st_half, df_2nd_half, on='Round', how='outer')
    df_top_speed = pd.merge(df_top_speed, df_game, on='Round', how='left')

    df_top_speed = df_top_speed.infer_objects(copy=False)
    df_top_speed['Mins played'] = pd.to_numeric(df_top_speed['Mins played'], errors='coerce').fillna(0).astype(int)

    # Sort logic
    if sort_order == 'form':
        df_top_speed = df_top_speed.sort_values(by='Date', ascending=False).head(5).sort_values(by='Date', ascending=True)
    elif sort_order == 'value':
        df_top_speed = df_top_speed.sort_values(by='Top Speed (m/s)', ascending=True)
    else:
        df_top_speed = df_top_speed.sort_values(by='Date', ascending=True)

    # Build chart
    fig = go.Figure(data=[
        go.Bar(
            name='1st Half',
            x=df_top_speed['Round'],
            y=df_top_speed['Top Speed (m/s) 1st Half'],
            marker_color='#87CEEB',  # Sky blue
            hoverinfo='text',
            hovertext=[
                f"1st Half: {speed_1st:.1f} m/s<br>2nd Half: {speed_2nd:.1f} m/s<br>Total Minutes Played: {int(mins)}"
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
            marker_color='#4682B4',  # Steel blue
            hoverinfo='text',
            hovertext=[
                f"2nd Half: {speed_2nd:.1f} m/s<br>1st Half: {speed_1st:.1f} m/s<br>Total Minutes Played: {int(mins)}"
                for speed_2nd, speed_1st, mins in zip(
                    df_top_speed['Top Speed (m/s) 2nd Half'],
                    df_top_speed['Top Speed (m/s) 1st Half'],
                    df_top_speed['Mins played']
                )
            ]
        )
    ])

    # Layout styling
    fig.update_layout(
        barmode='group',
        title=f"Top Speed Comparison - {selected_player}",
        title_font=dict(family="Segoe UI Black", size=24, color="white"),
        title_x=0.5,  # Centers the title
        xaxis_title="Round",
        yaxis_title="Top Speed (m/s)",
        font=dict(family="Segoe UI", size=14, color="white"),
        plot_bgcolor="#1e1e1e",
        paper_bgcolor="#1e1e1e",
        xaxis=dict(
            showline=True,
            showgrid=False,
            tickfont=dict(size=14),
        ),
        yaxis=dict(
            showline=True,
            gridcolor="gray",
            zeroline=True,
            tickfont=dict(size=14),
        ),
        hoverlabel=dict(font=dict(family="Segoe UI")),
        margin=dict(l=20, r=20, t=60, b=20),
    )


    return fig


# Updated Function to create the Player Load Chart
def create_player_load_chart(df_filtered, selected_player, sort_order):
    df_game = df_filtered[df_filtered['Split Name'] == 'game']

    if sort_order == 'form':
        df_game = df_game.sort_values(by='Date', ascending=False).head(5).sort_values(by='Date', ascending=True)
    elif sort_order == 'date':
        df_game = df_game.sort_values(by='Date', ascending=True)
    else:
        df_game = df_game.sort_values(by='Player Load', ascending=True)

    fig = go.Figure(data=[
        go.Scatter(
            x=df_game['Round'],
            y=df_game['Player Load'],
            mode='lines+markers',
            line=dict(color='#00BFFF', width=3),  # Sky Blue line
            marker=dict(size=8),
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

    fig.update_layout(
        title=f"Player Load - {selected_player}",
        title_font=dict(family="Segoe UI Black", size=24, color="white"),
        title_x=0.5,  # Center the title
        xaxis_title="Round",
        yaxis_title="Player Load",
        font=dict(family="Segoe UI", size=14, color="white"),
        plot_bgcolor="#1e1e1e",
        paper_bgcolor="#1e1e1e",
        xaxis=dict(
            showline=True,
            showgrid=False,
            tickfont=dict(size=14),
        ),
        yaxis=dict(
            showline=True,
            gridcolor="gray",
            zeroline=True,
            tickfont=dict(size=14),
        ),
        hoverlabel=dict(font=dict(family="Segoe UI")),
        margin=dict(l=20, r=20, t=60, b=20),
    )


    return fig



# Updated Function to create the Accel/Decel Chart
def create_accel_decel_chart(df_filtered, selected_player, sort_order):
    df_game = df_filtered[df_filtered['Split Name'] == 'game']

    acceleration_columns = [
        'Accelerations Zone Count: 3 - 4 m/s/s',
        'Accelerations Zone Count: > 4 m/s/s'
    ]
    deceleration_columns = [
        'Deceleration Zone Count: 3 - 4 m/s/s',
        'Deceleration Zone Count: > 4 m/s/s'
    ]

    df_game['Total Accelerations >3m/s/s'] = df_game[acceleration_columns].sum(axis=1)
    df_game['Total Decelerations >3m/s/s'] = df_game[deceleration_columns].sum(axis=1)

    if sort_order == 'form':
        df_game = df_game.sort_values(by='Date', ascending=False).head(5).sort_values(by='Date', ascending=True)
    elif sort_order == 'date':
        df_game = df_game.sort_values(by='Date')
    else:
        df_game = df_game.sort_values(by='Total Accelerations >3m/s/s')

    if df_game.empty:
        return go.Figure()

    fig = go.Figure(data=[
        go.Bar(
            name='Accelerations',
            x=df_game['Round'],
            y=df_game['Total Accelerations >3m/s/s'],
            marker_color='#00BFFF',
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
            marker_color='#6495ED',
            hoverinfo='text',
            hovertext=[
                f"Round: {round_val}<br>Decelerations: {int(val)}"
                for round_val, val in zip(df_game['Round'], df_game['Total Decelerations >3m/s/s'])
            ]
        )
    ])

    fig.update_layout(
        title=f"Accelerations/Decelerations >3m/s² - {selected_player}",
        title_font=dict(family="Segoe UI Black", size=24, color="white"),
        title_x=0.5,  # Center the title
        xaxis_title="Round",
        yaxis_title="Count",
        font=dict(family="Segoe UI", size=14, color="white"),
        plot_bgcolor="#1e1e1e",
        paper_bgcolor="#1e1e1e",
        xaxis=dict(
            showline=True,
            showgrid=False,
            tickfont=dict(size=14, color='white')
        ),
        yaxis=dict(
            showline=True,
            gridcolor="gray",
            zeroline=True,
            tickfont=dict(size=14, color='white')
        ),
        hoverlabel=dict(font=dict(family="Segoe UI")),
        margin=dict(l=20, r=20, t=60, b=20),
        barmode="group"
    )


    return fig



# start of callbacks section


# Define the callback to update the Power Plays chart
# Updated callback for Power Plays chart without update button
@app.callback(
    Output('power-plays-chart', 'figure'),
    [
        Input('player-dropdown', 'value'),
        Input('btn-date', 'n_clicks'),
        Input('btn-value', 'n_clicks'),
        Input('btn-form', 'n_clicks')
    ]
)
def update_power_plays_chart(selected_player, btn_date, btn_value, btn_form):
    if not selected_player:
        return go.Figure()

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

    return create_power_plays_chart(df_filtered, selected_player, sort_order)

# Define the callback to update the Sprint Distance chart
@app.callback(
    Output('sprint-distance-chart', 'figure'),
    [
        Input('player-dropdown', 'value'),
        Input('sprint-btn-date', 'n_clicks'),
        Input('sprint-btn-value', 'n_clicks'),
        Input('sprint-btn-form', 'n_clicks')
    ]
)
def update_sprint_chart(selected_player, btn_date, btn_value, btn_form):
    if not selected_player:
        return go.Figure()

    # Determine the most recently clicked button
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

    # Filter data for selected player
    df_filtered = df[df['Player Name'] == selected_player]

    # Return the chart
    return create_sprint_distance_chart(df_filtered, selected_player, sort_order)


# Define the callback to update the Player Load chart
# Updated callback for Player Load chart without update button
@app.callback(
    Output('player-load-chart', 'figure'),
    [
        Input('player-dropdown', 'value'),
        Input('btn-player-load-date', 'n_clicks'),
        Input('btn-player-load-value', 'n_clicks'),
        Input('btn-player-load-form', 'n_clicks')
    ]
)
def update_player_load_chart(selected_player, btn_date, btn_value, btn_form):
    if not selected_player:
        return go.Figure()

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

    # Filter and sort
    df_filtered = df[df['Player Name'] == selected_player]

    if sort_order == 'form':
        df_filtered = df_filtered[df_filtered['Split Name'] == 'game']
        df_filtered = df_filtered.sort_values(by='Date', ascending=False).head(5)
        df_filtered = df_filtered.sort_values(by='Date', ascending=False)
    elif sort_order == 'date':
        df_filtered = df_filtered.sort_values(by=['Date'])
    else:
        df_filtered = df_filtered.sort_values('Player Load', ascending=True)

    return create_player_load_chart(df_filtered, selected_player, sort_order)



# Define the callback to update the Accelerations and Decelerations chart
@app.callback(
    Output('accel-decel-chart', 'figure'),
    [
        Input('btn-accel-decel-date', 'n_clicks'),
        Input('btn-accel-decel-value', 'n_clicks'),
        Input('btn-accel-decel-form', 'n_clicks'),
        Input('player-dropdown', 'value')
    ]
)

def update_accel_decel_chart(btn_date, btn_value, btn_form, selected_player):
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
    [
        Input('player-dropdown', 'value'),
        Input('btn-dpm-date', 'n_clicks'),
        Input('btn-dpm-value', 'n_clicks'),
        Input('btn-dpm-form', 'n_clicks')
    ]
)
def update_distance_per_min_chart(selected_player, btn_date, btn_value, btn_form):
    if not selected_player:
        return go.Figure()

    # Determine sort order based on clicked button
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

    # Filter the data
    df_filtered = df[df['Player Name'] == selected_player]

    # Return updated chart
    return create_distance_per_min_chart(df_filtered, selected_player, sort_order)



# Callback to update the Top Speed chart
@app.callback(
    Output('top-speed-chart', 'figure'),
    [
        Input('btn-top-speed-date', 'n_clicks'),
        Input('btn-top-speed-value', 'n_clicks'),
        Input('btn-top-speed-form', 'n_clicks'),
        Input('player-dropdown', 'value')
    ]
)
def update_top_speed_chart(btn_date, btn_value, btn_form, selected_player):
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

