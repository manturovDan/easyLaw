import datetime
import re


def send(issue, author, message, engine):
    query = "INSERT INTO messages (author, ticket, text, time) VALUES (" + author + ", " + issue + ", '" + message + "', '" + datetime.datetime.now().isoformat() + "' )"
    with engine.connect() as con:
        rs = con.execute(query)

        last = con.execute("SELECT LAST_INSERT_ID();")
        msg = None
        for l in last:
            msg = l[0]
            break

        res = re.search(r'([0-9]{11})|@(\S)*', message)
        try:
            bad = res.group(1)
            con.execute("INSERT INTO harm (message, string, ticket) VALUES (" + str(msg) + ", '" + bad + "', " + issue + ")")
        except Exception as e:
            print(e)


