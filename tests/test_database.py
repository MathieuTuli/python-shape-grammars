import pytest

from python_shape_grammars.database import Database

# TODO FINISH


def test_database():
    # hashable key - a tuple
    d = Database()
    k, v = (1, 2, 3), 'magic'
    d[k] = v
    if d[k] != v:
        pytest.fail()

    # non-hashable key - a list - becomes a many-key shared value
    d = Database()
    keys, value = [1, 2, 3], ['magic']
    d.iterload(keys, value)
    if d[1] != v:
        pytest.fail()
    if d[2] != v:
        pytest.fail()
    if d[3] != v:
        pytest.fail()

    d = Database()
    k, v = ['what', 'ever'], ['test']
    d.iterload(k, v)
    assert d['what'] == d['ever']
    d['what'] = 'testing'
    try:
        assert d['what'] == d['ever']
    except AssertionError:
        assert True
    print("HERE")
    if 'what' not in d:
        pytest.fail()
    if 'ever' not in d:
        pytest.fail()

    d = Database()
    v = 'test'
    keys, values = ['what', 'ever'], [v]
    d.iterload(keys, values)
    d['whatever'] = 'test'
    assert v == d['whatever']
    assert v == d['what']
    assert d['whatever'] == d['what']
    d.update('whatever', 'test', 'new test')
    a, b = d['whatever'], d['what']
    assert a == b

    d = Database()
    try:
        d['test'] = 2
        if d['test'] != 2:
            pytest.fail()
        d['test2'] = 2
        if len(d.keys) != 2:
            pytest.fail()
        if len(d.values) != 1:
            pytest.fail()
        d['test2'] = 3
        # You have to use update to propogate the change in value
        if d['test'] == 3:
            pytest.fail()

    except Exception as e:
        raise e
