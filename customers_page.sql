--Посчитать количество заказчиков
SELECT COUNT(*) FROM customers;
--Выбрать все уникальные сочетания городов и стран, в которых "зарегестрированы" заказчики
SELECT DISTINCT country, city FROM customers;
--Найти заказчиков и обслуживающих их заказы сотрудников, таких, что и заказчики и сотрудники из города London, а доставка идёт компанией Speedy Express. Вывести компанию заказчика и ФИО сотрудника.
SELECT customers.company_name, CONCAT(employees.first_name, ' ', employees.last_name) as full_name FROM employees
INNER JOIN orders USING (employee_id)
INNER JOIN customers USING (customer_id)
WHERE employees.city = 'London' and customers.city = 'London' and ship_via = 1;
--Найти заказчиков, не сделавших ни одного заказа. Вывести имя заказчика и order_id
SELECT company_name, order_id FROM customers
FULL JOIN orders USING(customer_id)
WHERE orders.customer_id IS NULL