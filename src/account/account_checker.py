from flask import request, make_response, render_template


def check_session(engine):
    user = request.cookies.get('user')
    session = request.cookies.get('session')

    if user is None and session is None:
        return False

    query = "SELECT old FROM sessions WHERE user='" + user + "' AND hash = '" + session + "';"
    with engine.connect() as con:
        rs = con.execute(query)

        for row in rs:
            return True

        return False


def my_type(id, engine):
    query = "SELECT type FROM users WHERE id='" + id + "'"

    with engine.connect() as con:
        rs = con.execute(query)

        for row in rs:
            return row[0]

        return 0
