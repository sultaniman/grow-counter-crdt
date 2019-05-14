import socket
from core import grow_counter


HOST = socket.gethostname()


def test_counter():
    node1 = {
        "node2": 0,
        "node1": 1
    }

    node2 = {
        "node2": 5,
        "node1": 1
    }

    new_state_node1 = grow_counter._increment(node1, "node1")
    merged_state_node1 = grow_counter.merge(new_state_node1, node2)

    assert merged_state_node1 == {
        "node2": 5,
        "node1": 2
    }

    new_state_node2 = grow_counter._increment(node2, "node2")
    merged_state_node2 = grow_counter.merge(new_state_node2, merged_state_node1)

    assert merged_state_node2 == {
        "node2": 6,
        "node1": 2
    }

    assert grow_counter.value(merged_state_node1) == 7
    assert grow_counter.value(merged_state_node2) == 8
