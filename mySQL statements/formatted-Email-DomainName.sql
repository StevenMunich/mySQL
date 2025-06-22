SELECT SUBSTRING(email, LOCATE('@', email) + 1) AS domain
FROM Users;

