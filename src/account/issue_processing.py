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
    queryT = "SELECT ticket.id, ticket.client, ticket.status, ticket.meet_time, ticket.name, ticket.cr_time, ticket.description, users.name FROM ticket INNER JOIN users ON users.id=ticket.client WHERE ticket.id=" + str(issue) + ";"
    queryL = "SELECT users.id, users.name FROM users INNER JOIN lawyers_tickets ON lawyers_tickets.ticket=" + str(issue) + " AND lawyers_tickets.lawyer = users.id;";
    with engine.connect() as con:
        rst = con.execute(queryT)
        rsl = con.execute(queryL)

        issue = {'id' : None, 'client' : None, 'status' : None, 'meet_time' : None, 'name':None, 'cr_time':None, 'desc':None}
        for rowt in rst:
            print(rowt)
            issue['id'] = rowt[0]
            issue['client'] = rowt[1]
            issue['status'] = rowt[2]
            issue['meet_time'] = rowt[3]
            issue['name'] = rowt[4]
            issue['cr_time'] = rowt[5]
            issue['desc'] = rowt[6]
            issue['client_name'] = rowt[7]
            break

        lawyers = []
        for rowl in rsl:
            lawyers.append({'lawyer_id' : rowl[0], 'lawyer_name' : rowl[1]})

        return issue, lawyers


def pay(issue, engine):
    query = "UPDATE ticket SET status=8 WHERE id=" + str(issue) + ";"

    with engine.connect() as con:
        rs = con.execute(query)


def text_status(num):
    if num == 1:
        return "Ожидает рассмотрения"
    elif num == 2:
        return "Назначена встреча"
    elif num == 3:
        return "Сообщение от юриста"
    elif num == 4:
        return "В работе"
    elif num == 5:
        return "Ожидание Ваших действий"
    elif num == 6:
        return "Завершено"
    elif num == 7:
        return "Ожидание платежа"
    else:
        return "Поиск юриста"
