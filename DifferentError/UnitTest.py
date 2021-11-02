import Error as e

def test_output():
    assert e.get_tweets('@wwenbinbu') == '"I am so sad."'

def test_notfound():
    assert e.notFound_error('@wobuzdfayiluan') == "NotFound"

if __name__ == 'TestAdding':
    test_output()
    test_notfound()
