import datetime

import times


class DateTimeEncoderMixin(object):
    """A mixin for JSONEncoders, encoding :class:`datetime.datetime` and
    :class:`datetime.date` objects by converting them to UNIX timetuples."""
    def default(self, o):
        if isinstance(o, datetime.datetime):
            return times.format(o, 'Zulu')
        if isinstance(o, datetime.date):
            return o.isoformat()
        return super(DateTimeEncoderMixin, self).default(o)


class IterableEncoderMixin(object):
    """A mixin for JSONEncoders, encoding any iterable type by converting it to
    a list.

    Especially useful for SQLAlchemy results that look a lot like regular lists
    or iterators, but will trip up the encoder."""
    def default(self, o):
        if hasattr(o, '__iter__'):
            return list(iter(o))

        return super(IterableEncoderMixin, self).default(o)


class ToJsonEncoderMixin(object):
    def default(self, o):
        to_json = getattr(o, 'to_json')
        if callable(tojson):
            return to_json()
