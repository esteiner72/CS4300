import context
import task4
import pytest

def test_task4_1():
    # Test that task4 accepts ducktyping, but still only allows numerical data types
    with pytest.raises(TypeError):
        task4.calculate_discount(20, "50%")
    
    with pytest.raises(TypeError):
        task4.calculate_discount("20", 50)

    with pytest.raises(ValueError):
        task4.calculate_discount(1000, -100)

# Testing different int/float values

def test_task4_2():
    assert task4.calculate_discount(100, 50) == 50

def test_task4_3():
    assert task4.calculate_discount(1000.00, 10) == 900