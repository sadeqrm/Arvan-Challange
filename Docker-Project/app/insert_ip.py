import psycopg2


def insert_geoip(ip_address,country):
    connection = psycopg2.connect(
    host="postgres",
    database="ps_db",
    user="ps_admin",
    password="1234"
    )
    

    # ایجاد cursor
    cursor = connection.cursor()

    #ip_address = "8.8.8.8"
    #country = "US"

    insert_query = "INSERT INTO geoip (ip_address, country) VALUES (%s, %s)"
    cursor.execute(insert_query, (ip_address, country))

    connection.commit()

    print("Data inserted successfully")

    cursor.close()
    connection.close()

def find_ip(ip_address):
    connection = psycopg2.connect(
    host="postgres",
    database="ps_db",
    user="ps_admin",
    password="1234"
    )

    cursor = connection.cursor()

   
    query = "SELECT country FROM geoip WHERE ip_address = %s;"

    # اجرای کوئری
    cursor.execute(query, (ip_address,))

    # گرفتن نتایج
    rows = cursor.fetchall()

    # print(len(rows),rows[0][0])
    # for row in rows:
    #     print(f"Country: {row[0]}")


    # بستن cursor و connection

    cursor.close()
    connection.close()
    try:
        return len(rows),rows[0][0]
    except:
        return 0,""

#find_ip("8.8.8.8")
