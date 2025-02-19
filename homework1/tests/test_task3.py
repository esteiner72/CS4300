import context
import task3

def test_task3_1():
    # Set test case n below, check if n is even or odd to expect what to get from task3.py
    n_test = 2
    if n_test % 2 == 0:
        assert task3.task3_1(n_test) == "n is even"
    elif n_test % 2 == 1:
        assert task3.task3_1(n_test) == "n is odd"
    else:
        assert task3.task3_1(n_test) == "n is 0"

def test_task3_2():
    ten_prime = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29}
    assert ten_prime.issubset(task3.task3_2()) == True

def test_task3_3():
    assert task3.task3_3() == sum(range(1, 101))