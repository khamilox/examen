from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        # Convertir comas a puntos antes de transformar a float
        n1 = float(request.form['nota1'].replace(',', '.'))
        n2 = float(request.form['nota2'].replace(',', '.'))
        n3 = float(request.form['nota3'].replace(',', '.'))
        asistencia = float(request.form['asistencia'].replace(',', '.'))

        promedio = round((n1 + n2 + n3) / 3, 1)
        estado = "APROBADO" if promedio >= 4.0 and asistencia >= 75 else "REPROBADO"

        resultado = {
            "promedio": promedio,
            "asistencia": asistencia,
            "estado": estado
        }

        return render_template("ejercicio1.html", resultado=resultado)

    return render_template("ejercicio1.html", resultado=None)


@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    resultado = None
    if request.method == "POST":
        n1 = request.form["nombre1"]
        n2 = request.form["nombre2"]
        n3 = request.form["nombre3"]

        nombres = [n1, n2, n3]
        nombre_mas_largo = max(nombres, key=len)
        largo = len(nombre_mas_largo)

        resultado = {
            "nombre": nombre_mas_largo,
            "largo": largo
        }

    return render_template("ejercicio2.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
