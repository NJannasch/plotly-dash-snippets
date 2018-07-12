import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)
server = app.server

# Configure navbar menu
nav_menu = html.Div([
    html.Ul([
            html.Li([
                    dcc.Link('First', href='/first')
                    ], className='active'),
            html.Li([
                    dcc.Link('Second', href='/second')
                    ]),
            html.Li([
            dcc.Link('Third', href='/third')
                    ]),
            ], className='nav navbar-nav')
], className='navbar navbar-default navbar-static-top')

# Define layout
app.layout = html.Div([
    nav_menu,
])

# Add bootstrap css
app.css.append_css({"external_url": [
    "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"
]})

if __name__ == '__main__':
    app.run_server(debug=True)