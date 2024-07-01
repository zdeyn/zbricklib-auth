from flask import Flask
from zbricklib_auth import zAuthManager

from zbricklib.extension import zExtension

def test_is_zextension():
    auth = zAuthManager()
    assert isinstance(auth, zExtension)
