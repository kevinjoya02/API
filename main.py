from flask import Flask, jsonify, request # type: ignore #impotar librerias

app = Flask(__name__)  #crear aplicacion flask
@app.route('/')        #ruta principal 
def root():
    return """
    BIENVENIDO A MI API
   """
   
   
#base de datos (lista)
productos = [{"nombre":"camisa", "color":"azul"}]

#----------CRUD-----------#

#servicio GET (ver las los datos)  
@app.route('/productos', methods = ['GET'])
def ver_productos():
    return jsonify(productos),200 #codigo http  "OK"

#servicio POST (insertar datos)
@app.route('/productos', methods = ['POST'])
def agregar_productos():
    data = request.get_json()
    if not data or "nombre" not in data:
        return jsonify({"error": "El producto debe tener un nombre"})
    
    productos.append(data)   #guarda los datos en la lista 
    return jsonify(data)

#servicio PUT (actualizar datos)
@app.route('/productos/<int:inbdice>', methods = ['PUT'])
def actualizar(indice):
    if indice < 0 or indice >= len(productos):
        return jsonify({"error al actualizar"})
    data = request.get_json()  #recibir el json del postman
    productos[indice].update(data)
    return jsonify (productos[indice])

#servicio DELETE (eliminar)
@app.route('/productos/<int:indice>', methods = ['DELETE'])
def eliminar_producto(indice):
    if indice < 0 or indice >= len(productos):
        return jsonify({"indice desconocido"})
    eliminado = productos.pop(indice)  # quitar el producto de la lista
    return jsonify({
        "mensaje": "se eliminó el producto",
        "producto": eliminado
        })

if __name__ == "__main__":       #ejecutar el archivo directamente
    app.run(debug=True)         #iniciar servidor (modo debug: autorecarga y errores)
    
    
