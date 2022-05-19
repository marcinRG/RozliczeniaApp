from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import CSRFProtect

from db_cms.db_cms_core import DbCMS
from forms.tax_rates_forms import TaxRatesForm

app = Flask(__name__)
csrf = CSRFProtect(app)
bootstrap = Bootstrap5(app)
app.secret_key = 'NFcT&jCOn#ekRB~qyh9gSAso*l2+pXYUwDHt!PI5'

db = DbCMS('sqlite:///resources/db/app_data.db')


@app.route('/')
def main():
    return 'Hello world'


@app.route('/tax_rates/list')
def tax_rates_list():
    list_data = db.show_all_tax_rates()
    return render_template('tax_rates.html', list_data=list_data)


@app.route('/tax_rates/edit/<item_id>')
def tax_rates_edit(item_id):
    form = TaxRatesForm()
    return render_template('tax_rates.html', form=form, page_state='edit')


@app.route('/tax_rates/new')
def tax_rates_new():
    return 'new tax rate'


@app.route('/login')
def login():
    pass


if __name__ == '__main__':
    app.run(debug=True)
