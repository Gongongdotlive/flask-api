from flask import Blueprint

route_blp = Blueprint('routes', __name__)

route_blp.route('/api')
def index():
    return "THis is our api"
