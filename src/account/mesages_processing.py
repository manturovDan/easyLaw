import datetime


def send(issue, author, message, engine):
    query = "INSERT INTO messages (author, ticket, text, time) VALUES (" + author + ", " + issue + ", '" + message + "', '" + datetime.datetime.now().isoformat() + "' )"
    with engine.connect() as con:
        rs = con.execute(query)