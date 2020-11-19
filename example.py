def add(a,b):
    a_temp = a
    b_temp = b
    b = a_temp
    a = b_temp
    return b+a

def test_add():
    assert add(2,3)==5
    assert add('space','ship')=='spaceship'
    assert add(0,0)==0
