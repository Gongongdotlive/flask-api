# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from app import app
from flaskext.mysql import MySQL


# connection string mysql://root:root@localhost/mydatabase
# app = Flask(__name__)
connStr = 'mysql://root:root@localhost/gong_new'
# app.config['SQLALCHEMY_DATABASE_URI'] = connStr
# db = SQLAlchemy(app)

mysql = MySQL()
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'gong_new'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
