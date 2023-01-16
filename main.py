from script import suppliers_filled, creating_connection, create_suppliers_table, get_product_by_id, get_category_by_id


db_configs = {'host': 'localhost', 'database': 'northwind_traders', 'user': 'postgres', 'password': '54321'}

if __name__ == '__main__':
    conn = creating_connection(db_configs)
    create_suppliers_table(conn, 'create_suppliers_table.sql')
    suppliers_filled(conn, 'suppliers.json')
    print(get_product_by_id(db_configs, 8))
    print(get_category_by_id(db_configs, 1))
