from flask import Flask, render_template, request, jsonify
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
    return render_template("items.html", items=items)

# POST
@app.route("/items", methods=["POST"])
def post_item():
    name = request.form.get("name")
    if not name:
        return "Coloca un nombre", 400
    
    items.append(name)
    return jsonify({"message": "Item agregado", "items": items})

@app.route("/upload", method=["POST"])
def upload_file():
    file = request.files.get("file")
    if not file:
        return "Archivo no enviado", 404
    
    file.save(os.path.join(UPLOAD_DIRECT, file.filename))
    return jsonify({"message": "Archivo guardado", "filename": file.filename})

# PUT
@app.route("items/<int:index>", methods=["PUT"])
def update_item(index:int):
    data = request.json
    try:
        items[index] = data["name"]
        return jsonify({"message": "Item actualizado"})
    except IndexError:
        return jsonify({"error": "Item no existe"}), 404
    
# DELETE
@app.route("items/<int:index>", methods="DELETE")
def delete_item(index):
    try:
        items.pop(index)
        return jsonify({"message": "Item eliminado"})
    except IndexError:
        return jsonify({"error": "Item no existe"}), 404
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)