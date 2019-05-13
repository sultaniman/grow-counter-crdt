"""
Implements Grow Only counter each action which
requires state updates completely new updated
state is returned thus avoiding mutations.
https://en.wikipedia.org/wiki/Conflict-free_replicated_data_type#G-Counter_(Grow-only_Counter)
"""

import socket

from typing import Dict
from functools import partial


HOST = socket.gethostname()


def new() -> dict:
    """Instantiate new counter"""
    return {
        HOST: 0
    }


def merge(state: Dict, new_state: Dict) -> Dict:
    """
    Merges states from different nodes

        let ∀i ∈ [0,n − 1] : Z.P[i] = max(X.P[i],Y.P[i])

    :param state: current state for all node counters in current node
    :param new_state: new incoming state for from other nodes
    :return: new state which represents updated counters
    """
    # To accept new nodes we need to have a union of all nodes
    keys = state.keys() | new_state.keys()

    return {
        key: max(state.get(key, 0), new_state.get(key, 0))
        for key in keys
    }


def value(state: Dict) -> int:
    """
    Returns total view count for all nodes
    :param state: current state for this node
    :return: total view count
    """
    return sum(state.values())


def _increment(state: Dict, host: str = None) -> Dict:
    """
    Increment counter for current host

        let g = myId()
        P[g] := P[g] + 1

    :param state: current node state
    :param host: current host
    :return: updated state
    """
    return {
        **state,
        host: state[host] + 1
    }


increment = partial(_increment, host=HOST)
