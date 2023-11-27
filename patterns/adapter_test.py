from adapter import Adapter, Korean, British


def test_adapter():
	objects = []
	korean = Korean()
	british = British()
	objects.append(Adapter(korean, speak=korean.speak_korean))
	objects.append(Adapter(british, speak=british.speak_english))
	for obj in objects:
		if obj.name == 'Korean':
			assert obj.speak() == 'An-neyong?'
		elif obj.name == 'British':
			assert obj.speak() == 'Hello!'
