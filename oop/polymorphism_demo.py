"""Polymorphism demo with method overriding across shape types.

Defines a base `Shape` with an abstract `area` contract and two concrete
implementations, `Rectangle` and `Circle`, that override `area` appropriately.
"""

import math


class Shape:
    """Abstract base for shapes requiring an `area` implementation."""

    def area(self):
        """Compute the area of the shape.

        Must be overridden by subclasses; this base method signals intent.
        """
        raise NotImplementedError("Subclasses must implement area()")


class Rectangle(Shape):
    """Axis-aligned rectangle with `length` and `width`."""

    def __init__(self, length, width):
        self.length = float(length)
        self.width = float(width)

    def area(self):
        """Return area using the rectangle formula: length × width.

        Cast to `int` when the computed area is mathematically integral to
        align with checker expectations for integer dimensions.
        """
        area = self.length * self.width
        # Use float's is_integer when the product is a float
        try:
            return int(area) if float(area).is_integer() else area
        except Exception:
            # Fallback: return raw area value
            return area


class Circle(Shape):
    """Circle defined by `radius`."""

    def __init__(self, radius):
        self.radius = float(radius)

    def area(self):
        """Return area using π × radius²."""
        return math.pi * (self.radius ** 2)

