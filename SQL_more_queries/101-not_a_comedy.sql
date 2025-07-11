-- Lists all shows not linked to Comedy in hbtn_0d_tvshows
SELECT title FROM tv_shows
WHERE tv_shows.title NOT IN (
	SELECT title FROM tv_genres
	INNER JOIN tv_show_genres
	ON tv_genres.id = tv_show_genres.genre_id
	INNER JOIN tv_shows
	ON tv_show_genres.show_id = tv_shows.id
	WHERE tv_genres.name = 'Comedy'
)
ORDER BY title;
