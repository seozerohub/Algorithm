-- 코드를 입력하세요
SELECT count(USER_ID) AS 'USERS' FROM USER_INFO
    WHERE JOINED BETWEEN DATE_FORMAT("2021-01-01","%Y-%m-%d") AND DATE_FORMAT("2021-12-31","%Y-%m-%d") AND AGE BETWEEN 20 AND 29