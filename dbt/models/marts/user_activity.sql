{{ config (materialized = 'table')}}

WITH users AS(
    SELECT * FROM {{ ref('staging_user')}}
),

ratings AS(
    SELECT * FROM {{ ref('staging_ratings')}}
)

SELECT
    u.user_id,
    count(r.rating_id) as total_ratings --group by sayesinde her kullanıcı için saydırılır

FROM users u
LEFT JOIN ratings r ON u.user_id = r.user_id -- her kullanıcı gözüksün rating vermeyenler de dahil
GROUP BY u.user_id

-- BU SORGUYLA HER KULLANICI NE KADAR PUAN VERMİŞ ONA BAKTIK