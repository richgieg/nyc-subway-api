import json
from flask import Flask, Response

app = Flask(__name__)


@app.route('/stations')
def stations():
    try:
        with open('data.json', 'r') as data_file:
            data = data_file.read()
    except:
        data = ''
    return Response(
        response=data,
        status=200,
        mimetype='application/json'
    )


if __name__ == '__main__':
    app.run()
