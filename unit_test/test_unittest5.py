import time
import pytest


# ------- this mod_header should run once at the module -------#
@pytest.fixture(scope="module", autouse=True)
def mod_header(request):
    print('\n-----------------')
    print('module      : %s' % request.module.__name__)
    print('-----------------')

# ------- this func_header should run once at every test (test_one, test_two)-------#
@pytest.fixture(scope="function", autouse=True)
def func_header(request):
    print('\n-----------------')
    print('function    : %s' % request.function.__name__)
    print('time        : %s' % time.asctime())
    print('-----------------')

def test_one():
    print('in test_one()')
    assert 0

def test_two():
    print('in test_two()')
    assert 0

