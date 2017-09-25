import pytest
def f():
    raise SystemExit(1)

# test will check that SytemExit works and pass
def test_mytest():
    with pytest.raises(SystemExit):
        f()