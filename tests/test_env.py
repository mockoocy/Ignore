from src.lang.utils.BuiltIn import BuiltIn
from src.lang.utils.Environment import Environment

abcd = {
    "a": BuiltIn("a1"),
    "b": BuiltIn("b1"),
    "c": BuiltIn("c1"),
    "d": BuiltIn("d1"),
}
abcd_env = Environment(None, abcd)

cdef = {
    "c": BuiltIn("c2"),
    "d": BuiltIn("d2"),
    "e": BuiltIn("e2"),
    "f": BuiltIn("f2"),
}

cdef_env = Environment(abcd_env, cdef)


efgh = {
    "e": BuiltIn("e3"),
    "f": BuiltIn("f3"),
    "g": BuiltIn("g3"),
    "h": BuiltIn("h3"),
}

efgh_env = Environment(cdef_env, efgh)


def test_env_snapshot():
    expected_vars = {
        "a": BuiltIn("a1"),
        "b": BuiltIn("b1"),
        "c": BuiltIn("c2"),
        "d": BuiltIn("d2"),
        "e": BuiltIn("e3"),
        "f": BuiltIn("f3"),
        "g": BuiltIn("g3"),
        "h": BuiltIn("h3"),
    }
    assert Environment(None, expected_vars).variables == efgh_env.create_snapshot()


def test_env_lookup():
    names = ["a", "b", "c", "d", "e", "f"]
    expected_vals = ["a1", "b1", "c2", "d2", "e3", "f3", "g3", "h3"]
    for i, name in enumerate(names):
        assert efgh_env.lookup_variable(name).value == expected_vals[i]
