To create a navbar in plotly-dash we can also use bootstrap.  
The menu can be defined like this:

```
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
```

To make use of the bootstrap library we also make to include this inside our python code:
```
app.css.append_css({"external_url": [
    "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"
]})
```

A full working example can be found in  
[Python3 - Navbar Bootstrap](examples/Navbar-Bootstrap.py)
