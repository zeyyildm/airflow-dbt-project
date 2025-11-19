WITH source AS(
    SELECT *
    FROM {{ref('genres')}}
)

SELECT
    genre_id,
    genre_name

FROM source
WHERE genre_id IS NOT NULL