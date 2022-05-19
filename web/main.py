from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import CSRFProtect

from db_cms.db_cms_core import DbCMS

app = Flask(__name__)
csrf = CSRFProtect(app)
bootstrap = Bootstrap5(app)

db = DbCMS('sqlite:///resources/db/app_data.db')


@app.route('/')
def main():
    return 'Hello world'


@app.route('/tax_rates/list')
def tax_rates_list():
    print(db.show_all_tax_rates())
    return render_template('tax_rates.html')


@app.route('/tax_rates/edit/<item_id>')
def tax_rates_edit(item_id):
    text = 'tax rates' + str(item_id)
    return text


@app.route('/tax_rates/new')
def tax_rates_new():
    return 'new tax rate'


@app.route('/login')
def login():
    pass


if __name__ == '__main__':
    app.run(debug=True)
