from src.math_operations import mul,add
def test_mul():
    assert mul(2,3)==6
    assert mul(4,3)==12
def test_add():
    assert add(2,3)==5
    assert add(4,3)==7
    assert add(6,3)==9
    assert add(2,6)==8