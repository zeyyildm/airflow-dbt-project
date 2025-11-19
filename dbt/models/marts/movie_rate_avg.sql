{{ config (materialized = 'table')}}

WITH movies AS(
    SELECT * FROM {{ ref('staging_movies')}}
),

user_ratings AS(
    SELECT * FROM {{ ref('staging_user_ratings')}}
)

SELECT
    m.movie_id,
    AVG(u.rating) AS avg_rating

FROM movies m
LEFT JOIN user_ratings u ON m.movie_id =  u.movie_id
GROUP BY m.movie_id

-- HER FILM İÇİN ORTALAMA DEĞERLENDİRME PUANI