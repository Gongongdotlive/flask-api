from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# connection string mysql://root:root@localhost/mydatabase
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/gong_new'
db = SQLAlchemy(app)