from werkzeug.exceptions import HTTPException


class APIError(Exception):

    def __init__(self, message='Bad Request', response=None, code=400,
                 field='unknown', resource='unknown'):
        Exception.__init__(self)
        self.response = response
        self.status_code = code
        self.field = field
        self.message = message
        self.resource = resource

    def get_response(self, environment):
        resp = super(APIError, self).get_response(environment)
        resp.status = "%s %s" % (self.code, self.name.upper())
        return resp


class RateLimitError(APIError):

    def __init__(self, response=None, code=429, field='unknown',
                 resource='unknown', message='Too Many Requests'):
        Exception.__init__(self)
        self.response = response
        self.status_code = code
        self.field = field
        self.message = message
        self.resource = resource


class ImproperlyConfigured(RuntimeError):
    pass


class VoucherException(LookupError):
    pass