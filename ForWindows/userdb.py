import sqlite3

def create_table():
    try:
        with sqlite3.connect("userinfo.sqlite") as con:
            sql_cmd = """
            create table medal(
                name text primary key,
                age integer,
                gender text,
                height integer,
                weight real
            );
            """
            con.execute(sql_cmd)
    except Exception as e:
        print("Error -> {}".format(e))
        
def insert():
    try:
        with sqlite3.connect("userinfo.sqlite") as con:
            sql_cmd = """
            insert into medal values('Suphawit',18,'ชาย',170,51)
            """
            con.execute(sql_cmd)
            con.close()
    except Exception as e:
        print("Error -> {}".format(e))

def select(username):
    try:
        with sqlite3.connect("userinfo.sqlite") as con:
            sql_cmd = 'SELECT * FROM medal WHERE name = "' + \
                username + '"'
            data = con.execute(sql_cmd)
            for row in data:
                return True
    except Exception as e:
        print("Error -> {}".format(e))
        
def selectheight(username):
    try:
        with sqlite3.connect("userinfo.sqlite") as con:
            sql_cmd = 'SELECT height FROM medal WHERE name = "' + \
                username + '"'
            data = con.execute(sql_cmd)
            for row in data:
                return row[0]
    except Exception as e:
        print("Error -> {}".format(e))

def selectweight(username):
    try:
        with sqlite3.connect("userinfo.sqlite") as con:
            sql_cmd = 'SELECT weight FROM medal WHERE name = "' + \
                username + '"'
            data = con.execute(sql_cmd)
            for row in data:
                return row[0]
    except Exception as e:
        print("Error -> {}".format(e))

def selectage(username):
    try:
        with sqlite3.connect("userinfo.sqlite") as con:
            sql_cmd = 'SELECT age FROM medal WHERE name = "' + \
                username + '"'
            data = con.execute(sql_cmd)
            for row in data:
                return row[0]
    except Exception as e:
        print("Error -> {}".format(e))
        
def selectgender(username):
    try:
        with sqlite3.connect("userinfo.sqlite") as con:
            sql_cmd = 'SELECT gender FROM medal WHERE name = "' + \
                username + '"'
            data = con.execute(sql_cmd)
            for row in data:
                return row[0]
    except Exception as e:
        print("Error -> {}".format(e))
        
def delete():
    try:
        with sqlite3.connect("userinfo.sqlite") as con:
            sql_cmd = """
            delete from medal where name = 'tonn'
            """
            con.execute(sql_cmd)
    except Exception as e:
        print("Error -> {}".format(e))

#delete()
#selectgender()
#insert()
#create_table()