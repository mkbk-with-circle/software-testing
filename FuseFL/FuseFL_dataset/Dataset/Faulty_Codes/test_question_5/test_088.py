from questions.question_5.code.wrong.wrong_5_088 import *
def test_001():
    assert top_k([9, 9, 4, 9, 7, 9, 3, 1, 6], 5) == [9, 9, 9, 9, 7]

def test_002():
    assert top_k([9, 8, 4, 5, 7, 2, 3, 1, 6], 5) == [9, 8, 7, 6, 5]

def test_003():
    assert top_k([4, 5, 2, 3, 1, 6], 6) == [6, 5, 4, 3, 2, 1]

def test_004():
    assert top_k([4, 5, 2, 3, 1, 6], 3) == [6, 5, 4]

def test_005():
    assert top_k([4, 5, 2, 3, 1, 6], 0) == []

