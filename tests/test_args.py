# -*- coding: utf-8 -*-

import os
import pytest

from func_args.args import NOTHING, resolve_kwargs


def test_resolve_kwargs():
    kwargs = resolve_kwargs(arg1=NOTHING, arg2=NOTHING)
    assert kwargs == {}

    kwargs = resolve_kwargs(arg1=1, arg2=NOTHING)
    assert kwargs == {"arg1": 1}

    kwargs = resolve_kwargs(arg1=NOTHING, arg2=2)
    assert kwargs == {"arg2": 2}

    kwargs = resolve_kwargs(_mapper={"arg1": "kwarg1"}, arg1=1)
    assert kwargs == {"kwarg1": 1}


if __name__ == "__main__":
    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
