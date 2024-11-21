from chalice import Chalice

app = Chalice(app_name='sample-api')


@app.route('/')
def index():
    return {'wassup': 'girl'}


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}#
