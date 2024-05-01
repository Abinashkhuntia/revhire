from .user_dao import UserDAO
from ..dto import user_request
from ..dto import login_credentials
import logging 
import  jwt
logging.basicConfig(filename="users.log", encoding='utf-8', filemode='a', level=logging.INFO)
logger = logging.getLogger(__name__)

class UserService:

    def create_user(self, user_request:user_request.UserRequest):
        try:
            user_dao = UserDAO()
            user_dao.create_user(user_request)
            logger.info("User Created")
            return "User Created"
        except Exception as e:
            logger.error(f"Unable to create user {e}",e)
            raise Exception("Unable to create user")


    # def login(self, login: Login):
    #     try:
    #         user_dao = UserDAO()
    #         user_dao.login(login)
    #         logger.info("User Logged in")
    #         return "User Logged in"
    #     except Exception as e:
    #         logger.error(f"Unable to login {e}",e)
    #         raise Exception("Unable to login")

    def login(self, login: login_credentials.Login):
        try:
            user_dao = UserDAO()
            user = user_dao.login(login)
            if user is not None:
                # User is authenticated, now we need to generate a token
                token= jwt.encode(claims={"email":login.email,"password":login.password},key='secret',algorithm='HS256')
                logger.info("User Logged in")
                return token
            else:
                raise Exception("Invalid credentials")
        except Exception as e:
            logger.error(f"Unable to login {e}",e)
            raise Exception("Unable to login")
    
    def update_user(self, user_request:user_request.UserRequest, id:int):
        try:
            user_dao = UserDAO()
            user_dao.update_user(user_request, id)
            logger.info("User updated")
            return "User updated"
        except Exception as e:
            logger.error(f"Unable to update user {e}",e)
            raise Exception("Unable to update user")