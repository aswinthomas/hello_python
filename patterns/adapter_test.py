from adapter import Adapter, Korean, British


def test_adapter():
	objects = []
	# Create instance of incompatible classes
	korean = Korean()
	british = British()
	# wrap them in adapter
	korean_adapter = Adapter(korean)
	british_adapter = Adapter(british)

	assert korean_adapter.speak() == 'An-neyong?'
	assert british_adapter.speak() == 'Hello!'
