SELECT
    F.FLAVOR
FROM
    FIRST_HALF F
JOIN
    ICECREAM_INFO I ON I.FLAVOR = F.FLAVOR
WHERE
    F.TOTAL_ORDER > 3000 AND
    I.INGREDIENT_TYPE = 'fruit_based'
ORDER BY
    F.TOTAL_ORDER DESC;
