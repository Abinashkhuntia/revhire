from fastapi import FastAPI, HTTPException
import logging
import  jwt
# from user_service import UserService
from .dto import user_request
from .dto import user_response
from .dto import login_credentials
# from user_folder import user_dao
from .user_folder import user_service

logging.basicConfig(filename="user_controller.log", encoding='utf-8', filemode='a', level=logging.INFO)

logger=logging.getLogger(__name__)  

app = FastAPI()

user_service = user_service.UserService()

@app.get("/")
def read_root():
    return {"Hello"}

@app.get("/users")
def get_users(user_jwt:str):
    try:
        user_info = jwt.decode(user_jwt, "secret", algorithms=["HS256"])
        logger.info(f"User data retrieved: {user_info}")
        return user_info
    except Exception as e:
        logger.error(f"Error occurred: {e}")
        return {"error": str(e)}

@app.post("/signup")
def create_user(user_request:user_request.UserRequest):    #it expects a UserRequest object ie. name, email, password, role
    try:
        user_service.create_user(user_request)
        logger.info("User Created")
        return "user created"
    except Exception as e:
        logger.error("failed to create user, user exists already")
        raise HTTPException(status_code=500, detail="failed to create user,user exists already")

@app.post("/login")
def login(login:login_credentials.Login):
    try:
        token=user_service.login(login)
        logger.info("User Logged in")
        return {"token": token}
    except Exception as e:        
        logger.error(f"Unable to login {e}")
        raise HTTPException(status_code=500, detail="Unable to login")
    
# @app.put("/update/{id}")ls

