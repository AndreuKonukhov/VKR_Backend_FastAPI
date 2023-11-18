from connect_db import create_connection, execute_query, execute_read_query
from psycopg2 import OperationalError, connect
import json


connection = create_connection(db_name="MPF_NN_VKR",
                               db_user="postgres",
                               db_password="123456",
                               db_host="localhost",
                               db_port="5432")

select_users = "SELECT to_json(result) FROM (SELECT * FROM sech) result"

i = 0

while True:
    sech = execute_read_query(connection, select_users)
    print(sech)
    print(i)
    i = i+1
