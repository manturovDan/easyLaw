def get_tickets(engine):
    query = "SELECT id, status, name, meet_time, cr_time FROM ticket WHERE 1"

    issues = []
    with engine.connect() as con:
        rs = con.execute(query)

        for row in rs:
            issues.append({'id' : row[0], 'status' : row[1], 'name' : row[2], 'meet_time' : row[3], 'cr_time' : row[4]})

    return issues