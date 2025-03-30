from questions.question_1.code.wrong.wrong_1_041 import *
def test_001():
    assert search(42, (-5, 1, 3, 5, 7, 10)) == 6

def test_002():
    assert search(42, [1, 5, 10]) == 3

def test_003():
    assert search(5, (1, 5, 10)) == 1

def test_004():
    assert search(7, [1, 5, 10]) == 2

def test_005():
    assert search(3, (1, 5, 10)) == 1

def test_006():
    assert search(-5, (1, 5, 10)) == 0

def test_007():
    assert search(10, (-5, -1, 3, 5, 7, 10)) == 5

def test_008():
    assert search(-100, (-5, -1, 3, 5, 7, 10)) == 0

def test_009():
    assert search(0, (-5, -1, 3, 5, 7, 10)) == 2

def test_010():
    assert search(100, []) == 0

def test_011():
    assert search(-100, ()) == 0

