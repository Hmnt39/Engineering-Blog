from flask import jsonify


class EntityDoesNotExistException(Exception):
    def __init__(self, message=None):
        if not message:
            message = "Entity not found"
        super(EntityDoesNotExistException, self).__init__(message)


class InvalidRequestException(Exception):
    def __init__(self, message=None):
        if not message:
            message = "Invalid Request"
        super(InvalidRequestException, self).__init__(message)


exception_status_code_mapper = {
    InvalidRequestException: 400,
    EntityDoesNotExistException: 404,
}


def serialize_exceptions(func):
    def func_wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            status = exception_status_code_mapper.get(type(e), 500)
            body = jsonify({"message": str(e), "status": status})
        return body, status

    return func_wrapper
