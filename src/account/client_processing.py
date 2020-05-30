from flask import request, make_response, render_template
from src.account import issue_processing


def get_tickets(user, engine):
    query = "SELECT id, status, name, meet_time FROM ticket WHERE client='" + user + "'"

    issues = []
    with engine.connect() as con:
        rs = con.execute(query)

        for row in rs:
            issues.append({'id' : row[0], 'status' : issue_processing.text_status(row[1]), 'name' : row[2], 'meet_time' : row[3]})

    print(issues)
    return issues