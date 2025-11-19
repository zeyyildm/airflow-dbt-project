WITH source AS(
    SELECT *
    FROM {{ref('movies')}}
)

SELECT
    movie_id,
    title

FROM source
WHERE movie_id IS NOT NULL