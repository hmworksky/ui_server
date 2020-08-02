class Response:
    code = 0
    message = ""

    def __new__(cls, *args, **kwargs):
        return {
            "code": cls.code,
            "message": cls.message
        }
