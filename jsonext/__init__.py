"""JSON-rendering helpers.

This module provides mixins for the stdlib :class:`json.JSONEncoder` class,
adding serialization methods for other object types, such as
:class:`~datetime.datetime` objects or iterables.

All these are ready to use by using :data:`~jsonext.dumps`.
"""

import functools
import json

from .mixins import (
    JSONDateTimeMixin, JSONIterableMixin, JSONToDictMixin, JSONStringifyMixin,
)
from .wrappers import ISO88601Wrapper


class JSONEncoder(JSONDateTimeMixin, JSONIterableMixin, JSONToDictMixin,
                  JSONStringifyMixin, json.JSONEncoder):
    pass


JSONDecoder = ISO88601Wrapper(json.JSONDecoder())

dumps = functools.partial(json.dumps, cls=JSONEncoder)
loads = JSONDecoder.decode
