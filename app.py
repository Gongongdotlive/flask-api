from flask import Flask, render_template, make_response, jsonify, request
# from werkzeug import generate_password_hash,check_password_hash
import pymysql
from flaskext.mysql import MySQL

# from routes import routes

app = Flask(__name__)

mysql = MySQL()
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'gong_new'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

# THIS SHOULD BE A SEPERATE ROUTES FILE 

@app.route('/api/v1/users/all')
def index():

    try:
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute('SELECT * from wp_wswebinars_subscribers;')
        rows = cur.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)

    finally:
        cur.close()
        conn.close()

@app.errorhandler(404)
def page_not_found(error):

    return render_template('nferror.html', bodyClass="error-page"), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)
