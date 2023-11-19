from app.routes.routes import main
import os
from flask import Flask, render_template, url_for, session, redirect

app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = os.urandom(50)

app.register_blueprint(main)

if __name__ == '__main__':
    app.run(debug=True)

# Routes - Template Rendering

# Menu / Home
@main.route('/menu', methods=['GET'])
def menu():
    return render_template('/menu.html')

# Login 
@main.route('/login', methods=['GET'])
def login():
    return render_template('/login.html')

# Admin option panel
@main.route('/admin/options', methods=['GET'])
def admin():
    return render_template('/adminPanel.html')

# Admin panel
@main.route('/admin/denied')
def admin_denied():
    return render_template('/adminDenegado.html')

# Editor online
@main.route('/editor', methods=['GET'])
def editor():
    return render_template('/editor.html')

# Cerrar sesión
@main.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('menu'))
