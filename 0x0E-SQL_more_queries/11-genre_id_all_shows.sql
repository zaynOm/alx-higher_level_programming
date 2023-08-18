-- lists all shows contained in the database hbtn_0d_tvshows
SELECT s.title, sg.genre_id
FROM tv_shows s
LEFT JOIN tv_show_genre sg ON s.id = sg.show_id
ORDER BY s.title, sg.genre_id;
