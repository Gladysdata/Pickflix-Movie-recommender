#All unique movies with their duration, genres and ratings :
SELECT DISTINCT title, duration, genres, rating 
FROM cleaned_movies ;

#Total number of movies : 
SELECT COUNT(DISTINCT title) 
FROM cleaned_movies ;

#All movies by Fred Astaire because he is fantastic
SELECT title, year, duration, genres, rating 
FROM cleaned_movies 
WHERE `actor/actress` = 'Fred Astaire' ;

#Average rating for each movie genre
WITH genre_count AS (
  SELECT genres, COUNT(*) as movie_count, AVG(rating) as avg_rating
  FROM cleaned_movies
  GROUP BY genres
)
SELECT genres, avg_rating
FROM genre_count
WHERE movie_count > 10 ;


