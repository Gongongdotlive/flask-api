from flask import Flask, render_template, make_response


app = Flask(__name__)


# THIS SHOULD BE A SEPERATE ROUTES FILE 

@app.route('/')
def index():

    resp = make_response(render_template('index.html', bodyClass="loading"))
    # resp.set_cookie("audioAllowed", "true")

    return resp

@app.errorhandler(404)
def page_not_found(error):

    return render_template('nferror.html', bodyClass="error-page"), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)
