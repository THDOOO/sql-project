-- Initial SQL file for database views
CREATE VIEW ActiveCustomers AS
SELECT id, name, email
FROM Customers
WHERE active = 1;
