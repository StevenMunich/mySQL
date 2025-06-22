SELECT 
    users.id AS user_id,
    users.name AS user_name,
    orders.id AS order_id,
    orders.order_date,
    products.id AS product_id,
    products.name AS product_name,
    orderitems.quantity
FROM users
JOIN orders ON users.id = orders.user_id
JOIN orderitems ON orders.id = orderitems.order_id
JOIN products ON orderitems.product_id = products.id;