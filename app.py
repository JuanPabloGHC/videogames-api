from flask import Flask, render_template, jsonify, abort, request
import json

app = Flask(__name__)

uri = '/api/videogames'

with open('data.json', 'r') as file:
    data = json.load(file)

#GET------------------------------------------------------
#HOME
@app.route(uri, methods=['GET'])
def get_info():
    return jsonify(data)
#ID
@app.route(uri + "/item/<int:id>", methods=['GET'])
def get_item(id):
    itemTemp = []
    for item in data:
        if item['id'] == id:
            itemTemp.append(item)
    if itemTemp == 0:
        abort(404)
    return jsonify(itemTemp)
#NAME
@app.route(uri + "/name/<string:name>", methods=['GET'])
def get_name(name):
    itemTemp = []
    for item in data:
        if item['name'] == name:
            itemTemp.append(item)
    if itemTemp == 0:
        abort(404)
    return jsonify(itemTemp)
#AUTOR
@app.route(uri + "/autor/<string:autor>", methods=['GET'])
def get_autor(autor):
    itemTemp=[]
    for item in data:
        if item['autor'] == autor:
            itemTemp.append(item)
    if itemTemp == 0:
        abort(404)
    return jsonify(itemTemp)
#ANIO
@app.route(uri + "/anio/<string:anio>", methods=['GET'])
def get_anio(anio):
    itemTemp=[]
    for item in data:
        if item['anio'] == anio:
            itemTemp.append(item)
    if itemTemp == 0:
        abort(404)
    return jsonify(itemTemp)

#POST------------------------------------------------------
@app.route(uri, methods=['POST'])
def create_videogame():
    #Se recibe un json?
    if request.json:
        if request.json['name'] != '' and request.json['autor'] != '' and request.json['anio'] != '' and request.json['descripcion'] != '' and request.json['image1'] != '' and request.json['image2'] != '':
            game = {
                'id': len(data) + 1,
                'name': request.json['name'],
                "autor": request.json['autor'],
                "anio": request.json['anio'],
                "descripcion": request.json['descripcion'],
                "image1": request.json['image1'],
                "image2": request.json['image2']
            }
            data.append(game)

        return jsonify({'data': data}), 201
        # status: 200 -> OK, 201 -> ok de creación
    else:
        abort(404)

#PUT------------------------------------------------------
@app.route(uri + '/<int:id>', methods=['PUT'])
def update_videogame(id):
    #Se recibe un json?
    if request.json:
        #Buscar elemento con el id en la lista de videogames
        this_game = [game for game in data if game['id'] == id]
        #Si existe la tarea con el id
        if this_game:
            #Se recibe un name para actualizar
            if request.json.get('name'):
                this_game[0]['name'] = request.json['name']
            #Se recibe un autor para actualizar
            if request.json.get('autor'):
                this_game[0]['autor'] = request.json['autor']
            #Se recibe un anio para actualizar
            if request.json.get('anio'):
                this_game[0]['anio'] = request.json['anio']
            #Se recibe una descripcion para actualizar
            if request.json.get('descripcion'):
                this_game[0]['descripcion'] = request.json['descripcion']
            #Se recibe un link de la imagen 1 para actualizar
            if request.json.get('image1'):
                this_game[0]['image1'] = request.json['image1']
            #Se recibe un link de la imagen 2 para actualizar
            if request.json.get('image2'):
                this_game[0]['image2'] = request.json['image2']
        else:
            abort(404)        
    else:
        abort(404)
    
    return jsonify({'data': this_game[0]})

#DELETE------------------------------------------------------
@app.route(uri + '/<int:id>', methods=['DELETE'])
def delete_videogame(id):
    #Buscar elemento con el id en la lista de data
    this_game= [game for game in data if game['id'] == id]
    if this_game:
        data.remove(this_game[0])
    else:
        abort(404)
    
    return jsonify({'data': this_game[0]})



if __name__ == '__main__':
    app.run(debug = True)
