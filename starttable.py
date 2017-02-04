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
cmd="""drop table if exists mphilresults"""
cursor.execute(cmd)
cmd="""drop table if exists mphilcounters"""
cursor.execute(cmd)
cmd="""drop table if exists ncwebresults"""
cursor.execute(cmd)
cmd="""drop table if exists ncwebcounters"""
cursor.execute(cmd)
cmd="""drop table if exists phdcounters"""
cursor.execute(cmd)
cmd="""drop table if exists phdresults"""
cursor.execute(cmd)
cmd="""drop table if exists diplomacounters"""
cursor.execute(cmd)
cmd="""drop table if exists diplomaresults"""
cursor.execute(cmd)
cmd="""drop table if exists srcccounters"""
cursor.execute(cmd)
cmd="""drop table if exists hansrajcounters"""
cursor.execute(cmd)
cmd="""drop table if exists srccnotices"""
cursor.execute(cmd)
cmd="""drop table if exists hansrajnotices"""
cursor.execute(cmd)
cmd="""drop table if exists south_campusresults"""
cursor.execute(cmd)
cmd="""drop table if exists south_campuscounters"""
cursor.execute(cmd)
cmd="""drop table if exists api_datesheetugresults"""
cursor.execute(cmd)
cmd="""drop table if exists api_datesheetugcounters"""
cursor.execute(cmd)
cmd="""create table undergradresults(id int primary key auto_increment,title char(255) not null,linkf char(255) not null)"""
cursor.execute(cmd)
cmd="""create table postgradresults(id int primary key auto_increment,title char(255) not null,linkf char(255) not null)"""
cursor.execute(cmd)
cmd="""create table postgradcounters(postgradid int,postgradtitle char(255))"""
cursor.execute(cmd)
cmd="""create table undergradcounters(undergradid int,undergradtitle char(255))"""
cursor.execute(cmd)
cmd="""insert into undergradcounters(undergradid,undergradtitle) values(1,"last")"""
cursor.execute(cmd)
cmd="""insert into postgradcounters(postgradid,postgradtitle) values(1,"last")"""
cursor.execute(cmd)
cmd="""create table mphilresults(id int primary key auto_increment,title char(255) not null,linkf char(255) not null)"""
cursor.execute(cmd)
cmd="""create table mphilcounters(mphilid int,mphiltitle char(255))"""
cursor.execute(cmd)
cmd="""create table phdresults(id int primary key auto_increment,title char(255) not null,linkf char(255) not null)"""
cursor.execute(cmd)
cmd="""create table phdcounters(phdid int,phdtitle char(255))"""
cursor.execute(cmd)
cmd="""create table diplomaresults(id int primary key auto_increment,title char(255) not null,linkf char(255) not null)"""
cursor.execute(cmd)
cmd="""create table diplomacounters(diplomaid int,diplomatitle char(255))"""
cursor.execute(cmd)
cmd="""create table ncwebresults(id int primary key auto_increment,title char(255) not null,linkf char(255) not null)"""
cursor.execute(cmd)
cmd="""create table ncwebcounters(ncwebid int,ncwebtitle char(255))"""
cursor.execute(cmd)
cmd="""create table srccnotices(id int primary key auto_increment,title char(255) not null,linkf char(255) not null)"""
cursor.execute(cmd)
cmd="""create table srcccounters(srccid int,srcctitle char(255))"""
cursor.execute(cmd)
cmd="""create table hansrajnotices(id int primary key auto_increment,title char(255) not null,linkf char(255) not null)"""
cursor.execute(cmd)
cmd="""create table hansrajcounters(hansrajid int,hansrajtitle char(255))"""
cursor.execute(cmd)
cmd="""create table south_campuscounters(south_campusid int,south_campustitle char(255))"""
cursor.execute(cmd)
cmd="""create table south_campusresults(id int primary key auto_increment,title char(255) not null,linkf char(255) not null)"""
cursor.execute(cmd)
cmd="""insert into south_campuscounters values(1,"last")"""
cursor.execute(cmd)
cmd="""insert into srcccounters values(1,"last")"""
cursor.execute(cmd)
cmd="""insert into hansrajcounters values(1,"last")"""
cursor.execute(cmd)
cmd="""insert into mphilcounters values(1,"last")"""
cursor.execute(cmd)
cmd="""insert into diplomacounters values(1,"last")"""
cursor.execute(cmd)
cmd="""insert into ncwebcounters values(1,"last")"""
cursor.execute(cmd)
cmd="""create table api_datesheetugcounters(datesheetid int,datesheettitle char(255))"""
cursor.execute(cmd)
cmd="""create table api_datesheetugresults(id int primary key auto_increment,title char(255) not null,linkf char(255) not null)"""
cursor.execute(cmd)
cmd="""insert into api_datesheetugcounters values(1,"last")"""
cursor.execute(cmd)
db.commit()
cursor.close()
db.close()
