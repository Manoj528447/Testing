from dash import Dash, html

app = Dash(__name__)

app.layout = html.Div("Dash working")

server = app.server

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8050)
