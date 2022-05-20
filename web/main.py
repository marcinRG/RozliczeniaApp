from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import CSRFProtect

from blueprints.tax_rates import tax_rates_blueprint
from db_cms.db_cms_core import db
from forms.tax_rates_forms import TaxRatesForm

app = Flask(__name__)
csrf = CSRFProtect(app)
bootstrap = Bootstrap5(app)
app.secret_key = 'NFcT&jCOn#ekRB~qyh9gSAso*l2+pXYUwDHt!PI5'

app.register_blueprint(tax_rates_blueprint)

@app.route('/')
def main():
    return 'Hello world'

@app.route('/login')
def login():
    pass


if __name__ == '__main__':
    app.run(debug=True)
