-- list all genres and display the number of shows linked to each
SELECT tg.name, COUNT(*) AS 'number_of_shows'
FROM tv_genres tg
JOIN tv_show_genres tsg ON tg.id = tsg.genre_id
GROUP BY tsg.genre_id
ORDER BY number_of_shows DESC;
