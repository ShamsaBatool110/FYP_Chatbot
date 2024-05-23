from langchain_community.utilities import SQLDatabase

url = f"mysql+pymysql://root:Batool110$@localhost:3306/customer_support_db"
db = SQLDatabase.from_uri(url)
# print(db.dialect)
# print(db.get_usable_table_names())
# print(db.run("SELECT * FROM customers;"))