SELECT SUBSTRING(email, 1, LOCATE('@', email) - 1) AS username
FROM Users;