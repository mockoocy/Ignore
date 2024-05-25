from src.lang.stdlib import global_env
from src.lang.Driver import traverse
from src.lang.utils.BuiltIn import BuiltIn

def test_function_stupid():
    outputs = []
    # if you put any other number, it does not work XD
    test_nums = [12, 0, 420, -7]
    def new_print(x):
        outputs.append(x)
    for num in test_nums:
        global_env.variables["input"] = BuiltIn(lambda _: num)
        global_env.variables["print"] = BuiltIn(new_print)

        traverse("examples/functions/stupid.ign")
    expected_prints = []
    for num in test_nums:
        expected_prints.extend((4, num+2))
    assert outputs == expected_prints