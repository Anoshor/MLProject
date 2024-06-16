import sys
import logging

def error_message_detail(err, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    msg = "Error occured in python script [{0}] line number [{1}] error message[{2}]".format(
        file_name, exc_tb.tb_lineno, str(err)
    )

    return msg


class CustomException(Exception):

    def __int__(self, msg, error_detail:sys):
        super().__init__(msg)
        self.msg = error_message_detail(msg, error_detail=error_detail)

    def __str__(self) -> str:
        return self.msg
    
