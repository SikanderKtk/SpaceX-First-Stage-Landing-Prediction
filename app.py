import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
from datetime import datetime

# -----------------------------
# Load your processed dataset
# -----------------------------
df = pd.read_csv("data/processed/launches_clean.csv")
df["year"] = pd.to_datetime(df["date_utc"]).dt.year

# -----------------------------
# Initialize Dash App with Bootstrap
# -----------------------------
app = Dash(__name__, external_stylesheets=[dbc.themes.LUX])

# -----------------------------
# Layout
# -----------------------------
app.layout = dbc.Container([
    dbc.Row(
        dbc.Col(html.H1("🚀 SpaceX Falcon 9 Dashboard", className="text-center text-primary mb-4"),
                width=12)
    ),

    dbc.Row([
        dbc.Col([
            html.Label("Select Launch Sites:"),
            dcc.Dropdown(
                id="site-dropdown",
                options=[{"label": site, "value": site} for site in df["launch_site"].dropna().unique()],
                value=None,
                multi=True,
                placeholder="All Sites"
            ),
        ], width=6),

        dbc.Col([
            html.Label("Payload Mass Range (kg):"),
            dcc.RangeSlider(
                id="payload-slider",
                min=df["payload_mass_kg"].min(),
                max=df["payload_mass_kg"].max(),
                step=100,
                value=[df["payload_mass_kg"].min(), df["payload_mass_kg"].max()],
                marks={int(x): str(int(x)) for x in range(0, int(df["payload_mass_kg"].max())+1000, 2000)}
            )
        ], width=6)
    ], className="mb-4"),

    dbc.Row([
        dbc.Col(dcc.Graph(id="payload-hist"), width=6),
        dbc.Col(dcc.Graph(id="yearly-success"), width=6)
    ], className="mb-4"),

    dbc.Row([
        dbc.Col(dcc.Graph(id="map"), width=12)
    ]),

    dbc.Row(
        dbc.Col(html.P(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
                       className="text-center text-muted mt-4"), width=12)
    )
], fluid=True)

# -----------------------------
# Callbacks
# -----------------------------
@app.callback(
    [Output("payload-hist","figure"),
     Output("yearly-success","figure"),
     Output("map","figure")],
    [Input("site-dropdown","value"),
     Input("payload-slider","value")]
)
def update_graphs(selected_sites, payload_range):
    d = df.copy()

    # Filter by site
    if selected_sites:
        d = d[d["launch_site"].isin(selected_sites)]
    
    # Filter by payload range
    d = d[(d["payload_mass_kg"] >= payload_range[0]) & (d["payload_mass_kg"] <= payload_range[1])]

    # Histogram
    fig1 = px.histogram(
        d, x="payload_mass_kg",
        color=d["landing_success"].map({1:"Success",0:"Failure"}),
        nbins=40,
        title="Payload Mass vs Landing Outcome",
        color_discrete_map={"Success":"green","Failure":"red"}
    )
    fig1.update_layout(bargap=0.2, template="plotly_white")

    # Line Chart: Success Rate by Year
    yearly = d.groupby("year")["landing_success"].mean().mul(100).reset_index()
    fig2 = px.line(yearly, x="year", y="landing_success", markers=True,
                   title="Success Rate (%) by Year", template="plotly_white")
    fig2.update_traces(line=dict(color='royalblue', width=3))
    fig2.update_yaxes(range=[0,100], title="Success Rate (%)")
    fig2.update_xaxes(dtick=1)

    # Map of Launch Sites
    site_counts = d.groupby("launch_site")["landing_success"].mean().reset_index()
    site_counts["lat"] = site_counts["launch_site"].map({
        "CCAFS LC-40": 28.5618571,
        "KSC LC-39A": 28.6080585,
        "VAFB SLC-4E": 34.632093,
    })
    site_counts["lon"] = site_counts["launch_site"].map({
        "CCAFS LC-40": -80.577366,
        "KSC LC-39A": -80.604166,
        "VAFB SLC-4E": -120.610829,
    })
    fig3 = px.scatter_mapbox(
        site_counts, lat="lat", lon="lon", size="landing_success",
        hover_name="launch_site", zoom=3, height=500,
        title="Launch Site Success Rate",
        color="landing_success", color_continuous_scale="Viridis"
    )
    fig3.update_layout(mapbox_style="open-street-map")
    fig3.update_traces(marker=dict(sizemode='area', sizeref=0.2))

    return fig1, fig2, fig3

# -----------------------------
# Run App (latest Dash)
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
