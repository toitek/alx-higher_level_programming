-- Write a script that lists all shows contained in hbtn_0d_tvshows without a genre linked.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
SELECT tv_shows.title ,  tv_show_genres.genre_id
FROM hbtn_0d_tvshows.tv_shows 
LEFT JOIN hbtn_0d_tvshows.tv_show_genres 
ON tv_shows.id = tv_show_genres.tv_show_id 
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC , tv_show_genres.genre_id ASC ;