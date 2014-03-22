import datetime
import times


class JSONDateTimeMixin(object):
    """A mixin for JSONEncoders, encoding :class:`datetime.datetime` and
    :class:`datetime.date` objects by converting them to UNIX timetuples."""
    def default(self, o):
        if isinstance(o, datetime.datetime):
            return times.format(o, 'Zulu')
        if isinstance(o, datetime.date):
            return o.isoformat()
        return super(JSONDateTimeMixin, self).default(o)


class JSONIterableMixin(object):
    """A mixin for JSONEncoders, encoding any iterable type by converting it to
    a list.

    Especially useful for SQLAlchemy results that look a lot like regular lists
    or iterators, but will trip up the encoder."""
    def default(self, o):
        try:
            iterable = iter(o)
        except TypeError:
            pass
        else:
            return list(iterable)
        return super(JSONIterableMixin, self).default(o)


class JSONToDictMixin(object):
    """A mixin for JSONEncoders, encoding any object with a to_dict() method
    by calling that method and encoding the return value."""
    def default(self, o):
        if hasattr(o, 'to_dict'):
            return o.to_dict()
        return super(JSONToDictMixin, self).default(o)


class JSONStringifyMixin(object):
    """A mixing for JSONEncoders, encoding any object that has a __str__
    method with the return value of said function."""
    def default(self, o):
        if hasattr(o, '__str__'):
            return str(o)
        return super(JSONStringifyMixin, self).default(o)
