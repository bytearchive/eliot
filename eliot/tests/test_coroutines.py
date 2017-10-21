"""
Tests for coroutines, for Python versions that support them.
"""

import sys
if sys.version_info[:2] >= (3, 6):
    from .corotests import CoroutineTests


__all__ = ["CoroutineTests"]
