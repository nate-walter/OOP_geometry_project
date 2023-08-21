from shapes import Rectangle, Circle, Triangle

def test_shapes():
    r = Rectangle(10, 5)
    c = Circle(7)
    t = Triangle(6, 8)

    assert r.area() == 50
    assert c.area() == 153.93804002589985
    assert t.area() == 24

test_shapes()
print("All tests passed! These figures are in shape")