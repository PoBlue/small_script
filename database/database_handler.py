import sqlite3

sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        begin_date text,
                                        end_date text
                                    );"""

sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                id integer PRIMARY KEY,
                                name text NOT NULL,
                                priority integer,
                                status_id integer NOT NULL,
                                project_id integer NOT NULL,
                                begin_date text NOT NULL,
                                end_date text NOT NULL,
                                FOREIGN KEY (project_id) REFERENCES projects (id)
                            );"""

db_file = "example.db"

def excute_sql(sql_str, file_path):
    try:
        db = sqlite3.connect(file_path) # connect to database

        c = db.cursor()
        c.execute(sql_str)
        db.commit() # commit it
    finally:
        db.close() # close connection
    
