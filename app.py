from flask import Flask, redirect, render_template, request, jsonify, url_for
import os

# Inicializar web app
app = Flask(__name__) 

UPLOAD_DIRECT = "uploads"
os.makedirs(UPLOAD_DIRECT, exist_ok=True)

# DB
items = []

# ENDPOINTS =======

# GET
@app.route("/")
def home():
    mensaje = "Endpoints con Flask"
    return render_template("index.html", mensaje=mensaje)

@app.route("/items", methods=["GET"])
def get_items():
    return render_template("items.html", items=items, mensaje="Lista de items")

# POST
@app.route("/items", methods=["POST"])
def post_item():
    name = request.form.get("name")
    if not name:
        return "Coloca un nombre", 400
    
    items.append(name)
    return redirect(url_for('get_items'))

@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files.get("file")
    if not file:
        return "Archivo no enviado", 404

    filepath = os.path.join(UPLOAD_DIRECT, file.filename)
    file.save(filepath)

    # Leer contenido
    file.seek(0)
    contenido = file.read().decode("utf-8")

    # Renderizar template
    return render_template("upload_result.html",
                           filename=file.filename,
                           contenido=contenido)


# PUT
@app.route("/items/<int:index>", methods=["PUT"])
def update_item(index:int):
    data = request.json
    try:
        items[index] = data["name"]
        return jsonify({"message": "Item actualizado"})
    except IndexError:
        return jsonify({"error": "Item no existe"}), 404
    
# DELETE
@app.route("/items/<int:index>", methods=["DELETE"])
def delete_item(index):
    try:
        items.pop(index)
        return jsonify({"message": "Item eliminado"})
    except IndexError:
        return jsonify({"error": "Item no existe"}), 404
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)