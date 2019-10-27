from flask import Flask, jsonify, request
from libros import libros_list
from datetime import datetime
from datetime import date
from flask_cors import CORS, cross_origin




app = Flask(__name__)
cors = CORS(app)

@app.route('/libros', methods = ['GET'])
@cross_origin()
def function_get():
    return jsonify(libros_list)
#fed

@app.route('/addlibro', methods = ['POST'])
@cross_origin()
def function_post():
    r = request.json
    nuevo_libro = {
        "autor": r["autor"],
        "nombre": r["nombre"],
        "fecha": r["fecha"]
    }
    libros_list.append(nuevo_libro)
    return jsonify(libros_list)
#fed



if __name__ == '__main__':
    app.run(debug = False, port=4000)
#fi..