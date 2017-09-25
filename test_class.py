class TestClass(object):
	# test will pass
    def test_one(self):
        x = "this"
        assert 'h' in x

	# test will fail
    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')