# Use local CSS

To use a local CSS file within plotly dash we must serve it via our server.  
As dash runs with flask we can use flask to also serve our CSS file.

Requirement: the relative path to our CSS file is: *static/stylesheet.css*
```
# Serving local static files
@app.server.route('/static/<path:path>')
def static_file(path):
    static_folder = os.path.join(os.getcwd(), 'static')
    return send_from_directory(static_folder, path)
```

Now we can include our CSS:
```
app.css.append_css({"external_url": [
    "static/stylesheet.css"
]})
```

A full working example can be found in  
[Python3 - Use local css](examples/use-local-css.py)
