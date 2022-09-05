.. pybricks-requirements::

Color
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. autoclass:: pybricks.parameters.Color
    :no-members:

    .. rubric:: Saturated colors

    These colors have maximum saturation and brightness value.
    They differ only in hue.

    .. autoattribute:: RED

        .. pybricks-color:: RED

    .. autoattribute:: ORANGE

        .. pybricks-color:: ORANGE

    .. autoattribute:: YELLOW

        .. pybricks-color:: YELLOW

    .. autoattribute:: GREEN

        .. pybricks-color:: GREEN

    .. autoattribute:: CYAN

        .. pybricks-color:: CYAN

    .. autoattribute:: BLUE

        .. pybricks-color:: BLUE

    .. autoattribute:: VIOLET

        .. pybricks-color:: VIOLET

    .. autoattribute:: MAGENTA

        .. pybricks-color:: MAGENTA

    .. rubric:: Unsaturated colors

    These colors have zero hue and saturation. They differ only in brightness
    value.

    When detecting these colors using sensors, their values depend a lot
    on the distance to the object. If the distance between the sensor and the
    object is not constant in your robot, it is better to use only one of these
    colors in your programs.

    .. autoattribute:: WHITE

        .. pybricks-color:: WHITE

    .. autoattribute:: GRAY

        .. pybricks-color:: GRAY

    .. autoattribute:: BLACK

        This represents dark objects that still reflect
        a very small amount of light.

        .. pybricks-color:: BLACK

    .. autoattribute:: NONE

        This is total darkness, with no reflection or light at all.

        .. pybricks-color:: NONE
    
    .. rubric:: Brick colors
    
    These represent common LEGO colors. With the exception of ``BRICK_BLACK``,
    they are returned by the color sensors' ``color()`` functions.
    
    They have been calibrated at a distance of 2 LEGO plates (6.4 mm).
    Measuring from further away makes the color appear darker to the sensor.

    .. autoattribute:: BRICK_YELLOW

        .. pybricks-color:: BRICK_YELLOW
    
    .. autoattribute:: BRICK_RED

        .. pybricks-color:: BRICK_RED
    
    .. autoattribute:: BRICK_BLUE

        .. pybricks-color:: BRICK_BLUE
    
    .. autoattribute:: BRICK_GREEN

        .. pybricks-color:: BRICK_GREEN
    
    .. autoattribute:: BRICK_BLACK

        .. pybricks-color:: BRICK_BLACK
    
    .. autoattribute:: BRICK_WHITE

        .. pybricks-color:: BRICK_WHITE

.. rubric:: Making your own colors

This example shows the basics of color properties, and how to define new colors.

.. literalinclude::
    ../../../examples/pup/parameters/color_basics.py

This example shows more advanced use cases of the ``Color`` class.

.. literalinclude::
    ../../../examples/pup/parameters/color_advanced.py
