"""
File: tools.py
Author: Rodrigo Álvarez
Email: rodrigo.alvare.herrera@gmail.com
"""
import typing
from typing import Any, Sequence

T = typing.TypeVar('T')


def getLastItem(seq: Sequence[T]) -> T | None:
    """
    Returns the last item from some sequence.
    """
    return seq[-1] if len(seq) > 0 else None


def getFirstItem(seq: Sequence[T]) -> T | None:
    """
    Returns the first item from some sequence.
    """
    return seq[0] if len(seq) > 0 else None


def isAList(obj: Any) -> bool:
    return isinstance(obj, list)


def isATuple(obj: Any) -> bool:
    return isinstance(obj, tuple)


def isASet(obj: Any) -> bool:
    return isinstance(obj, set)


def isAFrozenSet(obj: Any) -> bool:
    return isinstance(obj, frozenset)
