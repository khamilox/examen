from flask import Flask, render_template, request

app = Flask(__name__)

# ---------- Función para formatear moneda CLP ----------
def formato_clp(valor):
    return f"${valor:,.0f}".replace(",", ".")


@app.route('/')
def home():
    return render_template('index.html')


# ------------------ EJERCICIO 1 ------------------
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        tarros = int(request.form['tarros'])

        precio_unitario = 9000
        total_sin_desc = tarros * precio_unitario

        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0.0

        total_con_desc = total_sin_desc - (total_sin_desc * descuento)

        return render_template(
            'ejercicio1_resultado.html',
            nombre=nombre,
            edad=edad,
            tarros=tarros,
            total_sin_desc=formato_clp(total_sin_desc),
            total_con_desc=formato_clp(total_con_desc),
            descuento_porcentaje=int(descuento * 100)
        )

    return render_template('ejercicio1.html')


# ------------------ EJERCICIO 2 ------------------
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    usuarios = {
        "juan": "admin",
        "pepe": "user"
    }

    mensaje = ""

    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']

        if usuario in usuarios and usuarios[usuario] == password:
            if usuario == "juan":
                mensaje = "Bienvenido administrador juan"
            else:
                mensaje = "Bienvenido usuario pepe"
        else:
            mensaje = "Usuario o contraseña incorrectos"

        return render_template('ejercicio2_resultado.html', mensaje=mensaje)

    return render_template('ejercicio2.html')


if __name__ == '__main__':
    app.run(debug=True)
