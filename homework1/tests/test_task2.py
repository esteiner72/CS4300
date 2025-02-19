import context
import task2

def test_task2():
    # Iterate through task2 return to see if it contains all the data types in our test case
    pass_case = False
    types = {int, float, str, bool, list, dict}
    task2_types = {type(value) for value in task2.task2_main()}

    if types.issubset(task2_types):
        pass_case = True

    assert pass_case == True