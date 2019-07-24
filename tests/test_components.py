import pytest

from python_shape_grammars.components import EdgeDirection


def fail_if(boolean):
    if boolean:
        pytest.fail()


def test_edge_direction():
    N = EdgeDirection('N')
    NE = EdgeDirection('NE')
    E = EdgeDirection('E')
    SE = EdgeDirection('SE')
    S = EdgeDirection('S')
    SW = EdgeDirection('SW')
    W = EdgeDirection('W')
    NW = EdgeDirection('NW')

    fail_if(N.value != 'N')
    fail_if(N.integer_value != 0)
    fail_if(NE.value != 'NE')
    fail_if(NE.integer_value != 1)
    fail_if(E.value != 'E')
    fail_if(E.integer_value != 2)
    fail_if(SE.value != 'SE')
    fail_if(SE.integer_value != 3)
    fail_if(S.value != 'S')
    fail_if(S.integer_value != 4)
    fail_if(SW.value != 'SW')
    fail_if(SW.integer_value != 5)
    fail_if(W.value != 'W')
    fail_if(W.integer_value != 6)
    fail_if(NW.value != 'NW')
    fail_if(NW.integer_value != 7)

    fail_if(N.reverse() != EdgeDirection('S'))
    fail_if(NE.reverse() != EdgeDirection('SW'))
    fail_if(E.reverse() != EdgeDirection('W'))
    fail_if(SE.reverse() != EdgeDirection('NW'))
    fail_if(S.reverse() != EdgeDirection('N'))
    fail_if(SW.reverse() != EdgeDirection('NE'))
    fail_if(W.reverse() != EdgeDirection('E'))
    fail_if(NW.reverse() != EdgeDirection('SE'))
