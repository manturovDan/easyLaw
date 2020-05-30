import datetime


def new_ticket(user, topic, desc, engine):
    query = "INSERT INTO ticket (client, status, name, cr_time, description) VALUES ('" + str(user) + "', 7, '" + topic + "', '" + datetime.datetime.now().isoformat() + "', '" + desc + "');"
    with engine.connect() as con:
        con.execute(query)