from flask import Flask, render_template, jsonify, abort, request
import json

app = Flask(__name__)

uri = '/api/videogames'

with open('data.json', 'r') as file:
    data = json.load(file)

@app.route(uri, methods=['GET'])
def get_info():
    return jsonify(data)

@app.route(uri + "/item/<int:id>", methods=['GET'])
def get_item(id):
    itemTemp = []
    for item in data:
        if item['id'] == id:
            itemTemp.append(item)
    if itemTemp == 0:
        abort(404)
    return jsonify(itemTemp)

@app.route(uri + "/name/<str:name>", methods=['GET'])
def get_item(name):
    itemTemp = []
    for item in data:
        if item['name'] == name:
            itemTemp.append(item)
    if itemTemp == 0:
        abort(404)
    return jsonify(itemTemp)

if __name__ == '__main__':
    app.run(debug = True)
