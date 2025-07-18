-- Lists all genres ordered by rating in hbtn_0d_tvshows_rate
SELECT tv_genres.name, SUM(rate) AS rating FROM tv_shows
INNER JOIN tv_show_ratings
ON tv_shows.id = tv_show_ratings.show_id
INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_genres.name
ORDER BY rating DESC;
