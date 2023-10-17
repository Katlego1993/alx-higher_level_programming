-- Displays the 3 cities with the highest average
-- temperatures between July and August.
y, AVG(value) AS avg_temp FROM temperatures WHERE month IN (7, 8) GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
