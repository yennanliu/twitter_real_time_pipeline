import os


def rm(filename):
    os.remove(filename)


def test_rm(mocker):
    filename = 'test.file'
    mocker.patch('os.remove')
    rm(filename)
    os.remove.assert_called_once_with(filename)