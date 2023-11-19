from app.routes.routes import main
from app.database.db import search
import os
from flask import Flask, render_template, url_for, session, redirect, request

app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = os.urandom(50)

app.register_blueprint(main)

app.template_folder = 'app/templates'
app.static_folder = 'app/static'

# Routes - Template Rendering



# Menu / Home
@app.route('/menu', methods=['GET'])
def menu():
    return render_template('/menu.html')

# Login 
@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user_id' in session:
        return redirect(url_for('menu'))
    else: 
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']

            user = search('users', '1')

            if user:
                session['user_id'] = user.id
                print('Inicio de sesión exitoso')
                return redirect(url_for('menu'))
            else:
                print('Credenciales incorrectas')
                return redirect(url_for('login'))

    return render_template('login.html')

# Admin option panel
@app.route('/admin/options', methods=['GET'])
def admin():
    return render_template('/adminPanel.html')

# Admin panel
@app.route('/admin/denied')
def admin_denied():
    return render_template('/adminDenegado.html')

# Editor online
@app.route('/editor', methods=['GET'])
def editor():
    return render_template('/editor.html')

# Cerrar sesión
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('menu'))

if __name__ == '__main__':
    app.run(debug=True)