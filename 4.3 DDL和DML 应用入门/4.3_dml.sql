-- 插入记录  
insert into student(id,name,age,sex) values ('003','王五',22,'男');

-- 修改记录  
update student set age = 25 where name='王五';

-- 删除记录  
delete from student where name='王五';

-- 查询记录  
select id,name,age,sex from student where name='张三';