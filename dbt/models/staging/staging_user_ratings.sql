WITH source AS(
    SELECT *
    FROM {{ref('user_ratings')}}
)

SELECT
    user_id,
    rating,
    rating_id,
    movie_id
FROM source
WHERE rating_id IS NOT NULL