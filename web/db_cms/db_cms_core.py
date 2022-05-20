from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Unicode, ForeignKey, Boolean, Numeric
from sqlalchemy import Date, insert, select, delete, update


class DbCMS:

    def __init__(self, db_connection_string):
        self.__engine__ = create_engine(db_connection_string)
        self.__metadata__ = MetaData()
        self.__initialize_tables__()
        self.__metadata__.create_all(self.__engine__)

    def __initialize_tables__(self):
        self.tax_rates = Table('tax_rates', self.__metadata__,
                               Column('id', Integer(), primary_key=True, autoincrement=True),
                               Column('name', String(35), nullable=True),
                               Column('symbol', String(3), nullable=False),
                               Column('rate', Numeric(), nullable=False),
                               Column('default', Boolean(), nullable=True))

        self.measurement_units = Table('measurement_units', self.__metadata__,
                                       Column('id', Integer(), primary_key=True, autoincrement=True),
                                       Column('name', String(35), nullable=False),
                                       Column('unit_symbol', String(3), nullable=False))

        self.items_categories = Table('items_categories', self.__metadata__,
                                      Column('id', Integer(), primary_key=True, autoincrement=True),
                                      Column('name', String(35), nullable=False),
                                      Column('description', Unicode()))

        self.operations = Table('operations', self.__metadata__,
                                Column('id', Integer(), primary_key=True, autoincrement=True),
                                Column('name', String(15), nullable=False))

        self.companies = Table('companies', self.__metadata__,
                               Column('id', Integer(), primary_key=True, autoincrement=True),
                               Column('short_name', String(15), nullable=False),
                               Column('name', Unicode()),
                               Column('name_cont', Unicode()),
                               Column('postal_code', String(7)),
                               Column('VAT_number', String(15)),
                               Column('city', String(25)),
                               Column('street', String(35)))

        self.items = Table('items', self.__metadata__,
                           Column('id', Integer(), primary_key=True, autoincrement=True),
                           Column('category_id', ForeignKey('items_categories.id')),
                           Column('measurement_id', ForeignKey('measurement_units.id')),
                           Column('short_name', String(15), nullable=False),
                           Column('name', Unicode()))

        self.documents = Table('documents', self.__metadata__,
                               Column('id', Integer(), primary_key=True, autoincrement=True),
                               Column('document_title', String(50), nullable=False),
                               Column('date', Date(), nullable=False),
                               Column('document_sum', Numeric(), nullable=False),
                               Column('operation_id', ForeignKey('operations.id')),
                               Column('description', Unicode()))

        self.documents_details = Table('documents_details', self.__metadata__,
                                       Column('id', Integer(), primary_key=True, autoincrement=True),
                                       Column('item_id', ForeignKey('operations.id')),
                                       Column('document_id', ForeignKey('documents.id')),
                                       Column('tax_id', ForeignKey('tax_rates.id')),
                                       Column('price_per_one', Numeric(), nullable=False),
                                       Column('price_all', Numeric(), nullable=False),
                                       Column('quantity', Numeric(), nullable=False),
                                       Column('mass_per_piece', Numeric(), nullable=True))

    def __add_new_from_dict(self, values_dict, table):
        ins = insert(table).values(values_dict)
        with self.__engine__.connect() as conn:
            conn.execute(ins)

    def __show_all_elements(self, table):
        selected = select([table])
        with self.__engine__.connect() as conn:
            return conn.execute(selected).all()

    def __remove_element(self, table, element_id):
        remove_op = delete(table).where(table.c.id == element_id)
        with self.__engine__.connect() as conn:
            return conn.execute(remove_op)

    def __get_element(self, table, element_id):
        elem = select([table]).where(table.c.id == element_id)
        with self.__engine__.connect() as conn:
            return conn.execute(elem).fetchone()

    def __edit_element(self, table, element_id, values_dict):
        update_op = update(table).where(table.c.id == element_id)
        update_op = update_op.values(values_dict)
        with self.__engine__.connect() as conn:
            conn.execute(update_op)

    def add_tax_rate(self, values_dict):
        self.__add_new_from_dict(values_dict, self.tax_rates)

    def remove_tax_rate(self, element_id):
        return self.__remove_element(self.tax_rates, element_id)

    def show_all_tax_rates(self):
        return self.__show_all_elements(self.tax_rates)

    def edit_tax_rate(self, element_id, new_values):
        return self.__edit_element(self.tax_rates, element_id, new_values)

    def get_tax_rate(self, element_id):
        return self.__get_element(self.tax_rates, element_id)

    def add_unit(self):
        pass

    def edit_category(self):
        pass

    def remove_category(self):
        pass

    def add_category(self):
        pass

    def get_tables(self):
        return self.__engine__.table_names()

    def get_companies_columns(self):
        return self.companies.columns


db = DbCMS('sqlite:///resources/db/app_data.db')