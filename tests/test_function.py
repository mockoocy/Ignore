from src.lang.stdlib import global_env
from src.lang.Driver import traverse
from src.lang.utils.BuiltIn import BuiltIn

def test_function_add2():
    outputs = []
    test_nums = [22, 0, 420, -7]
    def new_print(x):
        outputs.append(x)
    for num in test_nums:
        global_env.variables["input"] = BuiltIn(lambda _: num)
        global_env.variables["print"] = BuiltIn(new_print)

        traverse("examples/functions/add2.ign")
    expected_prints = []
    for num in test_nums:
        expected_prints.extend((4, num+2))
    assert outputs == expected_prints


def test_fib():
    expected_nums = [0,1,1,2,3,5,8,13,21,34]
    expected_out = [f"Fib({idx}) is: {num}" for (idx, num) in enumerate(expected_nums)]
    outputs = []
    global_env.variables["print"] = BuiltIn(lambda x: outputs.append(x))
    traverse("examples/functions/fibonacci.ign")
    assert outputs == expected_out

def test_currying():
    outputs = []
    global_env.variables["print"] = BuiltIn(lambda x: outputs.append(x))
    traverse("examples/functions/curry.ign")
    assert outputs == [6]
    