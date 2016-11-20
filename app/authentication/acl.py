from functools import wraps
from flask import abort, request

class Acl:
    TOKEN_HEADER = 'x-token'
    def validate(self, fn):
        
        @wraps(fn)
        def tokenVerification(*args, **kwargs):
            from user import User

            user = User.getTokenUser(self.getToken())
            # TODO resource management

            if user is not None:
                return fn(*args, **kwargs)
            else:
                abort(403)

        return tokenVerification

    def getToken(self):
        if self.TOKEN_HEADER not in request.headers:
            return ""
        return request.headers[self.TOKEN_HEADER]
