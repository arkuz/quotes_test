import mysql.connector


config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'quotes_test'
}

tab = 'tereshkova_table'

def init_connection():
    return mysql.connector.connect(**config)

def close_connection(con):
    con.close()

def copy_all_in_table(con, row_list):
    cursor = con.cursor()
    query = ("INSERT INTO "+ tab +
              " (goods, count, cost, action) "
              "VALUES (%s, %s, %s, %s)")
    for row in row_list:
        data = row
        cursor.execute(query, data)
        con.commit()
    cursor.close()

def select_all_from_db(con):
    cursor = con.cursor()
    query = ('SELECT * FROM ' + tab)
    cursor.execute(query)
    row_list = []
    for row in cursor:
        row_list.append(row[1:])
    cursor.close()
    return row_list

def delete_all_from_db(con):
    cursor = con.cursor()
    query = ('DELETE FROM ' + tab)
    cursor.execute(query)
    con.commit()
    cursor.close()
