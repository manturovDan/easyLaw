def get_free(engine):
    query = "SELECT id, status, name, meet_time FROM ticket WHERE status = 8"

    issues = []
    with engine.connect() as con:
        rs = con.execute(query)

        for row in rs:
            issues.append({'id': row[0], 'status': row[1], 'name': row[2], 'meet_time': row[3]})

    print(issues)
    return issues


def can_i_part(my_id, issue, engine):
    query = "SELECT id, status, name, meet_time FROM ticket WHERE id = '" + str(issue) + "';"
    with engine.connect() as con:
        rs = con.execute(query)

        for row in rs:
            if row[1] == 8:
                return True

    return is_mine(my_id, issue, engine)


def is_mine(my_id, issue, engine):
    query_my_issue = "SELECT id FROM lawyers_tickets WHERE ticket=" + str(issue) + " AND lawyer=" + str(my_id) + ";"
    with engine.connect() as con:
        rs = con.execute(query_my_issue)

        for row in rs:
            return True

    return False


def take(my_id, issue, engine):
    query = "START TRANSACTION;" \
            "INSERT INTO lawyers_tickets (ticket, lawyer) VALUES (" + issue + ", " + my_id + ");" \
            "UPDATE ticket SET status=4 WHERE id=" + str(issue) + ";" \
            "COMMIT;"
    with engine.connect() as con:
        if not can_i_part(my_id, issue, engine) or is_mine(my_id, issue, engine):
            return False
        con.execute(query)

        return True
