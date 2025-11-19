WITH source AS(
    SELECT *
    FROM {{ref('users')}}
)

SELECT
    user_id,
    country,
    age_range,
    gender,
    signup_date::timestamp AS signup_date

FROM source
WHERE user_id IS NOT NULL