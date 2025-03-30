from questions.question_4.code.wrong.wrong_4_357 import *
def test_001():
    assert sort_age([("F", 19)]) == [('F', 19)]

def test_002():
    assert sort_age([("M", 35), ("F", 18), ("M", 23), ("F", 19), ("M", 30), ("M", 17)]) == [('M', 35), ('M', 30), ('M', 23), ('F', 19), ('F', 18), ('M', 17)]

def test_003():
    assert sort_age([("F", 18), ("M", 23), ("F", 19), ("M", 30), ("M", 17)]) == [('M', 30), ('M', 23), ('F', 19), ('F', 18), ('M', 17)]

def test_004():
    assert sort_age([("F", 18), ("M", 23), ("F", 19), ("M", 30)]) == [('M', 30), ('M', 23), ('F', 19), ('F', 18)]

def test_005():
    assert sort_age([("M", 23), ("F", 19), ("M", 30)]) == [('M', 30), ('M', 23), ('F', 19)]

def test_006():
    assert sort_age([]) == []

