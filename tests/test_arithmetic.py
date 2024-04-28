import os

from src.lang.Driver import traverse


def test_parens():
    visitor = traverse("tests/lang_files/arithmetic.ign")
    assert visitor.variables["num1"].value == 22
    assert visitor.variables["num2"].value == 1
    assert visitor.variables["diff"].value == 21
