import logging.config
import mysql.connector
import logging
logger = logging.getLogger(__name__)

try:
    connection = mysql.connector.connect(
            user="root",
            password="TGIydaGzqj8nkXiR40rkLRtH0HSlkGPL",
            host="arkobot-members.arkobot.svc",
            database="mainDB",
            port=3306
    )
    print("Connected to MySQL successfully.")
    print(connection)
    executer=connection.cursor()
except mysql.connector.Error as err:
    logger.error(f"Failed to connect to MySQL: {err}")
    

def main():
    ...


def GetCredits(username):
    
    executer.execute('Select Credits FROM users WHERE UserName = "{}"'.format(username))
    result=executer.fetchone()
    result=result[0]
    print(result)
    return result

def LoseCredits(username):
    try:
        executer.execute('UPDATE users SET credits = credits-1 WHERE UserName = "{}"'.format(username))
        return "lost credits!"
    except:
        return "cant lose credits"
if __name__=="__main__":
    main()