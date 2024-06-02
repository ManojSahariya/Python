"""This is a sample why we use logging. The output of this code will be printed in the terminal and will not be 
available post new run. We need to log the output of the code when we host the code in the server"""
# def add_number(a,b):
#     out = a+b
#     print("successfully executed")

#     return out

# num = add_number(3,4)
# print(num)





import logging
import os

#create a logger script
logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s]"

log_folder = "Logs"
log_file = "Logs/Running_log.log"
os.makedirs(log_folder, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_file)
    ]

)
logger = logging.getLogger("mylog")




def add_number(a,b):
    out = a+b
    #print("successfully executed")
    logger.info("successfully executed")

    return out

num = add_number(3,4)
print(num)

