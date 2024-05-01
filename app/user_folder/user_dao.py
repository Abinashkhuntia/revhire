import sqlite3
from ..model import user
from ..dto import user_request
from ..dto import user_response
import logging

logging.basicConfig(filename="users.log", encoding='utf-8', filemode='a', level=logging.INFO)
logger = logging.getLogger(__name__)

class UserDAO:
    # con = sqlite3.connect("/mnt/c/Computer_science/devops/revature/revhire/revhire.db", check_same_thread=False)
    con = sqlite3.connect("/revhire/revhire.db", check_same_thread=False) # for docker

    cursor = con.cursor()

    def create_user(self, user_request:user_request.UserRequest):

        try:
            self.cursor.execute(
                """SELECT * FROM USER WHERE email = ?""",
                (user_request.email,),
            )
            if self.cursor.fetchone() is not None:
                logging.error("User with this email already exists")
                raise Exception("User with this email already exists")
            
            self.cursor.execute(
                """INSERT INTO USER(name, email, password, role) VALUES(?, ?, ?, ?)""",
                (user_request.name, user_request.email, user_request.password,user_request.role ),
            )
            self.con.commit()

            logging.info("User created")
            return "created"
        
        except Exception as e:
            logging.error(f"Error in creating new user : {e}")
            raise Exception("unable to insert user information")

    
    def get_users(self):
        res = self.cursor.execute(
            """SELECT * from USER"""
        )
        self.con.commit()
        return res.fetchall()
    
    def update_user(self, user_request:user_request.UserRequest, id:int):
        self.cursor.execute(
            """UPDATE USER SET name = ?, email = ?, password = ? WHERE id = ?""",(
                user_request.name,user_request.email,user_request.password, id )
        )

        res = self.cursor.execute(
            """SELECT * FROM USER WHERE id = ?""", (id)
        )

        user = res.fetchone()
        self.con.commit()

        user_response = user_response.UserResponse(user.id, user.name, user.email, user.role)
        return user_response

    def delete_user(self, id):
        self.cursor.execute("""DELETE FROM USER WHERE id = ?""", (id))
        self.con.commit()
        return "User deleted"

    
    def login(self, login):
        self.cursor.execute(
            """SELECT * FROM USER WHERE email = ? AND password = ? AND role = ?""",
            (login.email, login.password , login.role),
        )
        user = self.cursor.fetchone()
        if user is None:
            logging.error("User not found")
            raise Exception("User not found")
        return 1
    