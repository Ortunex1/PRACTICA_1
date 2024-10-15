from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta para la página de inicio
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para la página de "Quiénes Somos"
@app.route('/about')
def about():
    return render_template('about.html')

# Ruta para la página de "Servicios"
@app.route('/services')
def services():
    return render_template('services.html')

# Ruta para la página de "Noticias"
@app.route('/news')
def news():
    return render_template('news.html')

# Ruta para la página de "Contacto"
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        mensaje = request.form['mensaje']
        return f"Gracias por tu mensaje, {nombre}. Nos pondremos en contacto contigo pronto."
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
