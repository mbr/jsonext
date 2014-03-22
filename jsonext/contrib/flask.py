from werkzeug.exceptions import HTTPException


class HTTPExceptionEncoderMixin(object):
    """A mixin for JSONEncoders, encoding
    :class:`~werkzeug.exceptions.HTTPException` instances.

    The format is similiar to::

        {
          "error": {"description": "You need to login",
                    "code": 401}
        }
    """
    def default(self, o):
        if isinstance(o, HTTPException):
            return {
                'error': {
                    'description': o.description,
                    'code': o.code,
                }
            }
        super(HTTPExceptionEncoderMixin, self).default(o)
