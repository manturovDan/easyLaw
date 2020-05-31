def get_bad_tickets(engine):
    query = "SELECT id, status, name, meet_time, cr_time, client FROM ticket WHERE 1"

    issues = []
    with engine.connect() as con:
        rs = con.execute(query)

        for row in rs:
            rsb = con.execute("SELECT id, message, string, ticket FROM harm WHERE ticket=" + str(row[0]) + " AND active=1;")

            harm = "-"
            for b in rsb:
                harm = b[2]
                break
            issues.append({'id' : row[0], 'status' : row[1], 'name' : row[2], 'meet_time' : row[3], 'cr_time' : row[4], 'harm' : harm, 'client' : row[5]})

    return issues