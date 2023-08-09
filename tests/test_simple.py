import pytest
from SimpleTests.simple_tests import SimpleTests


def test_simple():
    simple = SimpleTests("")
    assert simple.hello() == "Hello World!"


@pytest.mark.parametrize("test_input, expected", [
    ('a', 'a'),
    ('b', 'b'),
    ('c', 'c'),
])
def test_constructor(test_input, expected):
    simple = SimpleTests(test_input)

    assert simple.getString() == expected


@pytest.mark.parametrize("test_input, expected", [
    ('a', 'a'),
    ('b', 'b'),
    ('c', 'c'),
])
def test_get_set(test_input, expected):
    simple = SimpleTests("")

    assert simple.getString() == ""

    simple.setString(test_input)

    assert simple.getString() == expected


@pytest.mark.skip(reason="Sum not supported yet")
@pytest.mark.parametrize("x, y, expected", [
    (2, 2, 4),
    (2, -5, -3),
    (2, 1, 3),
])
def test_sum(x, y, expected):
    simple = SimpleTests("")

    assert simple.sum(x, y) == expected


@pytest.mark.xfail
def test_divide_by_zero():
    assert 1 / 0 == 1


def test_print(capfd):
    print("hello")

    out, err = capfd.readouterr()

    assert out == "hello\n"
    assert err == ''
