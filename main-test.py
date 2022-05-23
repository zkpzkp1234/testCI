from main import add

def test_add():
    assert add(2, 3) == 5
    print("add function works correctly")

if __name__=='__main__':
    test_add()