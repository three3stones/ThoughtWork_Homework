/* 1. 一共有多少不同的用户 */
select count(distinct userId) as user_cnt from rating;

/* 2. 一共有多少不同的电影 */
select count(distinct movieId) as movie_cnt from movie;

/* 3. 一共有多少不同的电影种类 */
select count(t.genres_signal) as genres_cnt 
from (
select genres_signal from movie 
lateral view explode(split(genres,"\\|")) ss as genres_signal
where genres_signal != "(no genres listed)"
group by genres_signal
) as t;

