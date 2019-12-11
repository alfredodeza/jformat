from jformat import main


def test_yes_is_true():
    result = main.str_to_bool('yes')
    assert result == True
