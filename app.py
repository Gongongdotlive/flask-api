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


@app.route('/')
def index():

    resp = make_response(render_template('index.html', bodyClass="loading"))
    return resp


@app.route('/api/v1/users/all')
def api():

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


# fetch all emails only
@app.route('/api/v1/users/emails')
def emails():

    try:
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        # cur.execute('SELECT EMAIL from wp_wswebinars_subscribers WHERE WEBINAR_ID="10";')
        cur.execute('SELECT EMAIL from wp_wswebinars_subscribers;')
        rows = cur.fetchall()
        resp = jsonify(rows)
        return resp

        # resp.status_code = 200
        
    except Exception as e:
        print(e)

    finally:
        cur.close()
        conn.close()

# fetch all


@app.errorhandler(404)
def page_not_found(error):

    return render_template('nferror.html', bodyClass="error-page"), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)
