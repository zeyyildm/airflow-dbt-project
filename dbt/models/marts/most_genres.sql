{{ config(materialized = 'table') }}

WITH movie_genres AS (
    SELECT * FROM {{ ref('staging_mgenres') }}
),
movies AS (
    SELECT * FROM {{ ref('staging_movies') }}
)

SELECT
    g.genre_id,
    COUNT(m.movie_id) AS toplam_film
FROM movies m
LEFT JOIN movie_genres g ON m.movie_id = g.movie_id
GROUP BY g.genre_id



-- HANGİ TÜRDEN KAÇ TANE FİLM VAR