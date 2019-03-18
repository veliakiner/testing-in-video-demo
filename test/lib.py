from contextlib import contextmanager
import pytest


@contextmanager
def xfail(exception, msg):
    try:
        yield
    except Exception as exc:
        if isinstance(exc, exception):
            pytest.xfail(msg)
        else:
            print("Failed for another reason")
            raise exc
    else:
        raise Exception("Test didn't fail but should've")
