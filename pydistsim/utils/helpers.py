from collections.abc import Callable, Iterable
from itertools import product
from random import choice, shuffle
from typing import TYPE_CHECKING, Any, TypeVar

from pydistsim.logger import logger

T = TypeVar("T")
U = TypeVar("U")


def pydistsim_equal_objects(obj1, obj2):
    """
    Compare two objects and their attributes, but allow for non immutable
    attributes to be equal up to their class.
    """
    classes = obj1.__class__ == obj2.__class__
    attr_names = attr_values = True
    if isinstance(obj1, object) and isinstance(obj2, object):
        attr_names = set(obj1.__dict__.keys()) == set(obj2.__dict__.keys())
    types = (str, tuple, int, int, bool, float, frozenset, bytes, complex)
    for key, value in list(obj1.__dict__.items()):
        other_value = getattr(obj2, key, None)
        if (isinstance(value, types) and value != other_value) or value.__class__ != other_value.__class__:
            attr_values = False
            break
    return classes and attr_names and attr_values


def with_typehint(baseclass: type[T]) -> type[T]:
    """
    Useful function to make mixins with baseclass typehint without actually inheriting from it.
    """
    if TYPE_CHECKING:
        return baseclass
    return object


def first(iterable: Iterable[T], default: U | None = None) -> T | U | None:
    """
    Return the first item in an iterable, or a default value if the iterable is empty.

    :param iterable: The iterable to get the first item from.
    :type iterable: Iterable[T]
    :param default: The default value to return if the iterable is empty.
    :type default: U | None

    :return: The first item in the iterable, or the default value if the iterable is empty.
    :rtype: T | U | None
    """

    iterator = iter(iterable)
    return next(iterator, default)


def measure_sortedness(sequence: Iterable[T], key: Callable[[T], Any] = None, reverse: bool = False) -> float:
    """
    Measure the sortedness of a sequence. A higher value means the sequence is more sorted.

    `sortedness = 1 - inversions / (n * (n - 1) / 2)`, so if `sortedness == 1` corresponds to a sorted sequence.


    :param sequence: The sequence to measure the sortedness of.
    :type sequence: Iterable[T]
    :param key: The key function to use to extract a comparison key from each element.
    :type key: Callable[[T], Any]
    :param reverse: Whether to sort the sequence in reverse order.
    :type reverse: bool
    :return: The sortedness of the sequence (between 0 and 1) and the inverted pairs found.
    :rtype: tuple[float, list[tuple[int, int]]]
    """

    if len(sequence) <= 1:
        return 1.0, []

    if not key:
        key = lambda x: x

    if reverse:
        key = lambda x: -key(x)

    sortedness = 0
    inverted_pairs = []
    for pair in product(range(len(sequence)), repeat=2):
        i, j = pair
        if i < j and key(sequence[i]) <= key(sequence[j]):
            sortedness += 1
        elif i != j:
            inverted_pairs.append(pair)

    return (sortedness / (len(sequence) * (len(sequence) - 1) / 2), inverted_pairs)


def sort_by_sortedness(
    sequence: Iterable[T], sortedness_threshold, key: Callable[[T], Any] = None, reverse: bool = False
) -> list[T]:
    """
    Sort a sequence by sortedness. A higher value means the sequence is more sorted.

    :param sequence: The sequence to sort by sortedness.
    :type sequence: Iterable[T]
    :param sortedness_threshold: The sortedness threshold to sort the sequence by.
    :type sortedness_threshold: float
    :param key: The key function to use to extract a comparison key from each element.
    :type key: Callable[[T], Any]
    :param reverse: Whether to sort the sequence in reverse order.
    :type reverse: bool
    :return: The sequence sorted by sortedness.
    :rtype: list[T]
    """

    sequence = list(sequence)
    shuffle(sequence)
    measured_sortedness, inverted_pairs = measure_sortedness(sequence, key=key, reverse=reverse)
    while measured_sortedness < sortedness_threshold:
        logger.trace("Shuffling sequence to improve sortedness. Sortedness: %f", measured_sortedness)
        i, j = choice(inverted_pairs)
        sequence[i], sequence[j] = sequence[j], sequence[i]
        measured_sortedness, inverted_pairs = measure_sortedness(sequence, key=key, reverse=reverse)

    return sequence
