{{ config(materialized = 'table') }}

WITH users AS (
    SELECT * FROM {{ ref('staging_user') }}
)


SELECT
    user_id,
    signup_date
FROM users
ORDER BY signup_date