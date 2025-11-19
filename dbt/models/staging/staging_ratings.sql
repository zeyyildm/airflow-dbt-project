WITH source AS(
    SELECT *
    FROM {{ref('user_ratings')}}
)

SELECT
    rating_id,
    user_id,
    movie_id,
    rating,
    rating_date::timestamp AS rating_date

FROM source
WHERE rating_id IS NOT NULL