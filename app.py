from flask import render_template, request, redirect, url_for, session, flash, jsonify

from syllabus.db.db import app, db

from syllabus.models.user_model import User

from syllabus.routes.faculty_routes import faculty_routes
from syllabus.routes.version_routes import version_routes
from syllabus.routes.syllabus_routes import syllabus_routes
from syllabus.routes.subject_routes import subject_routes
from syllabus.routes.user_routes import user_routes

app.register_blueprint(faculty_routes, url_prefix="/faculty")
app.register_blueprint(subject_routes, url_prefix="/subject")
app.register_blueprint(user_routes, url_prefix="/user")
app.register_blueprint(syllabus_routes, url_prefix="/syllabus")
app.register_blueprint(version_routes, url_prefix="/version")


# Routes - Template Rendering

# Menu / Home
@app.route('/', methods=['GET'])
def menu():
    return render_template('/menu.html')

# Login 
@app.route('/login', methods=['GET', 'POST'])
def login():
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