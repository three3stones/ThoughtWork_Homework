-- **数据库级别：**  
--  显示所有数据库  
SHOW DATABASE;

--  进入某个数据库  
USE student_examination_sys;

--  创建一个数据库  
CREATE DATABASE IF NOT EXISTS student_examination_sys;

--  创建指定字符集的数据库  
CREATE DATABASE IF NOT EXISTS student_examination_sys DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

--  显示数据库的创建信息   
SHOW CREATE DATABASE student_examination_sys;

--  修改数据库的编码  
ALTER DATABASE student_examination_sys character set utf8;

--  删除一个数据库   
DROP DATABASE student_examination_sys;


-- **表级别**
--  修改表名
ALTER TABLE student rename to student1;

--  修改字段的数据类型
ALTER TABLE student1 modify column age varchar(10);

--  修改字段名
ALTER TABLE student1 change age age1 varchar(20);

--  添加字段
ALTER TABLE student1 add addr varchar(100);

--  删除字段
ALTER TABLE student1 drop column addr;

--  修改表的存储引擎
ALTER TABLE student1 ENGINE = MyIsam;

--  删除表的外键约束
ALTER TABLE student1 drop foreign key foreign_key;

--  删除一张表
DROP TABLE student1;