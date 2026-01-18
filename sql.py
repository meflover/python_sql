import sqlite3 as sq
class DatabaseSQL:
    def __init__(self, dir_, tables):
        self.database = dir_
        self.table = tables
    
    def get(self, index, point, value, target):
        with sq.connect(self.database) as con:
            cur = con.cursor()
            query = f'SELECT {value} FROM {self.table[index]} WHERE {point} = ?'
            result = cur.execute(query, (value, target,)).fetchone()
            return result[0] if result else None

    def putin(self, index, point, point_, value, target):
        with sq.connect(self.database) as con:
            cur = con.cursor()
            cur.execute(f'UPDATE {self.table[index]} SET {point} = ? WHERE {point_} = ?', (value, target))
            con.commit()

    def check(self, index, point, value):
        with sq.connect(self.database) as con:
            cur = con.cursor()
            exists = cur.execute(f'SELECT 1 FROM {self.table[index]} WHERE {point} = ?', (value,)).fetchone()
            if exists:
                return True
            else:
                return False

    def get_data(self, index, point, value):
        with sq.connect(self.database) as con:
            cur = con.cursor()
            cur.execute(f'SELECT * FROM {self.table[index]} WHERE {point} = ?', (value,))
            row = cur.fetchone()
            return row

    def insert_data(self, index, point, value):
        with sq.connect(self.database) as con:
            cur = con.cursor()
            cur.execute(
                f'''INSERT INTO {self.table[index]} 
                ({point})
                VALUES (?)''',
                (value)
            )
            con.commit()
            
    def getline(self, index, point):
        with sq.connect(self.database) as con:
            cur = con.cursor()
            return [row[0] for row in cur.execute(f"SELECT {point} FROM {self.table[index]}")]

    def delete(self, index, point, value):
        with sq.connect(self.datamess) as con:
            cur = con.cursor()
            cur.execute(f'DELETE FROM {self.table[index]} WHERE {point} = ?',(value,))
            con.commit()
            
DSQL = DatabaseSQL("storage/form.db", ["users","data"])