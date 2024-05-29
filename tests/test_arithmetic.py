from src.lang.Driver import traverse
from src.lang.stdlib import global_env
from src.lang.utils.BuiltIn import BuiltIn


def test_parens():
    visitor = traverse("tests/lang_files/arithmetic.ign")
    # We store variable declarations as keys (as they uniquely identify each object by memory address)
    variable_declarations = visitor.variables
    # Then we can extract their names and values. It only works if the names are not shadowed by some inner scope.
    variables = {
        ctx.FUNCTION_NAME().getText()[5:]: val
        for (ctx, val) in variable_declarations.items()
    }
    print(variables)
    assert variables["num1"].value == 22
    assert variables["num2"].value == 1
    assert variables["diff"].value == 21


def test_if_stdin():
    outputs = []
    test_nums = [-7, 0, 420, 13]
    expected = ["odd", "even", "even", "odd"]
    for num in test_nums:
        global_env.variables["print"] = BuiltIn(lambda x: outputs.append(x))
        global_env.variables["input"] = BuiltIn(lambda _: num)
        traverse("examples/conditional/if_stdin.ign")

    assert outputs == expected
