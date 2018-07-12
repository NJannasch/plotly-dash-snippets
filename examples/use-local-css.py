import dash
import dash_html_components as html

from flask import send_from_directory
import os

app = dash.Dash(__name__)
server = app.server

# Define layout
app.layout = html.Div('Local CSS is served', className='content')

# Add css file (locally hosted)
app.css.append_css({"external_url": [
    "static/stylesheet.css"
]})

# Serving local static files
@app.server.route('/static/<path:path>')
def static_file(path):
    static_folder = os.path.join(os.getcwd(), 'static')
    return send_from_directory(static_folder, path)

if __name__ == '__main__':
    app.run_server(debug=True)