#!/usr/bin/python3
"""up"""


class MyInt(int):
    """MyInt class, inherits from int."""
    def __eq__(self, other):
        """Overrides == to return the inverse of the standard behavior."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Overrides != to return the inverse of the standard behavior."""
        return super().__eq__(other)
