from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Unicode, ForeignKey, Boolean, Numeric
from sqlalchemy import Date, insert, select, delete, update, join


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
                               Column('street', String(35)),
                               Column('postal_code', String(7)),
                               Column('VAT_number', String(15)),
                               Column('city', String(25)))

        self.items = Table('items', self.__metadata__,
                           Column('id', Integer(), primary_key=True, autoincrement=True),
                           Column('category_id', ForeignKey('items_categories.id')),
                           Column('measurement_id', ForeignKey('measurement_units.id')),
                           Column('short_name', String(15), nullable=False),
                           Column('name', Unicode()))

        # TODO - dodać id kontrahenta
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
                                       Column('price_per_one', Numeric(), nullable=True),
                                       Column('quantity', Numeric(), nullable=False),
                                       Column('price_all', Numeric(), nullable=False),
                                       Column('tax_value', Numeric(), nullable=False))

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

    # --------------------------------------------------------------------------
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

    # --------------------------------------------------------------------------

    def add_unit(self, values_dict):
        self.__add_new_from_dict(values_dict, self.measurement_units)

    def remove_unit(self, element_id):
        return self.__remove_element(self.measurement_units, element_id)

    def show_all_units(self):
        return self.__show_all_elements(self.measurement_units)

    def edit_unit(self, element_id, new_values):
        return self.__edit_element(self.measurement_units, element_id, new_values)

    def get_unit(self, element_id):
        return self.__get_element(self.measurement_units, element_id)

    # --------------------------------------------------------------------------

    def add_category(self, values_dict):
        self.__add_new_from_dict(values_dict, self.items_categories)

    def remove_category(self, element_id):
        return self.__remove_element(self.items_categories, element_id)

    def show_all_categories(self):
        return self.__show_all_elements(self.items_categories)

    def edit_category(self, element_id, new_values):
        return self.__edit_element(self.items_categories, element_id, new_values)

    def get_category(self, element_id):
        return self.__get_element(self.items_categories, element_id)

    # --------------------------------------------------------------------------

    def add_operation(self, values_dict):
        self.__add_new_from_dict(values_dict, self.operations)

    def remove_operation(self, element_id):
        return self.__remove_element(self.operations, element_id)

    def show_all_operations(self):
        return self.__show_all_elements(self.operations)

    def edit_operation(self, element_id, new_values):
        return self.__edit_element(self.operations, element_id, new_values)

    def get_operation(self, element_id):
        return self.__get_element(self.operations, element_id)

    # --------------------------------------------------------------------------

    def add_company(self, values_dict):
        self.__add_new_from_dict(values_dict, self.companies)

    def remove_company(self, element_id):
        return self.__remove_element(self.companies, element_id)

    def show_all_companies(self):
        return self.__show_all_elements(self.companies)

    def edit_company(self, element_id, new_values):
        return self.__edit_element(self.companies, element_id, new_values)

    def get_company(self, element_id):
        return self.__get_element(self.companies, element_id)

    # --------------------------------------------------------------------------
    def show_all_documents(self):
        columns = [self.documents.c.id, self.documents.c.document_title, self.documents.c.date,
                   self.documents.c.document_sum, self.documents.c.description,
                   self.operations.c.name.label('operation')]
        selected = select(columns)
        selected = selected.select_from(
            self.documents.join(self.operations, self.documents.c.operation_id == self.operations.c.id))
        with self.__engine__.connect() as conn:
            return conn.execute(selected).all()

    def add_document(self, values_dict):
        return self.__add_new_from_dict(values_dict, self.documents)

    def remove_document(self, element_id):
        return self.__remove_element(self.documents, element_id)

    def edit_document(self, element_id, new_values):
        return self.__edit_element(self.documents, element_id, new_values)

    def get_document(self, element_id):
        columns = [self.documents.c.id, self.documents.c.document_title, self.documents.c.date,
                   self.documents.c.document_sum, self.documents.c.description,
                   self.documents.c.operation_id, self.operations.c.name.label('operation')]
        selected = select(columns)
        selected = selected.select_from(
            self.documents.join(self.operations, self.documents.c.operation_id == self.operations.c.id)).where(
            self.documents.c.id == element_id)
        with self.__engine__.connect() as conn:
            return conn.execute(selected).fetchone()

    # ---------------------------------------------------------------------------
    def show_document_details(self, element_id):
        columns = [self.documents_details.c.id, self.documents_details.c.document_id,
                   self.documents_details.c.price_per_one, self.documents_details.c.price_all,
                   self.documents_details.c.quantity, self.documents_details.c.tax_value, self.tax_rates.c.symbol,
                   self.items.c.name]
        selected = select(columns)
        selected = selected.select_from(
            self.documents_details.join(self.tax_rates, self.documents_details.c.tax_id == self.tax_rates.c.id)).join(
            self.items, self.documents_details.c.item_id == self.items.c.id).where(
            self.documents_details.c.document_id == element_id)

        with self.__engine__.connect() as conn:
            return conn.execute(selected).all()

    # --------------------------------------------------------------------------
    def show_all_items(self):
        columns = [self.items.c.id, self.items.c.short_name, self.items.c.name,
                   self.items_categories.c.name.label('category_name'),
                   self.measurement_units.c.name.label('unit_name')]
        selected = select(columns)
        selected = selected.select_from(
            self.items.join(self.items_categories, self.items.c.category_id == self.items_categories.c.id).join(
                self.measurement_units, self.items.c.measurement_id == self.measurement_units.c.id))
        with self.__engine__.connect() as conn:
            return conn.execute(selected).all()

    def add_item(self, values_dict):
        return self.__add_new_from_dict(values_dict, self.items)

    def remove_item(self, element_id):
        return self.__remove_element(self.items, element_id)

    def edit_item(self, element_id, new_values):
        return self.__edit_element(self.items, element_id, new_values)

    def get_item(self, element_id):
        return self.__get_element(self.items, element_id)

    # --------------------------------------------------------------------------
    def __get_elements_as_list(self, table, field_name):
        elem_list = []
        table = self.__show_all_elements(table)
        elem_list = [(element['id'], element[field_name]) for element in table]
        return elem_list

    def get_taxes_list(self):
        return self.__get_elements_as_list(self.tax_rates, 'symbol')

    def get_items_list(self):
        return self.__get_elements_as_list(self.items_categories, 'name')

    def get_operations_list(self):
        return self.__get_elements_as_list(self.operations, 'name')

    def get_measurement_units_list(self):
        return self.__get_elements_as_list(self.measurement_units, 'name')

    def get_categories_list(self):
        return self.__get_elements_as_list(self.items_categories, 'name')

    def get_tables(self):
        return self.__engine__.table_names()


db = DbCMS('sqlite:///resources/db/app_data.db')
