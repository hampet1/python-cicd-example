from app import index, home

# testing what returns index function
def test_index():
    assert index() == "hello, world!"

def test_home():
    assert home() == "home directory"
