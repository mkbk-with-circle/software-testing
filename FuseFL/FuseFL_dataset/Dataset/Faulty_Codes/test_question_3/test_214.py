from questions.question_3.code.wrong.wrong_3_214 import *
def test_001():
    assert remove_extras([1, 1, 1, 2, 3]) == [1, 2, 3]

def test_002():
    assert remove_extras([1, 5, 1, 1, 3, 2]) == [1, 5, 3, 2]

def test_003():
    assert remove_extras([]) == []

def test_004():
    assert remove_extras([3, 4, 5, 1, 3]) == [3, 4, 5, 1]

def test_005():
    assert remove_extras([3, 4, 5, 1, 3]) == [3, 4, 5, 1]

def test_006():
    assert remove_extras([3, 4, 5, 1, 3]) == [3, 4, 5, 1]

