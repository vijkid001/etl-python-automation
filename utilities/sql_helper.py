def execute_query(connection, query):

    cursor = connection.cursor()

    cursor.execute(query)

    result = cursor.fetchall()

    cursor.close()

    return result