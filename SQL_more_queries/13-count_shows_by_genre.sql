-- Lists all genres in hbtn_0D_tvshows with number of shows linked
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows FROM tv_genres
LEFT JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_show_genres.genre_id IS NOT NULL
GROUP BY genre
ORDER BY number_of_shows DESC;
