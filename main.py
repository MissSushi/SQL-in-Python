#Einbindung von SQL in Python. Mit pip mysql vorher installieren. Mysql muss im Hintergrund laufen
from mysql.connector import MySQLConnection
from mysql.connector import Error

def create_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = MySQLConnection(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

connection = create_connection("localhost", "root", "")
"""
cursor erstellt wie ein 'Spiegelbild' von connection. Connection ist die Verbindung zum DBMS.
Mit anderen Worten, es wird ein Spiegelbild vom DBMS in der ich mich eingeloggt habe erstellt.
Mit diesem Spiegelbild kann ich z.B. in einer Datenbank a Sachen verändern, die im DBMS wiedergespiegelt werden.
Wenn ich von diesem DBMS aus etwas in einer Datenbank b ändern möchte und gleichzeitig nicht die Datenbank a verlassen will,
muss ich einen weiteren 'cursor' anlegen.
Generell ist es positiv anzusehen wenn man direkt mit einem Cursor arbeitet.

Beispiel:
cursor_a = connection.cursor()
cursor_a.execute("USE DATABASE a")
cursor_b = connection.cursor()
cursor_b.execute("USE DATABASE b")
"""
cursor = connection.cursor()

"""SQL-Befehle werden in 'query' geschrieben. 
Die Befehle werden dann in cursor.execute(query) aufgerufen, wie bei einer normalen Funktion.
Schreibende Befehle die was an der Datenbank ändern oder hinzufügen, danach noch connection.commit(), damit die
Änderungen übernommen werden (wie speichern)


query = ""
connection.execute(query)
connection.commit()

Sobald ich mit allen Änderungen die ich vor habe fertig bin, sollte man es mit cursor.close() und connection.close() schließen.
cursor.close schließt das Spiegelbild und connection.close die Verbindung
cursor.close()
connection.close()
"""