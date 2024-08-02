import sys
import os

#This line of code is modifying the Python path so that the interpreter can locate modules that are not in the default path.
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.logger import logging

def error_msg_details(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info() # will tell every exception on which line and part of code has occured
    file_name = exc_tb.tb_frame.f_code.co_filename # it is custom execption , will be find when search custom Execption python

    error_message = "Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name,exc_tb.tb_lineno,str(error))
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_msg_details(error_message,error_detail)
    
    def __str__(self):
        return self.error_message


