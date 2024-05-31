from src.lang.Driver import traverse
from src.lang.stdlib import global_env
from src.lang.utils.BuiltIn import BuiltIn


def test_loops():
    """
        Tests if nested loops work
    """
    values = []
    global_env.variables["print"] = BuiltIn(lambda x: values.append(x))
    traverse("examples/loops/nested.ign")
    assert values == [1,2,3,4,5]*5

def test_for_loops():
    """
        Tests if nested for loops work
    """
    values = []
    global_env.variables["print"] = BuiltIn(lambda x: values.append(x))
    traverse("examples/loops/nested_for.ign")
    assert values == [1,2,3,4,5]*5
