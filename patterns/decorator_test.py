from decorator import make_blink


def hello_world1():
	return "Hello, World!"


@make_blink
def hello_world2():
	return "Hello, World!"


def test_decorator():
	assert hello_world1() == "Hello, World!"
	assert hello_world2() == "<blink>Hello, World!</blink>"
