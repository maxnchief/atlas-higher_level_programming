-- list all genres and display the number of shows in each genre
SELECT g.name AS genre, COUNT(s.id) AS number_of_shows
FROM genres g
JOIN tv_shows_genres tsg ON g.id = tsg.genre_id
JOIN tv_shows s ON tsg.tv_show_id = s.id
GROUP BY g.name
HAVING COUNT(s.id) > 0
ORDER BY number_of_shows DESC;