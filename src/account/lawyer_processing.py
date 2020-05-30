def get_free(engine):
    query = "SELECT id, status, name, meet_time FROM ticket WHERE status = 8"

    issues = []
    with engine.connect() as con:
        rs = con.execute(query)

        for row in rs:
            issues.append({'id': row[0], 'status': row[1], 'name': row[2], 'meet_time': row[3]})

    print(issues)
    return issues