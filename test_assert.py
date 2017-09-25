import pytest

def test_function():
	a = 4
	assert a % 2 == 0, "value was odd, should be even"

# function doesn't start with 'test' in name, so not checked	
def other_func():
	b = 5
	assert b % 2 == 0, "value was odd, should be even"

# function gets evaluated to false
def test_2():
	c = 3
	assert c % 2 == 0, "value was odd, should be even"
	