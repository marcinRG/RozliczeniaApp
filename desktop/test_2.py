from db_cms.db_cms_core import DbCMS

db_cms = DbCMS('sqlite:///:memory:')

print(db_cms.get_tables())
