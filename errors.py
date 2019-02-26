class ValidationError(Exception):
    
    def __init__(self, message:str):
        Exception.__init__(message)
