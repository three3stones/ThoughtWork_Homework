/* 1. 设计数据在mysql中的schema，并使之符合三范式 */
CREATE DATABASE IF NOT EXISTS movieLens
DEFAULT CHARACTER SET utf8;

USE movieLens;

CREATE TABLE IF NOT EXISTS movie(
    movieId INT primary key,
    title VARCHAR(500),
    genres VARCHAR(500)
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS rating(
    userId INT,
    movieId INT,
    rating FLOAT,
    timestamp VARCHAR(500)
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS tag(
    userId INT,
    movieId INT,
    tag VARCHAR(500),
    timestamp VARCHAR(500)
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS link(
    movieId INT primary key,
    imdbId VARCHAR(500),
    tmbdId VARCHAR(500),
    FOREIGN KEY (movieId) REFERENCES movie(movieId)
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS genome_tag(
    tagId INT primary key,
    tag VARCHAR(500)
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS genome_score(
    movieId INT,
    tagId INT,
    relevance VARCHAR(500),
    FOREIGN KEY (movieId) REFERENCES movie(movieId),
    FOREIGN KEY (tagId) REFERENCES genome_tag(tagId)
)ENGINE=InnoDB;


/* 2.将外键依赖删除 */
alter table movielens.tag DROP FOREIGN KEY tag_ibfk_1;
alter table movielens.genome_score DROP FOREIGN KEY genome_score_ibfk_1;
alter table movielens.genome_score DROP FOREIGN KEY genome_score_ibfk_2;


/* 3. 导入csv数据 */
LOAD DATA INFILE "C:/Users/10920/Desktop/ml-25m/movies.csv"
INTO TABLE movielens.movie character set gb2312
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\r\n';

LOAD DATA INFILE "C:/Users/10920/Desktop/ml-25m/links.csv"
INTO TABLE movielens.movie character set gb2312
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\r\n';

LOAD DATA INFILE "C:/Users/10920/Desktop/ml-25m/ratings.csv"
INTO TABLE movielens.movie character set gb2312
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\r\n';

LOAD DATA INFILE "C:/Users/10920/Desktop/ml-25m/tags.csv"
INTO TABLE movielens.movie character set gb2312
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\r\n';

LOAD DATA INFILE "C:/Users/10920/Desktop/ml-25m/genome-tags.csv"
INTO TABLE movielens.movie character set gb2312
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\r\n';

LOAD DATA INFILE "C:/Users/10920/Desktop/ml-25m/genome-scores.csv"
INTO TABLE movielens.movie character set gb2312
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\r\n';

/* 4. 将外键依赖恢复 */
alter table movielens.link ADD CONSTRAINT link_ibfk_1 FOREIGN KEY (movieId) REFERENCES movie(movieId);
alter table movielens.genome_score ADD CONSTRAINT genome_score_ibfk_1 FOREIGN KEY (movieId) REFERENCES movie(movieId);
alter table movielens.genome_score ADD CONSTRAINT genome_score_ibfk_2 FOREIGN KEY (tagId) REFERENCES genome_tag(tagId);

/* 5. 建立索引 */
CREATE INDEX index_1 ON movie (movieId);
CREATE INDEX index_2 ON rating (userId);
CREATE INDEX index_3 ON tag (userId, movieId);
CREATE INDEX index_4 ON link (movieId);
CREATE INDEX index_5 ON genome_tag (tagId);