import MySQLdb
db=MySQLdb.connect("localhost","root","plutonian","test1")
cursor=db.cursor()
cmd="""drop table if exists undergradresults"""
cursor.execute(cmd)
cmd="""drop table if exists postgradresults"""
cursor.execute(cmd)
cmd="""drop table if exists undergradcounters"""
cursor.execute(cmd)
cmd="""drop table if exists postgradcounters"""
cursor.execute(cmd)
cmd="""create table undergradresults(id int primary key auto_increment,title char(75) not null,linkf char(75) not null)"""
cursor.execute(cmd)
cmd="""create table postgradresults(id int primary key auto_increment,title char(75) not null,linkf char(75) not null)"""
cursor.execute(cmd)
cmd="""create table postgradcounters(postgradid int,postgradtitle char(75))"""
cursor.execute(cmd)
cmd="""create table undergradcounters(undergradid int,undergradtitle char(75))"""
cursor.execute(cmd)
cmd="""insert into undergradcounters(undergradid,undergradtitle) values(1,"last")"""
cursor.execute(cmd)
cmd="""insert into postgradcounters(postgradid,postgradtitle) values(1,"last")"""
cursor.execute(cmd)
cmd="""create table mphilresults(id int primary key auto_increment,title char(75) not null,linkf char(75) not null)"""
cursor.execute(cmd)
cmd="""create table mphilcounters(mphilid int,mphiltitle char(75))"""
cursor.execute(cmd)
cmd="""create table phdresults(id int primary key auto_increment,title char(75) not null,linkf char(75) not null)"""
cursor.execute(cmd)
cmd="""create table phdcounters(phdid int,phdtitle char(75))"""
cursor.execute(cmd)
cmd="""create table diplomaresults(id int primary key auto_increment,title char(75) not null,linkf char(75) not null)"""
cursor.execute(cmd)
cmd="""create table diplomacounters(diplomaid int,diplomatitle char(75))"""
cursor.execute(cmd)
cmd="""create table ncwebresults(id int primary key auto_increment,title char(75) not null,linkf char(75) not null)"""
cursor.execute(cmd)
cmd="""create table ncwebcounters(ncwebid int,ncwebtitle char(75))"""
cursor.execute(cmd)
cmd="""create table srccnotices(id int primary key auto_increment,title char(75) not null,linkf char(75) not null)"""
cursor.execute(cmd)
cmd="""create table srcccounters(srccid int,srcctitle char(75))"""
cursor.execute(cmd)
cmd="""create table hansrajnotices(id int primary key auto_increment,title char(75) not null,linkf char(75) not null)"""
cursor.execute(cmd)
cmd="""create table hansrajcounters(hansrajid int,hansrajtitle char(75))"""
cursor.execute(cmd)
db.commit()
cursor.close()
db.close()
