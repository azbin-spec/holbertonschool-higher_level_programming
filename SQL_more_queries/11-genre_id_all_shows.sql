-- Lists all shows in hbtn_0D_tvshows with NULL displayed when no genre assigned
SELECT title, genre_id FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY title ASC, genre_id ASC;
