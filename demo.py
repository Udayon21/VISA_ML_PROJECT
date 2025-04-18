from VISA_ML_PROJECT.logger import logging
from VISA_ML_PROJECT.exception import visaException
import sys
#logging.info("Welcome to our custom log")

try:
    a=2/0
except Exception as e:
    raise  visaException(e,sys)   
