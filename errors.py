''' Custom errors to aid in catching specific errors. '''
class ValidationError(Exception):
    ''' This is used for the `validate()` method, indicating invalidation.  '''
    def __init__(self, message:str):
        Exception.__init__(self, message)
