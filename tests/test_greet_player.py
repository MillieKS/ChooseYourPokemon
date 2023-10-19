
from lib.greet_player import *
import builtins
import pytest

def test_return_error_when_no_input_is_given():
    # Simulate user input by replacing the input function
    original_input = builtins.input
    builtins.input = lambda _: ""

    result = greet_player()  # Call the greet_player function

    # Restore the original input function
    builtins.input = original_input

    # Check if the result matches the expected exception meassage
    with pytest.raises(Exception) as err:
        error = str(err.value)
        assert error == "you need to enter a name"


def test_return_input_name_with_greet():
    # Simulate user input by replacing the input function
    original_input = builtins.input
    builtins.input = lambda _: "kimchi"

    result = greet_player()  # Call the greet_player function

    # Restore the original input function
    builtins.input = original_input

    # Check if the result matches the expected output
    assert result == 'Ready for battle kimchi?'