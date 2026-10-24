from flask import Flask, render_template, request
app = Flask(__name__)

"""ruta raiz"""


@app.route("/")
def base():
    return render_template("base.html")


"""ruta para la teoria"""


@app.route("/teoria")
def teoria():
    return render_template("teoria.html")


"""a para el boton de panico"""


@app.route("/panico")
def panico():
    return render_template("panico.html")


"""rutas para la calculadora"""


@app.route("/calculadora")
def calculadora():
    return render_template("calculadora.html")


"""ruta del calculo de CO2"""


@app.route("/calculo", methods=["POST"])
def calculo():
    """extracción de datos de calculadora.html"""
    auto = request.form.get("auto")
    km_auto = float(request.form.get("km_auto"))
    vuelos = int(request.form.get("vuelos"))
    km_vuelos = float(request.form.get("km_vuelos"))
    duchas = request.form.get("duchas")
    reciclas = request.form.get("reciclaje")
    arbol = request.form.get("arbol")
    N_arboles = int(request.form.get("N_arboles"))

    """estapa de suma al CO2"""
    if auto == "si":
        CO2_km_auto = km_auto * 150
    elif auto == "si_electrico":
        CO2_km_auto = km_auto * 75
    else:
        CO2_km_auto = 0

    """calculo del CO2 por vuelos"""
    CO2_vuelos = vuelos*km_vuelos*196

    """calculo de las duchas diarias"""
    if duchas == "+1duchaXdia":
        CO2_duchas = 3 * 2 * 365
    elif duchas == "duchaXdia":
        CO2_duchas = 3*365
    elif duchas == "ducha_dia/2":
        CO2_duchas = 3 * 183
    else:
        CO2_duchas = 3 * 52
    CO2_total = CO2_km_auto + CO2_vuelos + CO2_duchas
    """estapa de resta del CO2"""
    CO2_reciclada = 0
    if reciclas == "si":
        CO2_a_restar = CO2_total*0.05
        CO2_reciclada -= round(CO2_total-CO2_a_restar)
    elif reciclas == "a_veces":
        CO2_a_restar = CO2_total*0.025
        CO2_reciclada = round(CO2_total-CO2_a_restar)
    else:
        CO2_reciclada = CO2_total
    if arbol == "si":
        CO2_reciclada = CO2_reciclada-(N_arboles*21)
    elif arbol == "plantas":
        CO2_reciclada = CO2_reciclada - 0.5

    else:
        """CO2_final = al valor que se va a returnar"""
        CO2_reciclada = CO2_reciclada
    CO2_final = -(CO2_reciclada)

    """retorna a respuesta.html ni bien se termina el cuestionario"""
    return render_template("resultado.html", resultado_co2=CO2_final)


app.run(debug=True)
