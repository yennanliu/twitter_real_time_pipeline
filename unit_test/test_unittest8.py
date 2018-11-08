class ForTest:
    field = 'origin'

    def method():
        pass


def test_for_test(mocker):
    test = ForTest()
    mock_method = mocker.patch.object(test, 'method')
    test.method()
    assert mock_method.called

    assert 'origin' == test.field
    mocker.patch.object(test, 'field', 'mocked')
    assert 'mocked' == test.field