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



"""Try except block is used to capture any error, instead of failing the code. In below example
if the division "try" block fails a error message will e displayed along with the result of 'add'. The add
and the error message is executed only when the 'try' block fails."""

def division(a,b):
    try:
        out = a/b
        return out
    except Exception as e:
        #print("Their is some error in the input",e)
        logger.info(e)
        add = a+b
        return add
    

#out = division(4,2)

# Expected error, division by zero
out = division(4,0)
print(out)



