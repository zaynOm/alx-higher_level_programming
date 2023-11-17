-- list all shows without the genre Comedy
SELECT title FROM tv_shows
WHERE id NOT IN (
	SELECT tsg.show_id FROM tv_show_genres tsg
	JOIN tv_genres tg ON tg.id = tsg.genre_id
	WHERE tg.name = 'Comedy'
	)
ORDER BY title;
