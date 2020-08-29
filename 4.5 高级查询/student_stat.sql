/* 创建结果表 */
create table student_stat (
    name VARCHAR(20),
    teacher VARCHAR(20),
    subject VARCHAR(20),
    avg_score FLOAT,
    score FLOAT,
    total_score FLOAT,
    score_rate VARCHAR(200)
)

/* 创建存储过程 */
create procedure calc_student_stat()
BEGIN
    insert into save.student_stat
    select 
        a.name, 
        c.teacher,
        c.subject,
        e.avg_score,
        b.score,
        d.total_score,
        concat(TRUNCATE(b.score / d.total_score * 100, 2), '%') as score_rate
    from student as a
    inner join score as b
    inner join subject as c
    inner join (
        select 
            a.name,
            sum(score) as total_score
        from student as a
        inner join score as b
        on a.id = b.student_id
        group by a.name 
    ) as d
    inner join (
        select 
            a.subject,
            avg(score) as avg_score
        from subject as a
        inner join score as b
        on a.id = b.subject_id
        group by a.subject
    ) as e
    on a.id = b.student_id and b.subject_id = c.id
    and a.name = d.name and c.subject = e.subject
END;


/* 调用存储过程 */
call calc_student_stat();