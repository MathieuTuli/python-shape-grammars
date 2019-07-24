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
    if 'what' not in d:
        pytest.fail()
    if 'ever' not in d:
        pytest.fail()
    if 'everr' in d:
        pytest.fail()

    d = Database()
    v = 'test'
    keys, values = ['what', 'ever'], [v]
    d.iterload(keys, values)
    d['whatever'] = 'test'
    assert v == d['whatever']
    assert v == d['what']
    assert d['whatever'] == d['what']
    if d['what'] != v:
        pytest.fail()
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

    # test removing items
    d = Database()
    d.iterload(['key1', 'key2'], ['test'])
    if d['key1'] != 'test':
        pytest.fail()
    del d['key1']
    if 'key1' in d:
        pytest.fail()
    if 'key2' not in d:
        pytest.fail()
    del d['key2']
    if 'key2' in d:
        pytest.fail()

    # test iterating over database
    d = Database()
    d.iterload(['key1', 'key2'], ['test1'])
    d.iterload(['key3', 'key4'], ['test2'])
    d.iterload(['key5', 'key6'], ['test3'])
    d['key7'] = "test4"
    for k, v in d.items():
        if k == 'key1' or k == 'key2':
            if v != 'test1':
                pytest.fail()
        if k == 'key3' or k == 'key4':
            if v != 'test2':
                pytest.fail()
        if k == 'key5' or k == 'key6':
            if v != 'test3':
                pytest.fail()
        if k == 'key7':
            if v != 'test4':
                pytest.fail()
