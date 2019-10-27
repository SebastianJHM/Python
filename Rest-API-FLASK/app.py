# flask es la librería de python que nos permite hacer backend y API
# Para instalar Flask primero instalamos python y luego la línea pip install flask en todo el pc
# La línea {from flask import Flask} importa flask para usarlo
# La linea {app = Flask(__name__)} nos dice que el nombre del app
# -----La sigiente línea ejecuta el programa, es necesaria, en app.run indicamos en que puerto 
# queremos que corra el programa
# if __name__ == '__main__':
#   app.run(debug = True, port=5000)
#--------------------------------------------------------
# Tenemos que usar requests para manejar la petición del Front. pip install requests
# Usamos flask import request para recibir

from flask import Flask, jsonify
from products import products_list
from flask import request

app = Flask(__name__)

# Esta es la forma de declara una ruta en el servidor
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "pong!"})
#fed

# Función de tipo get
@app.route('/products', methods=['GET'])
def function_get():
    # De esta forma la respuesta es una lista
    # return jsonify(products_list)
    # De esta forma la respuesta es una propiedad
    return jsonify({"prods": products_list, "message": "Product's List"})
#fed


# Función de tipo get para obtener solo un elemento de la lista
@app.route('/products/<string:product_name>', methods=['GET'])
def function2_get(product_name):
    product_found = {}
    for p in products_list:
        if ( p["name"] == product_name ):
            product_found = p
        #fi
    #rof

    if (product_found == {}):
        return jsonify({"message": "product don't found"})
    else:
        return jsonify({"product": product_found})
    #fi

    # #Esto es una forma alternativa
    # # Esta es una forma en Python de agrgar todo lo que cumpla la condición del ciclo al vector product_found
    # product_found = [p for p in products_list if p["name"] == product_name]
    # if ( len(product_found) > 0 ):
    #     return jsonify({"product": product_found[0]})
    # else:
    #     return jsonify({"message": "product don't found"})
    # #fi
#fed


# Ruta método POST
@app.route('/products', methods=['POST'])
def addProducts():
    np = request.json
    new_product = {
        "name": np["name"],
        "price": np["price"],
        "quantity": np["quantity"],
        "appoint": np["appoint"]
    }
    products_list.append(new_product)
    return jsonify({"message": "Product added succesfully", "products": products_list})
#fed

# Ruta método PUT
@app.route('/products/<string:product_name>', methods=['PUT'])
def editProducts(product_name):
    edit_product = request.json
    product_found = False

    for p in products_list:
        if ( p["name"] == product_name ):
            product_found = True
            p["name"] = edit_product["name"]
            p["price"] = edit_product["price"]
            p["quantity"] = edit_product["quantity"]
            p["appoint"] = edit_product["appoint"]
        #fi
    #rof

    if (product_found == False):
        return jsonify({"message": "product don't found"})
    else:
        return jsonify({
            "message": "Product updated", 
            "products": products_list
        })
    #fi


    # ---------- OTRA VERSION QUE NO ENTIENDO MUY BIEN --------------------
    # for p in products_list:
    #     if ( p["name"] == product_name ):
    #         product_found = p
    #     #fi
    # #rof

    # if (product_found == {}):
    #     return jsonify({"message": "product don't found"})
    # else:
    #     product_found["name"] = edit_product["name"]
    #     product_found["price"] = edit_product["price"]
    #     product_found["quantity"] = edit_product["quantity"]
    #     product_found["appoint"] = edit_product["appoint"]
    #     return jsonify({
    #         "message": "Product updated", 
    #         "products": products_list
    #     })
    # #fi
#fed

# Ruta método DELETE
@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProducts(product_name):
    product_found = False

    product_found = {}
    for p in products_list:
        if ( p["name"] == product_name ):
            product_found = p
        #fi
    #rof

    if (product_found == {}):
        return jsonify({"message": "product don't found"})
    else:
        products_list.remove(product_found)
        return jsonify({
            "message": "Product deleted", 
            "products": products_list
        })
    #fi
#fed


if __name__ == '__main__':
    app.run(debug = False, port=4000)
#fi