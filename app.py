from flask import Flask, render_template

# Inicializar web app
app = Flask(__name__) 

# Primer endpoint (home)
@app.route("/")
def home():
    mensaje = "Endpoints con Flask"
    return render_template("index.html", mensaje=mensaje)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)