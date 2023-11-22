from flask import render_template, request, redirect, url_for, session, flash, jsonify
from sqlalchemy import Enum
from datetime import datetime

from syllabus.db.db import app, db

# Creación de tablas

# Tablas Independientes
from syllabus.models.subjects_model import Subjects
from syllabus.models.faculties_model import Faculties

# Tablas Dependientes
from syllabus.models.users_model import Users
from syllabus.models.syllabi_model import Syllabi
from syllabus.models.versions_model import Versions
from syllabus.models.evaluations_model import Evaluations
from syllabus.models.contentsAndStrategies_model import ContentsAndStrategies

# Tablas Intermedias
from syllabus.models.users_subjects_model import UsersSubjects
from syllabus.models.faculties_subjects_model import FacultiesSubjects

# Importación de las rutas HTTP
from syllabus.routes.faculties_routes import faculties_routes
from syllabus.routes.versions_routes import versions_routes
from syllabus.routes.syllabi_routes import syllabi_routes
from syllabus.routes.subjects_routes import subjects_routes
from syllabus.routes.users_routes import users_routes
from syllabus.routes.users_subjects_routes import users_subjects_routes
from syllabus.routes.faculties_subjects_routes import faculties_subjects_routes

app.register_blueprint(faculties_routes, url_prefix="/faculties")
app.register_blueprint(subjects_routes, url_prefix="/subjects")
app.register_blueprint(users_routes, url_prefix="/users")
app.register_blueprint(syllabi_routes, url_prefix="/syllabi")
app.register_blueprint(versions_routes, url_prefix="/versions")
app.register_blueprint(users_subjects_routes, url_prefix="/users_subjects")
app.register_blueprint(faculties_subjects_routes, url_prefix="/faculties_subjects")


# Routes - Template Rendering


# Menu / Homes
@app.route("/", methods=["GET"])
def menu():
    if "user_id" in session:
        user_id = session["user_id"]
        user = Users.query.get(user_id)

        # Consulta de las materias por usuario
        user_subjects = (
            db.session.query(Subjects)
            .join(UsersSubjects)
            .filter(UsersSubjects.users_id == user_id)
            .all()
        )
        data = [{"id": subject.id, "name": subject.name} for subject in user_subjects]

        return render_template("/menu.html", username=user.name, data=data)
    else:
        return redirect(url_for("login"))


# Login
@app.route("/login", methods=["GET", "POST"])
def login():
    if "user_id" in session:
        return redirect(url_for("menu"))
    else:
        if request.method == "POST":
            email = request.form["emailInput"]
            password = request.form["passwordInput"]

            user = Users.query.filter_by(email=email, password=password).first()

            if user:
                session["user_id"] = user.id
                print("Inicio de sesión exitoso")
                return redirect(url_for("menu"))
            else:
                print("Credenciales incorrectas")
                return redirect(url_for("login"))

    return render_template("login.html")


# Admin option panel
@app.route("/admin/options", methods=["GET"])
def admin():
    # Si no hay sesión iniciada va a login
    if "user_id" not in session:
        return redirect(url_for("login"))

    user_id = session["user_id"]
    user = Users.query.get(user_id)

    if user.role == "admin":
        return render_template("/adminPanel.html")
    else:
        return render_template("/adminDenegado.html")


# Editor online
@app.route("/editor/<int:subject_id>", methods=["GET"])
def editor_by_id(subject_id):
    if "user_id" in session:
        syllabus_id = (
            db.session.query(Syllabi.id)
            .filter(Syllabi.subject_id == subject_id)
            .first()[0]
        )

        # Consultas a la base de datos
        syllabus = db.session.query(Syllabi).filter(Syllabi.id == syllabus_id).first()

        evaluations = (
            db.session.query(Evaluations)
            .filter(Evaluations.syllabus_id == syllabus_id)
            .first()
        )

        faculty = (
            db.session.query(Faculties)
            .filter(Faculties.id == syllabus.faculty_id)
            .first()
        )
        subject = (
            db.session.query(Subjects)
            .filter(Subjects.id == syllabus.subject_id)
            .first()
        )

        teachers = (
            db.session.query(Users)
            .join(UsersSubjects, Users.id == UsersSubjects.users_id)
            .filter(UsersSubjects.subjects_id == syllabus.subject_id)
            .all()
        )
        versions = (
            db.session.query(Versions).filter(Versions.syllabus_id == syllabus_id).all()
        )

        contents_and_strategies = (
            db.session.query(ContentsAndStrategies)
            .filter(ContentsAndStrategies.syllabus_id == syllabus_id)
            .all()
        )

        # Formatear consultas en JSON
        syllabus_data = {
            "id": syllabus.id,
            "date": syllabus.date,
            "program": syllabus.program,
            "cycle": syllabus.cycle,
            "justification": syllabus.justification,
            "competences": syllabus.competences,
            "learning_results": syllabus.learning_results,
            "methodology": syllabus.methodology,
            "faculty_id": syllabus.faculty_id,
            "subjects_id": syllabus.subject_id,
        }

        faculty_data = {"id": faculty.id, "name": faculty.name}

        subject_data = {
            "id": subject.id,
            "name": subject.name,
            "modality": subject.modality,
            "type": subject.type,
            "credits": subject.credits,
            "semester": subject.semester,
            "bibliography": subject.bibliography,
        }

        teachers_data = [
            {
                "name": teacher.name,
            }
            for teacher in teachers
        ]

        contentsAndStrategies_data = [
            {
                "id": content.id,
                "content_name": content.content_name,
                "sub_content": content.sub_content,
                "strategies": content.strategies,
                "syllabus_id": content.syllabus_id
                # Agrega más campos según sea necesario
            }
            for content in contents_and_strategies
        ]
        evaluations_data = {
            "first_percentage": evaluations.first_percentage,
            "description_first_percentage": evaluations.description_first_percentage,
            "second_percentage": evaluations.second_percentage,
            "description_second_percentage": evaluations.description_second_percentage,
            "third_percentage": evaluations.third_percentage,
            "description_third_percentage": evaluations.description_third_percentage,
        }

        versions_data = [
            {
                "id": version.id,
                "update_date": version.update_date.isoformat(),
                "description": version.description,
                "user_id": version.user_id,
                "syllabus_id": version.syllabus_id,
            }
            for version in versions
        ]

        return render_template(
            "/editor.html",
            # Mandar JSON para el HTML
            syllabus_data=syllabus_data,
            faculty_data=faculty_data,
            subject_data=subject_data,
            teachers_data=teachers_data,
            contentsAndStrategies_data=contentsAndStrategies_data,
            evaluations_data=evaluations_data,
            versions_data=versions_data,
        )

    else:
        return redirect(url_for("login"))


# Cerrar sesión
@app.route("/logout")
def logout():
    session.pop("user_id", None)
    print("Cierre de sesión exitoso")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
