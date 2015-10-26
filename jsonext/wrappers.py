import arrow
import datetime
import re

import six


class DecoderWrapper(object):
    def __init__(self, decoder):
        self._decoder = decoder

    def _convert_dict(self, v):
        return {k: self._convert(v) for k, v in six.iteritems(v)}

    def _convert_list(self, v):
        return [self._convert(v) for v in iter(v)]

    def _convert_text(self, v):
        return v

    def _convert_integer(self, v):
        return v

    def _convert_float(self, v):
        return v

    def _convert_bool(self, v):
        return v

    def _convert_none(self, v):
        return v

    def _convert(self, value):
        if isinstance(value, dict):
            return self._convert_dict(value)
        if isinstance(value, list):
            return self._convert_list(value)
        if isinstance(value, six.text_type):
            return self._convert_text(value)
        if isinstance(value, six.integer_types):
            return self._convert_integer(value)
        if isinstance(value, float):
            return self._convert_float(value)
        if isinstance(value, bool):
            return self._convert_bool(value)
        if value is None:
            return self.convert_none(value)
        assert False, 'unreachable'

    def decode(self, *args, **kwargs):
        val = self._decoder.decode(*args, **kwargs)
        return self._convert(val)

    def raw_recode(self, *args, **kwargs):
        val = self._decoder.raw_decode(*args, **kwargs)
        return self._convert(val)


class ISO88601Wrapper(DecoderWrapper):
    DATE_RE = re.compile(r'^\d{4}-\d{2}-\d{2}$')
    TIME_RE = re.compile(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}[^\s]*$')

    def _convert_text(self, v):
        try:
            if self.DATE_RE and self.DATE_RE.match(v):
                return arrow.get(v).date()

            if self.TIME_RE and self.TIME_RE.match(v):
                return arrow.get(v).to('utc').naive
        except arrow.ParserError:
            return v

        return v
