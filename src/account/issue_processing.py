import datetime


def new_ticket(user, topic, desc, engine):
    query = "INSERT INTO ticket (client, status, name, cr_time, description) VALUES ('" + str(user) + "', 7, '" + topic + "', '" + datetime.datetime.now().isoformat() + "', '" + desc + "');"
    with engine.connect() as con:
        con.execute(query)


def is_my_issue(user, issue, engine):
    query = "SELECT id from ticket WHERE id=" + str(issue) + " AND client=" + str(user) + ";"

    with engine.connect() as con:
        rs = con.execute(query)

        for row in rs:
            return True

        return False


def get_status(issue, engine):
    query = "SELECT status FROM ticket WHERE id=" + str(issue) + ";"

    with engine.connect() as con:
        rs = con.execute(query)

        for row in rs:
            return row[0]

        return 0


def pay(issue, engine):
    query = "UPDATE ticket SET status=8 WHERE id=" + str(issue) + ";"

    with engine.connect() as con:
        rs = con.execute(query)
