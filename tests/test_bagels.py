import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import pytest
from app import bagels


def test_getSecretNum_1():
    result = bagels.getSecretNum()
    assert isinstance(result, str)


def test_getSecretNum_2():
    result = bagels.getSecretNum()
    assert len(result) == 3
