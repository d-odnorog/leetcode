# https://leetcode.com/problems/delete-duplicate-emails/

DELETE
FROM
     person
USING
    person, person p1
WHERE
    person.id > p1.id
    AND person.email = p1.email;
