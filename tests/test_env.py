from src.lang.utils.Environment import Environment
from src.lang.utils.VariableInfo import VariableInfo

abcd = {
    "a": VariableInfo("a1"),
    "b": VariableInfo("b1"),
    "c": VariableInfo("c1"),
    "d": VariableInfo("d1"),
}
abcd_env = Environment(None, abcd)

cdef = {
    "c": VariableInfo("c2"),
    "d": VariableInfo("d2"),
    "e": VariableInfo("e2"),
    "f": VariableInfo("f2"),
}

cdef_env = Environment(abcd_env, cdef)


efgh = {
    "e": VariableInfo("e3"),
    "f": VariableInfo("f3"),
    "g": VariableInfo("g3"),
    "h": VariableInfo("h3"),
}

efgh_env = Environment(cdef_env, efgh)


def test_env_snapshot():
    expected_vars = {
        "a": VariableInfo("a1"),
        "b": VariableInfo("b1"),
        "c": VariableInfo("c2"),
        "d": VariableInfo("d2"),
        "e": VariableInfo("e3"),
        "f": VariableInfo("f3"),
        "g": VariableInfo("g3"),
        "h": VariableInfo("h3"),
    }
    assert Environment(None, expected_vars).variables == efgh_env.create_snapshot()


def test_env_lookup():
    names = ["a", "b", "c", "d", "e", "f"]
    expected_vals = ["a1", "b1", "c2", "d2", "e3", "f3", "g3", "h3"]
    for i, name in enumerate(names):
        assert efgh_env.lookup_variable(name).value == expected_vals[i]
