WITH source AS(
    SELECT *
    FROM {{ref('movie_genres')}}
)

SELECT
    genre_id,
    movie_id

FROM source
WHERE genre_id IS NOT NULL