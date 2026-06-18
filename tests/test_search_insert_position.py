from projects.search_insert_position import search_insert


def test_exact_match():
    assert search_insert([1, 3, 5, 6], 5) == 2


def test_insert_middle():
    assert search_insert([1, 3, 5, 6], 2) == 1


def test_insert_end():
    assert search_insert([1, 3, 5, 6], 7) == 4


def test_insert_beginning():
    assert search_insert([1, 3, 5, 6], 0) == 0


def test_single_element():
    assert search_insert([1], 0) == 0