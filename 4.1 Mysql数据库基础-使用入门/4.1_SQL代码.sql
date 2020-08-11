/* 创建数据库 */
CREATE DATABASE student_examination_sys;
/* 选择数据库 */
USE student_examination_sys;

/* 1. 学生表 */
CREATE TABLE IF NOT EXISTS student(
   id VARCHAR(20),
   name VARCHAR(50),
   age INT,
   sex VARCHAR(10),
   PRIMARY KEY ( id )
) ENGINE = InnoDB DEFAULT CHARSET = utf8;

INSERT INTO student VALUES ('001', '张三', '18', '男');
INSERT INTO student VALUES ('002', '李四', '20', '女');


/* 2. 考试科目表 */
CREATE TABLE IF NOT EXISTS subject(
   id VARCHAR(20),
   subject VARCHAR(20),
   teacher VARCHAR(20),
   description VARCHAR(100),
   PRIMARY KEY ( id )
) ENGINE = InnoDB DEFAULT CHARSET = utf8;

INSERT INTO student VALUES ('1001', '语文', '王老师', '本次考试比较简单');
INSERT INTO student VALUES ('1002', '数学', '刘老师', '本次考试比较难');


/* 3. 成绩表 */
CREATE TABLE IF NOT EXISTS score(
   id VARCHAR(10),
   student_id VARCHAR(20),
   subject_id VARCHAR(20),
   score FLOAT,
   PRIMARY KEY ( id )
) ENGINE = InnoDB DEFAULT CHARSET = utf8;

INSERT INTO score VALUES ('1', '001', '1001', 80);
INSERT INTO score VALUES ('2', '002', '1002', 60);
INSERT INTO score VALUES ('3', '001', '1001', 70);
INSERT INTO score VALUES ('4', '002', '1002', 60.5);
