-- 1.查询同时存在1课程和2课程的情况
select 
    t2.id,t2.name,t2.age,t2.sex,t1.score1,t1.score2
from (select 
        sc1.studentid, sc1.courseid, sc1.score as score1,
        sc2.score as score2 from 
            (select * from student_course where courseid='1') sc1
            inner join 
            (select * from student_course where courseid='2') sc2
            on sc1.studentid = sc2.studentid
        ) as t1
inner join  
(select id, name, age, sex
 from student) as t2
on t1.studentid = t2.id;
/*
1	赵雷	1990-01-01 00:00:00	男	80.0	90.0
2	钱电	1990-12-21 00:00:00	男	70.0	60.0
3	孙风	1990-05-20 00:00:00	男	80.0	80.0
4	李云	1990-08-06 00:00:00	男	50.0	30.0
5	周梅	1991-12-01 00:00:00	女	76.0	87.0
*/

-- 2.查询同时存在1课程和2课程的情况  同上
select 
    t2.id,t2.name,t2.age,t2.sex,t1.score1,t1.score2
from (select 
        sc1.studentid, sc1.courseid, sc1.score as score1,
        sc2.score as score2 from 
            (select * from student_course where courseid='1') sc1
            inner join 
            (select * from student_course where courseid='2') sc2
            on sc1.studentid = sc2.studentid
        ) as t1
inner join  
(select id, name, age, sex
 from student) as t2
on t1.studentid = t2.id;

-- 3.查询平均成绩大于等于60分的同学的学生编号和学生姓名和平均成绩
select
    a.studentid,
    b.name,
    sum(a.score)/count(a.courseid) as avg_score
from student_course as a 
left join student as b
on a.studentid = b.id
group by a.studentid 
having avg_score >= 60;
/* 
1	赵雷	89.66667
2	钱电	70.00000
3	孙风	80.00000
5	周梅	81.50000
7	郑竹	93.50000
*/

-- 4.查询在student_course表中不存在成绩的学生信息的SQL语句
select id, name, age, sex
from student
where id not in (
    select studentid from student_course
    group by studentid
);
/*
8	王菊	1990-01-20 00:00:00	女
*/

-- 5.查询所有有成绩的SQL
select id, name, age, sex
from student
where id in (
    select studentid from student_course
    group by studentid
);
/*
1	赵雷	1990-01-01 00:00:00	男
2	钱电	1990-12-21 00:00:00	男
3	孙风	1990-05-20 00:00:00	男
4	李云	1990-08-06 00:00:00	男
5	周梅	1991-12-01 00:00:00	女
6	吴兰	1992-03-01 00:00:00	女
7	郑竹	1989-07-01 00:00:00	女
*/

-- 6.查询学过编号为1并且也学过编号为2的课程的同学的信息
select id, name, age, sex from student as st
where  
(select COUNT(*) from student_course as sc1 where sc1.studentid=st.id and sc1.courseid='1') > 0
and
(select COUNT(*) from student_course as sc2 where sc2.studentid=st.id and sc2.courseid='2') > 0;
/*
1	赵雷	1990-01-01 00:00:00	男
2	钱电	1990-12-21 00:00:00	男
3	孙风	1990-05-20 00:00:00	男
4	李云	1990-08-06 00:00:00	男
5	周梅	1991-12-01 00:00:00	女
*/

-- 7.检索1课程分数小于60，按分数降序排列的学生信息
select
    b.id, b.name, b.age, b.sex
from student_course as a 
inner join student as b
on a.studentid = b.id
and a.courseid='1'
where a.score < 60
order by a.score desc;
/*
4	李云	1990-08-06 00:00:00	男
6	吴兰	1992-03-01 00:00:00	女
*/

-- 8.查询每门课程的平均成绩，结果按平均成绩降序排列，平均成绩相同时，按课程编号升序排列
select
    c.name,
    sum(sc.score) / count(sc.score) as avg_score
from student_course as sc
inner join course as c
on sc.courseid = c.id
group by sc.courseid
order by avg_score desc, sc.courseid asc;
/*
数学	72.66667
英语	68.50000
语文	64.50000
*/

-- 9.查询课程名称为"数学"，且分数低于60的学生姓名和分数
select 
    s.name,
    sc.score
from student_course as sc
inner join course as c 
on sc.courseid = c.id
inner join student as s
on sc.studentid = s.id
where c.name = '数学' and sc.score < 60;
/*
李云	30.0
*/