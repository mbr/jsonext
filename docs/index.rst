jsonext
=======

jsonext is a small library that collects commonly used implementations of
JSON-serializers for various objects. A good example are
:class:`~datetime.datetime` objects, which are commonly found in web
applications. Since JSON does not know these types, they need to be
serialized to strings - certainly not an impossible task,
but tricky enough to get right when timezones are involved that it's a turn
off to reimplement them every time.

There are many other libraries on PyPI that somehow deal with this problem
or a related one, though many of those are either dead or do a horrible job
of wrapping the standard JSON library in funky ways.


Encoders and Mixins
-------------------

jsonext works with the standard libraries facilities as closely as possible;
new encoding methods are added as mixins::

  from json import JSONEncoder
  from jsonenc.mixins import JSONDateTimeMixin, JSONIterableMixin

  class MyJSONEncoder(JSONDateTimeMixin, JSONIterableMixin, JSONEncoder):
      pass

  # ...

  enc = MyJSONEncoder()
  enc.encode(data)

The example above will encode ``data`` as JSON,
using :class:`~jsonext.mixins.JSONDateTimeMixin` to encode any
:class:`~datetime.datetime` objects found and any iterables using
:class:`~jsonext.mixins.JSONIterableMixin`. All these are just mixins for
the stdlib's :class:`~json.JSONEncoder`.

Behind the scene these mixins provide a :meth:`~json.JSONEncoder.default`
method that will check for types it can encode and either return the result
or call the superclasses default method. An example implementation for a
custom class ``Foo`` is simple::

  class JSONFooMixin(object):
      def default(self, o):
          if isinstance(o, Foo):
              # return anything composed of objects the encoder can handle
              return ('This is a Foo object as a tuple', Foo.value)
          return super(JSONFooMixin, self).default(o)


Shortcuts
---------

Some shortcuts are provided if less customization is needed. The
:class:`jsonext.JSONEncoder` is a :class:`json.JSONEncoder` with some
commonly useful classes mixed in: :class:`~jsonext.mixins.JSONDateTimeMixin`,
:class:`~jsonext.mixins.JSONIterableMixin`,
:class:`~jsonext.mixins.JSONToDictMixin`,
:class:`~jsonext.mixins.JSONStringifyMixin` and
:class:`~jsonext.mixins.json.JSONEncoder`.

In addition, the :func:`jsonext.dumps` function is the same as
:func:`json.dumps`, except is uses :class:`jsonext.JSONEncoder` as the
encoder per default. This means that::

  import jsonext

  jsonext.dumps(some_data)

will just work.


API Reference
-------------

The following mixins are provided:

.. automodule:: jsonext.mixins
   :members:
