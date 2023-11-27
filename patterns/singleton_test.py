from singleton import Singleton


def test_singleton():
	x = Singleton(HTTP="Hyper Text Transfer Protocol")
	assert str(x) == str({'HTTP': 'Hyper Text Transfer Protocol'})
	y = Singleton(SNMP="Simple Network Management Protocol")
	assert str(x) == str({'HTTP': 'Hyper Text Transfer Protocol',
	                      'SNMP': 'Simple Network Management Protocol'})
	assert str(y) == str({'HTTP': 'Hyper Text Transfer Protocol',
	                      'SNMP': 'Simple Network Management Protocol'})
