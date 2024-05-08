from src.lang.stdlib import global_env
from src.lang.Driver import first_phase, second_phase
from src.lang.utils.VariableInfo import VariableInfo

def test_function_stupid():
    outputs = []
    test_nums = [13, 0, 420, -7]
    for num in test_nums:
        tree, variables = first_phase("examples/functions/stupid.ign")

        global_env.variables["print"] = VariableInfo(lambda x: outputs.append(x))
        global_env.variables["input"] = VariableInfo(lambda _: num)
        print("input gives", num)
        second_phase(tree, variables)
    expected_prints = []
    for num in test_nums:
        expected_prints.extend((4, num+2))
    assert outputs == expected_prints