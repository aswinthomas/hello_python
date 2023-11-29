from proxy import Proxy


def test_proxy():
	# instantiate a proxy
	p = Proxy()
	# make the proxyL artist produce until producer is available
	assert p.produce() is True
	# change state to occupied
	p.occupied = 'Yes'
	assert p.produce() is False
