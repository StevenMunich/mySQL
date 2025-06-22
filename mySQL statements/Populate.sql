INSERT INTO Users (name, email, password_hash)
VALUES ('Alice Thompson', 'alice@example.com', 'hashed_password_here');

INSERT INTO Products (name, description, price, stock)
VALUES 
('Wireless Mouse', 'Ergonomic and rechargeable', 24.99, 100),
('USB-C Cable', 'Durable 1-meter charging cable', 9.99, 250);

INSERT INTO Orders (user_id, status)
VALUES (1, 'Pending');

INSERT INTO OrderItems (order_id, product_id, quantity, price_at_time)
VALUES 
(1, 1, 2, 24.99),  -- 2 mice
(1, 2, 1, 9.99);   -- 1 cable

INSERT INTO Payments (order_id, amount, payment_method, card_last4, card_type)
VALUES (1, 59.97, 'credit_card', '1234', 'Visa');