from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Unicode, ForeignKey


class DbCMS:
    __name__ = 'To jest nazwa'

    def __init__(self, db_connection_string):
        self.__engine__ = create_engine(db_connection_string)
        self.__metadata__ = MetaData()
        self.__initialize_tables__()
        self.__metadata__.create_all(self.__engine__)

    def __initialize_tables__(self):
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
                               Column('city', String(25)))

        self.items = Table('items', self.__metadata__,
                           Column('id', Integer(), primary_key=True, autoincrement=True),
                           Column('category_id', ForeignKey('items_categories.id')),
                           Column('measurement_id', ForeignKey('measurement_units.id')),
                           Column('short_name', String(15), nullable=False),
                           Column('name', Unicode()))

        self.documents = Table('documents', self.__metadata__,
                               Column('id', Integer(), primary_key=True, autoincrement=True),
                               Column('document_title', String(50), nullable=False))

        self.documents = Table('document_details', self.__metadata__,
                               Column('id', Integer(), primary_key=True, autoincrement=True),
                               Column('user_id', ForeignKey('documents.id')),
                               Column('item_id', ForeignKey('items.id')))

    def get_tables(self):
        return self.__engine__.table_names()

    def get_companies_columns(self):
        return self.companies.columns
