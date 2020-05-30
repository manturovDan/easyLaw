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


def get_full_info(issue, engine):
    queryT = "SELECT id, client, status, meet_time, name, cr_time, description FROM ticket WHERE id=" + str(issue) + ";"
    queryL = "SELECT users.id, users.name FROM users INNER JOIN lawyers_tickets ON lawyers_tickets.ticket=" + str(issue) + " AND lawyers_tickets.lawyer = users.id;";
    with engine.connect() as con:
        rst = con.execute(queryT)
        rsl = con.execute(queryL)

        for rowt in rst:
            print(rowt)

        for rowl in rsl:
            print(rowl)


def pay(issue, engine):
    query = "UPDATE ticket SET status=8 WHERE id=" + str(issue) + ";"

    with engine.connect() as con:
        rs = con.execute(query)
