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


def get_login(id, engine):
    query = "SELECT account FROM users WHERE id='" + id + "'"

    with engine.connect() as con:
        rs = con.execute(query)

        for row in rs:
            return row[0]

        return "###"


def get_name(id, engine):
    query = "SELECT name FROM users WHERE id='" + id + "'"

    with engine.connect() as con:
        rs = con.execute(query)

        for row in rs:
            return row[0]

        return "###"


def get_blog(engine):
    query = "SELECT id, topic, text FROM blog ORDER by id DESC;"

    blog = []
    with engine.connect() as con:
        rs = con.execute(query)

        for row in rs:
            blog.append({'id': row[0], 'topic' : row[1], 'text' : row[2]})

        return blog


def get_art(art, engine):
    query = "SELECT id, topic, text FROM blog WHERE id = " + str(art) + " ;"
    with engine.connect() as con:
        rs = con.execute(query)

        for row in rs:
            return {'id': row[0], 'topic' : row[1], 'text' : row[2]}

        return None