from questions.question_2.code.wrong.wrong_2_244 import *
from questions.question_2.code.global_tuple import *
def test_001():
    assert unique_day("1", (("January","1"),("February","1"))) == False

def test_002():
    assert unique_month("January", (("January","1"),("January","2"))) == False

def test_003():
    assert unique_month("January", (("January","1"),("February","1"))) == True

def test_004():
    assert contains_unique_day("January", (("January","1"),("January","2"))) == True

def test_005():
    assert contains_unique_day("January", (("January","1"),("February","1"))) == False

def test_006():
    assert contains_unique_day("February", (("January","10"),("February","1"),("February","10"))) == True

def test_007():
    assert unique_day("3", (("January","1"),("January","2"))) == False

def test_008():
    assert unique_month("March", (("January","1"),("February","1"))) == False

def test_009():
    assert unique_day("1", (("January","1"),("January","2"))) == True

def test_010():
    assert unique_day("16", tuple_of_possible_birthdays) == False

def test_011():
    assert unique_day("17", tuple_of_possible_birthdays) == False

def test_012():
    assert unique_day("18", tuple_of_possible_birthdays) == True

def test_013():
    assert unique_day("19", tuple_of_possible_birthdays) == True

def test_014():
    assert unique_month("May", tuple_of_possible_birthdays) == False

def test_015():
    assert unique_month("June", tuple_of_possible_birthdays) == False

def test_016():
    assert contains_unique_day("June", tuple_of_possible_birthdays) == True

def test_017():
    assert contains_unique_day("July", tuple_of_possible_birthdays) == False

