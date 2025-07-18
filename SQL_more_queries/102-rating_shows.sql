-- Lists all shows ordered by rating in hbtn_0d_tvshows_rate
SELECT title, SUM(rate) AS rating FROM tv_shows
LEFT JOIN tv_show_ratings
ON tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_shows.title
ORDER BY rating DESC;
