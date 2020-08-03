class Response:
    code = 0
    message = ""

    def __new__(cls, *args, **kwargs):
        return {
            "code": cls.code,
            "message": cls.message
        }

    def set_code(self, code):
        self.code = code

    def set_message(self, message):
        self.message = message


if __name__ == '__main__':
    r = Response()
    print(type(r))