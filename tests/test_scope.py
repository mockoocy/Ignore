from src.lang.Driver import traverse
from src.lang.stdlib import global_env
from src.lang.utils.BuiltIn import BuiltIn


def test_scope():
    values = []
    global_env.variables["print"] = BuiltIn(lambda x: values.append(x))
    traverse("examples/scopes/scope1.ign")
    assert values == [5, 7, 2]
