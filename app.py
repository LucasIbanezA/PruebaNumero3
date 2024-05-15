from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    promedio = None
    estado = None
    if request.method == 'POST':
        notas = [float(request.form['nota1']), float(request.form['nota2']), float(request.form['nota3'])]
        asistencia = int(request.form['asistencia'])

        promedio = sum(notas) / len(notas)
        estado = 'Aprobado' if promedio >= 40 and asistencia >= 75 else 'Reprobado'

    return render_template('ejercicio1.html', promedio=promedio, estado=estado)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    nombre_largo = None
    caracteres = None
    if request.method == 'POST':
        nombres = [request.form['nombre1'], request.form['nombre2'], request.form['nombre3']]

        nombre_largo = max(nombres, key=len)
        caracteres = len(nombre_largo)

    return render_template('ejercicio2.html', nombre_largo=nombre_largo, caracteres=caracteres)

if __name__ == '__main__':
    app.run(debug=True)
