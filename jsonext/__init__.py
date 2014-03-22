from core import DateTimeEncoderMixin, IterableEncoderMixin
from json import JSONEncoder


class ToJSONEncoder(DateTimeEncoderMixin,
                    IterableEncoderMixin,
                    )
