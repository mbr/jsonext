jsonext
=======

.. image:: https://travis-ci.org/mbr/jsonext.svg?branch=master
   :target: https://travis-ci.org/mbr/jsonext


jsonext makes it easy to serialize objects outside of the standard Python
primitives to JSON::

    >>> import jsonext
    >>> from datetime import datetime
    >>> jsonext.dumps(datetime.now())
    '"2014-03-22T22:17:18.304528+00:00"'
    >>> jsonext.dumps(i**2 for i in range(10))
    '[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]'

It uses mixins to the standard encoder to achieve this and is easily reuse-
and extensible. Check out the `documentation <http://pythonhosted
.org/jsonext>`_ for details.
