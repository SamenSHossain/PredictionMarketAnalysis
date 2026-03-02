import os
import webbrowser
from threading import Timer
import pandas as pd
from dash import Dash, html, dash_table

# =====================================================
# LOAD DATA
# =====================================================

df_master = pd.read_csv("processed_data.csv")

leaderboard_df = df_master.groupby(
    ['token_id', 'question', 'end_date'],
    as_index=False
).agg({
    'price': 'max',
    'actual_outcome': 'max',
    'volume': 'max'
})

leaderboard_df = leaderboard_df.rename(columns={
    'token_id': 'Token ID',
    'question': 'Market Question',
    'end_date': 'End Date',
    'price': 'Peak Price',
    'actual_outcome': 'Outcome',
    'volume': 'Volume'
})

# =====================================================
# INIT DASH APP
# =====================================================

app = Dash(__name__, assets_folder='assets')
server = app.server

# =====================================================
# DEBUG: CHECK ASSETS FOLDER
# =====================================================

assets_path = "assets"  # Relative path

print(f"\n{'='*50}")
print(f"Looking for assets in: {os.path.abspath(assets_path)}")
print(f"Assets folder exists: {os.path.exists(assets_path)}")

if os.path.exists(assets_path):
    all_files = os.listdir(assets_path)
    print(f"All files in assets: {all_files}")
    
    image_files = sorted([
        f for f in all_files
        if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))
    ])
    print(f"Image files found: {image_files}")
else:
    image_files = []
    print("ERROR: Assets folder not found!")

print(f"{'='*50}\n")

# =====================================================
# LAYOUT
# =====================================================

app.layout = html.Div([

    html.H1(
        "Polymarket Market Efficiency Dashboard",
        style={
            'textAlign': 'center',
            'marginBottom': '40px',
            'fontFamily': 'Arial'
        }
    ),

    html.Div([

        # ================= LEFT SIDE — TABLE =================
        html.Div([
            html.H3("Market Leaderboard"),

            dash_table.DataTable(
                data=leaderboard_df.to_dict("records"),
                columns=[{"name": col, "id": col} for col in leaderboard_df.columns],
                page_size=15,
                sort_action="native",
                filter_action="native",

                style_table={
                    'height': '800px',
                    'overflowY': 'auto',
                    'overflowX': 'auto',
                    'border': '1px solid #ddd'
                },

                style_cell={
                    'padding': '8px',
                    'textAlign': 'left',
                    'minWidth': '120px',
                    'whiteSpace': 'normal'
                },

                style_header={
                    'backgroundColor': '#f4f4f4',
                    'fontWeight': 'bold'
                }
            )
        ], style={
            'width': '60%',
            'display': 'inline-block',
            'verticalAlign': 'top',
            'paddingRight': '20px'
        }),

        # ================= RIGHT SIDE — CHARTS =================
        html.Div([
            html.H3("Charts"),

            html.Div([
                html.Div([
                    html.H4(img, style={'fontSize': '14px', 'color': '#666'}),
                    html.Img(
                        src=app.get_asset_url(img),
                        style={
                            'width': '100%',
                            'marginBottom': '25px',
                            'borderRadius': '8px',
                            'boxShadow': '0px 4px 10px rgba(0,0,0,0.1)'
                        }
                    )
                ]) for img in image_files
            ] if image_files else [
                html.P(
                    f"No image files found in assets folder. Files present: {os.listdir(assets_path) if os.path.exists(assets_path) else 'Folder does not exist'}", 
                    style={'color': 'red', 'fontSize': '16px', 'padding': '20px'}
                )
            ])
        ], style={
            'width': '38%',
            'display': 'inline-block',
            'verticalAlign': 'top'
        })

    ])

])

# =====================================================
# AUTO-OPEN BROWSER + RUN SERVER
# =====================================================

def open_browser():
    webbrowser.open_new("http://127.0.0.1:8050/")

if __name__ == "__main__":
    Timer(3, open_browser).start()
    app.run(debug=False, port=8050)