from composite import Composite, Child


def test_composite():
	# top level composite menu
	top = Composite("top_menu")
	# build composite submenu
	sub1 = Composite("submenu1")
	sub2 = Child("submenu2")

	top.append_child(sub1)
	top.append_child(sub2)

	# create child submenu
	sub11 = Child("sub_submenu 11")
	sub12 = Child("sub_submenu 12")

	sub1.append_child(sub11)
	sub1.append_child(sub12)

	res = top.component_function()
	assert res == ['top_menu', ['submenu1','sub_submenu 11','sub_submenu 12'],'submenu2']
