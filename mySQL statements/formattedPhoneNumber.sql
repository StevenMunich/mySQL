SELECT CONCAT('(', SUBSTRING(phone_number, 1, 3), ') ', SUBSTRING(phone_number, 4, 3), '-', SUBSTRING(phone_number, 7)) AS formatted_number;
```
