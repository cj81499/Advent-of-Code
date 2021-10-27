import pytest

import aoc_cj.aoc2016.day14 as d


def test_a():
    assert d.parta("abc") == 22728


def test_key_stretch_hash():
    assert d.key_stretch_hash("abc0") == "a107ff634856bb300138cac6568c0f24"


@pytest.mark.slow
def test_b():
    assert d.partb("abc") == 22551
