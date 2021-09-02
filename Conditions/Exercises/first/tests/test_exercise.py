import pytest
import src.age
from tests.input_data import input_values

# Define the parametrization based on the inputs from the input_data file
@pytest.mark.parametrize("value, result, message", input_values)
def test_age(value, result, message):
    """
    Tests the code in src.age using the inputs from tests.input_data.
    Asserts that what is printed in the terminal is the same as
    the expected result.

    Parameters:
        value: list(str)
            The values that are used as input for the test.
            Usually strings, since we are simulating input from user.
        result: list(str)
            The expected output in the terminal, usually what the user prints
        message: str
            A hint string in case of an error
    """
    output = []

    def mock_input(input_s=None):
        """
        Create a mock input, where each input is obtained from
        the list of inputs. Appends the input to a list.

        Parameters:
            input_s: str
                Input from the test age.
        """
        if input_s is not None:
            output.append(input_s)
        else:
            output.append("")

        return value.pop(0)

    src.age.input = mock_input
    # src.age.print = lambda s : output.append(s)
    src.age.print = lambda *args: output.append(" ".join(map(str, args)))

    src.age.main()

    assert output == result, message
