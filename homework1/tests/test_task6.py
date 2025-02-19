import context
import task6
import pytest
import os

def get_files():
    # Going up one directory and returning all txt files for testing
    l1 = []
    for filename in os.listdir('./'):
        if filename.endswith(".txt"):
            l1.append(filename)
    
    return l1

files = get_files()
print(files)

@pytest.mark.parametrize("filename", files)
def test_task6_1(filename):
    # Hard coded truths for homework purposes
    expected = {"task6_read_me.txt": 104}
    base_file = os.path.basename(filename)

    word_count = task6.task6_1(filename)

    assert word_count == expected[base_file]

