from utilities.Utils import *


class TestmySQLOne(UtilClassOne):
    def test_mySQLTC1(self, log):
        log.info("testing mysql")
        host = self.getConfig("test_mySQLTC1", "host")
        database = self.getConfig("test_mySQLTC1", "database")
        user = self.getConfig("test_mySQLTC1", "user")
        password = self.getConfig("test_mySQLTC1", "password")
        conn = mysql.connector.connect(host=host, database=database, user=user,
                                       password=password)
        log.info(conn.is_connected())
        query1 = self.getConfig("test_mySQLTC1", "query1")



        sQ = self.sendMySQLQuery(conn, query1)
        log.info(sQ)
        query = self.getConfig("test_mySQLTC1", "query")

        sQall = self.sendMySQLQuery(conn, query)
        log.info(sQall)
        d = []
        d1 = []
        for row in sQall:
            # convert the tuple from DB query into dictionary that we can use for posting say in API in JSON format
            data = {"name": row[0], "job": row[1], "id": row[2]}
            data1 = {"name": row[0], "job": row[1]}
            d.append(data)
            d1.append(data1)

        log.info(d1)
        log.info(d1[1])

        D123 = d1[2]
        D12 = d1[1]
        url = self.getConfig("test_mySQLTC1", "url")
        res = requests.post(url, data=D123)
        log.info(res.status_code)
        J = res.json()
        log.info(J)
        res = requests.post(url, data=D12)
        log.info(res.status_code)
        J = res.json()
        log.info(J)


