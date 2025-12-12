from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def calculadora():
    pantalla = request.form.get("pantalla", "0")
    boton = request.form.get("boton")

    #
    # Este código es para recibir señales del formulario que se encuentra en la calculadora.html
    #
    if boton:
        if boton == "C":
            pantalla = "0"

        elif boton == "=":
            try:
                pantalla = str(eval(pantalla))
            
            except:
                pantalla = "Error"

        else:
            if pantalla == "0":
                pantalla = boton

            else:
                pantalla += boton

    return render_template("calculadora.html", pantalla=pantalla)
