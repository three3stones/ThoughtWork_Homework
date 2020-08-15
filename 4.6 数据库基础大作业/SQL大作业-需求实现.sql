/* 1. 一共有多少不同的用户 */
select count(distinct userId) as user_count from rating;

/* 2. 一共有多少不同的电影 */
select count(distinct movieId) as movie_count from movie;

/* 3. 一共有多少不同的电影种类 */

/* 4. 一共有多少电影没有外部链接 */
select count(*) as movie_not_link_num
from movie a left join link b
on a.movieId = b.movieId
where b.imdbId is null;

/* 5. 2018年一共有多少人进行过电影评分 */
select count(distinct t.userId) from
(
	select userId, FROM_UNIXTIME(timestamp,'%Y') as rating_year
	from rating
) as t
where t.rating_year = '2018';

/* 6. 2018年评分5分以上的电影及其对应的标签 */
select b.movieId, group_concat(tag) as tags
from
(
    select movieId
    from rating
    where FROM_UNIXTIME(timestamp,'%Y') = '2018'
    group by movieId
    having avg(rating)>=5
) as a
inner join tag as b
on a.movieId = b.movieId
group by b.movieId;



