import cx_Oracle
from src.ConfigParser import ConfigParser
from src.Db.Value import DateValue, ClobValue, BlobValue, LiteralValue, SequenceValue


class DbConnector:

    def __init__(self, config_file):
        db_instance = "DB"
        self.KAFKA_CONFIG_FILEPATH = config_file
        self.cfg = ConfigParser(self.KAFKA_CONFIG_FILEPATH)
        self.DB_HOST = self.cfg.safe_get(db_instance, 'DB_HOST')
        self.DB_USER = self.cfg.safe_get(db_instance, 'DB_USER')
        self.DB_PASSWORD = self.cfg.safe_get(db_instance, 'DB_PASSWORD')
        self.DB_SERVICE = self.cfg.safe_get(db_instance, 'DB_SERVICE')
        self.CON_STR = self.DB_USER + "/" + self.DB_PASSWORD + "@" + self.DB_HOST + "/" + self.DB_SERVICE
        #  print(self.CON_STR)
        self.connect = cx_Oracle.connect(self.CON_STR)

    def execute_query(self, query, params=None):
        cursor = self.connect.cursor()
        self.query = query
        result = cursor.execute(self.query, params).fetchall()
        cursor.close()
        return result

    def execute(self, query, params=None):
        cursor = self.connect.cursor()
        self.query = query
        cursor.execute(self.query, params)
        self.connect.commit()
        cursor.close()

    def insert_query(self, query, params=None):
        cursor = self.connect.cursor()
        self.query = query
        cursor.execute(self.query, params)
        self.connect.commit()
        cursor.close()

    def update_query(self, query, params=None):
        cursor = self.connect.cursor()
        self.query = query
        cursor.execute(self.query, params)
        self.connect.commit()
        cursor.close()

    def fetch_value(self, query, params=None):
        cursor = self.connect.cursor()
        self.query = query
        cursor.execute(query, params)
        row = cursor.fetchone()
        cursor.close()
        if row is None:
            return False
        else:
            return row[0]


    def fetch_row(self, query, params=None):
        cursor = self.connect.cursor()
        self.query = query
        cursor.execute(query, params)
        row = cursor.fetchone()
        cursor.close()
        return row

    # Insert a record
    def insert_row(self, table, row):
        ret = True
        placeholders = []
        keys = []
        values = {}
        i = 0
        cursor = self.connect.cursor()
        for key, value in row.items():
            i = i + 1
            bind_var = 'zz' + str(i)

            if value is not None:
                keys.append(key)
                if isinstance(value, DateValue):
                    values[bind_var] = value
                    placeholders.append("TO_DATE(:" + bind_var + ", 'YYYY-MM-DD HH24:MI:SS')")
                elif isinstance(value, LiteralValue):
                    placeholders.append(value.get_value())
                elif isinstance(value, SequenceValue):
                    ret = self.fetch_value('select ' + value.get_value() + '.nextval from dual')
                    placeholders.append(key + " = " + ret)
                elif isinstance(value, ClobValue):
                    clobvar = cursor.var(cx_Oracle.CLOB)
                    clobvar.setvalue(0, value.get_value())
                    cursor.setinputsizes(bind_var=cx_Oracle.CLOB)
                    values[bind_var] = clobvar
                    placeholders.append(':' + bind_var)
                elif isinstance(value, BlobValue):
                    blobvar = cursor.var(cx_Oracle.BLOB)
                    blobvar.setvalue(0, value.get_value())
                    cursor.setinputsizes(bind_var=cx_Oracle.BLOB)
                    values[bind_var] = blobvar
                    placeholders.append(':' + bind_var)
                else:
                    values[bind_var] = value
                    placeholders.append(':' + bind_var)

        columns = ', '.join(keys)
        sql = "INSERT INTO %s ( %s ) VALUES ( %s )" % (table, columns, ', '.join(placeholders))
        cursor.execute(sql, values)
        self.connect.commit()
        return ret

    #######################
    # Update a record
    ##############################
    def update_row(self, table, row, where, where_bind):
        placeholders = []
        values = {}
        values.update(where_bind)
        i = 0
        ret = True
        cursor = self.connect.cursor()
        for key, value in row.items():
            i = i + 1
            bind_var = 'zz_' + str(i)

            if isinstance(value, DateValue):
                values[bind_var] = value
                placeholders.append(key + " = TO_DATE(:" + bind_var + ", 'YYYY-MM-DD HH24:MI:SS')")
            elif isinstance(value, LiteralValue):
                placeholders.append(key + " = " + value.get_value())
            elif isinstance(value, ClobValue):
                clobvar = cursor.var(cx_Oracle.CLOB)
                clobvar.setvalue(0, value.get_value())
                cursor.setinputsizes(bind_var=cx_Oracle.CLOB)
                values[bind_var] = clobvar
                placeholders.append(key + '= :' + bind_var)
            elif isinstance(value, BlobValue):
                blobvar = cursor.var(cx_Oracle.BLOB)
                blobvar.setvalue(0, value.get_value())
                cursor.setinputsizes(bind_var=cx_Oracle.BLOB)
                values[bind_var] = blobvar
                placeholders.append(key + ' = :' + bind_var)
            else:
                values[bind_var] = value
                placeholders.append(key + ' = :' + bind_var)
        sql = "update %s set %s where %s " % (table, ', '.join(placeholders), where)
        cursor.execute(sql, values)
        self.connect.commit()
        return ret

# db = DbConnector('QA.DB.P03.SJC01')
# QUERY="select count(SUBSCRIPTION_ID) from FO_ACCOUNT where USERNAME=:username"
# results = db.execute_query(QUERY, {'username': 'ap_mm'})
# for result in results:
#     print (result[0])
