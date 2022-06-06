from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import CSRFProtect

from blueprints.tax_rates_bp import tax_rates_blueprint
from blueprints.units_bp import units_blueprint
from blueprints.categories_bp import categories_blueprint
from blueprints.operations_bp import operations_blueprint
from blueprints.companies_bp import companies_blueprint
from blueprints.documents_bp import documents_blueprint
from blueprints.items_bp import items_blueprint

app = Flask(__name__)
csrf = CSRFProtect(app)
bootstrap = Bootstrap5(app)
app.secret_key = 'NFcT&jCOn#ekRB~qyh9gSAso*l2+pXYUwDHt!PI5'

app.register_blueprint(tax_rates_blueprint)
app.register_blueprint(units_blueprint)
app.register_blueprint(categories_blueprint)
app.register_blueprint(operations_blueprint)
app.register_blueprint(companies_blueprint)
app.register_blueprint(documents_blueprint)
app.register_blueprint(items_blueprint)


@app.route('/')
def main():
    return 'Hello world'


@app.route('/login')
def login():
    pass


if __name__ == '__main__':
    app.run(debug=True)
