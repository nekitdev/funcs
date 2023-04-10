from operator import attrgetter as standard_attribute_getter
from operator import itemgetter as standard_item_getter

__all__ = ("attribute_getter", "item_getter")

attribute_getter = standard_attribute_getter
"""An alias of the standard `attribute_getter` type that implements attribute fetching."""

item_getter = standard_item_getter
"""An alias of the standard `item_getter` type that implements item fetching."""
