import json
import functools
from flask import (render_template, redirect, blueprints,
                   session, request, url_for,)
from werkzeug.security import check_password_hash, generate_password_hash
from controllers import *

main = blueprints.Blueprint('main', __name__)

# ------------------------ Template Rendering ------------------------
