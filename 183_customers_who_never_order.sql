# https://leetcode.com/problems/customers-who-never-order/

SELECT
    name as 'Customers'
FROM
    customers
WHERE
    id NOT IN (
        SELECT
            customerId
        FROM
            orders
    );
