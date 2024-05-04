
from src.lang.Driver import traverse
from src.lang.utils.VariableInfo import VariableInfo
from src.lang.stdlib import global_env
from copy import deepcopy
def test_scope():
    values = []
    global_env.variables["print"] = VariableInfo(lambda x: values.append(x))
    traverse("examples/scopes/scope1.ign")
    assert values == [5,7,2]
