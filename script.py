import json
import psycopg2

products_and_suppliers_dictionary = {}


def creating_connection(config):
    conn = psycopg2.connect(host=config.get('host'), database=config.get('database'),
                            user=config.get('user'), password=config.get('password'))
    return conn


def create_suppliers_table(conn, sql_file):
    with conn.cursor() as cur:
        with open(f'{sql_file}') as file:
            request = file.read()
            cur.execute(request)
            conn.commit()


def suppliers_filled(conn, file):
    with conn.cursor() as cur:
        with open(f'{file}') as suppliers_file:
            suppliers_data = json.load(suppliers_file)
            for row in suppliers_data:
                address_list = row['address'].split(';')
                cur.execute(
                    'INSERT INTO suppliers (company_name, contact, country, address, phone, fax, homepage) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING supplier_id',
                    (row['company_name'], row['contact'], address_list[0], row['address'], row['phone'], row['fax'],
                     row['homepage']))
                new_id = cur.fetchone()[0]
                for product in row['products']:
                    products_and_suppliers_dictionary[product] = new_id
            sql_request = ''
            for k, v in products_and_suppliers_dictionary.items():
                name = k
                name = name.replace("'", "")
                sql_request += f"UPDATE products SET supplier_id = {v} WHERE product_name = '{name}';"
            cur.execute(sql_request)
            conn.commit()
            conn.close()


def get_product_by_id(config, id):
    conn = creating_connection(config)
    sql_request = f'SELECT product_id, product_name, categories.category_name, unit_price FROM products ' \
                  f'INNER JOIN categories USING(category_id) ' \
                  f'WHERE product_id = {id}'
    with conn.cursor() as cur:
        cur.execute(sql_request)
        sql_result = cur.fetchall()
        for row in sql_result:
            return f'id продукта: {row[0]}; название продукта: {row[1]}; название категории: {row[2]}; цена продукта: {row[3]}'


def get_category_by_id(config, id):
    products = []
    conn = creating_connection(config)
    sql_request = f'SELECT categories.category_id, categories.category_name, categories.description, product_name FROM products ' \
                  f'INNER JOIN categories USING (category_id) ' \
                  f'WHERE category_id = {id}'
    with conn.cursor() as cur:
        cur.execute(sql_request)
        sql_result = cur.fetchall()
        for row in sql_result:
            products.append(row[3])
        for row in sql_result:
            return f'id категории: {row[0]}; название категории: {row[1]}; описание категории: {row[2]}; список продуктов, относящихся к этой категории: {products}'
