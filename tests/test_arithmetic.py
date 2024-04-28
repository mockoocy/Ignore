
from src.lang.Driver import first_phase, traverse, second_phase
from src.lang.utils.VariableInfo import VariableInfo


def test_parens():
    visitor = traverse("tests/lang_files/arithmetic.ign")
    assert visitor.variables["num1"].value == 22
    assert visitor.variables["num2"].value == 1
    assert visitor.variables["diff"].value == 21

def test_if_stdin():
    outputs = []
    test_nums = [-7, 0, 420, 13]
    expected = ["odd", "even", "even", "odd"]
    for num in test_nums:
        tree, variables = first_phase("examples/if_stdin.ign")
        variables['print'] = VariableInfo(lambda x: outputs.append(x))
        variables['input'] = VariableInfo(lambda _: num)
        second_phase(tree, variables)
    assert outputs == expected
