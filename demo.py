from us_visa.exception import USvisaException
from us_visa.logger import logging
import sys

try:
    a=2/1
    logging.info("logger file created")
except Exception as e:
    USvisaException(e,sys)