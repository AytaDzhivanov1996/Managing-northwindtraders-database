ALTER TABLE products DROP COLUMN IF EXISTS supplier_id;
DROP TABLE IF EXISTS suppliers;

CREATE TABLE IF NOT EXISTS suppliers
(
	supplier_id serial PRIMARY KEY,
	company_name varchar NOT NULL,
	contact varchar NOT NULL,
	country varchar NOT NULL,
	address varchar NOT NULL,
	phone varchar NOT NULL,
	fax varchar NOT NULL,
	homepage text
);

ALTER TABLE products ADD COLUMN IF NOT EXISTS supplier_id int;
ALTER TABLE products ADD CONSTRAINT fk_products_supplier_id FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id);