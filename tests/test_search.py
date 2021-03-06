"""Tests of search algorithms."""

import pytest

from algorithms.search.linear_search import linear_search
from algorithms.search.binary_search import binary_search
from algorithms.search.exponential_search import exponential_search


@pytest.mark.parametrize("function", [linear_search, binary_search, exponential_search])
def test_element_is_not_found(function):
    items = [1,2,3,4,5]
    assert(function(items, 6) == -1)


@pytest.mark.parametrize("function", [linear_search, binary_search, exponential_search])
def test_list_is_empty(function):
    assert(function([], 6) == -1)


@pytest.mark.parametrize("function", [linear_search, binary_search, exponential_search])
def test_one_element(function):
    items = [1]
    assert(function(items, 1) == 0)


@pytest.mark.parametrize("function", [linear_search, binary_search, exponential_search])
def test_positive_one(function):
    items = [1,1,2,3,4]
    assert(function(items, 1) == 0)


@pytest.mark.parametrize("function", [linear_search, binary_search, exponential_search])
def test_positive_two(function):
    items = [1,1,2,3,4]
    assert(function(items, 4) == 4)


@pytest.mark.parametrize("function", [linear_search, binary_search, exponential_search])
def test_positive_three(function):
    items = [1,1,2,3,4]
    assert(function(items, 2) == 2)


@pytest.mark.parametrize("function", [linear_search, binary_search, exponential_search])
def test_positive_four(function):
    items = [1,2,3,4,5,6,7,8,9,10,11] 
    assert(function(items, 6) == 5)


@pytest.mark.parametrize("function", [linear_search, binary_search, exponential_search])
def test_positive_four(function):
    items = [0,1,1,1,1,1,1,1,1]
    assert(function(items, 0) == 0)
