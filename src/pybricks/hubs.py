# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2020 The Pybricks Authors

"""LEGO® Programmable Hubs."""
from ._common import (
    Speaker,
    Battery,
    ColorLight,
    Keypad,
    LightMatrix,
    IMU,
    Charger,
    System,
    SimpleAccelerometer,
)
from .ev3dev._speaker import Speaker as EV3Speaker
from .geometry import Axis
from .media.ev3dev import Image
from .parameters import Button


class EV3Brick:
    """LEGO® MINDSTORMS® EV3 Brick."""

    # These class attributes are here for auto-documentation only.
    # In reality, they are instance attributes created by __init__.
    buttons = Keypad(
        (
            Button.LEFT,
            Button.RIGHT,
            Button.CENTER,
            Button.UP,
            Button.DOWN,
        )
    )
    screen = Image("_screen_")
    speaker = EV3Speaker()
    battery = Battery()
    light = ColorLight()


class MoveHub:
    """LEGO® BOOST Move Hub."""

    # These class attributes are here for auto-documentation only.
    # In reality, they are instance attributes created by __init__.
    battery = Battery()
    light = ColorLight()
    imu = SimpleAccelerometer()
    system = System()
    button = Keypad((Button.CENTER,))


class CityHub:
    """LEGO® City Hub."""

    # These class attributes are here for auto-documentation only.
    # In reality, they are instance attributes created by __init__.
    battery = Battery()
    light = ColorLight()
    system = System()
    button = Keypad((Button.CENTER,))


class TechnicHub:
    """LEGO® Technic Hub."""

    # These class attributes are here for auto-documentation only.
    # In reality, they are instance attributes created by __init__.
    battery = Battery()
    light = ColorLight()
    imu = IMU()
    system = System()
    button = Keypad((Button.CENTER,))

    def __init__(self, top_side: Axis = Axis.Z, front_side: Axis = Axis.X):
        """TechnicHub(top_side=Axis.Z, front_side=Axis.X)

        Initializes the hub. Optionally, specify how the hub is
        :ref:`placed in your design <robotframe>` by saying in which
        direction the top side (with the button) and front side
        (with the light) are pointing.

        Arguments:
            top_side (Axis): The axis that passes through the *top side* of
                the hub.
            front_side (Axis): The axis that passes through the *front side* of
                the hub.
        """
        pass


class PrimeHub:
    """LEGO® SPIKE Prime Hub or LEGO® MINDSTORMS Inventor Hub."""

    # These class attributes are here for auto-documentation only.
    # In reality, they are instance attributes created by __init__.
    battery = Battery()
    buttons = Keypad(
        (
            Button.LEFT,
            Button.RIGHT,
            Button.CENTER,
            Button.BLUETOOTH,
        )
    )
    charger = Charger()
    light = ColorLight()
    display = LightMatrix(5, 5)
    speaker = Speaker()
    imu = IMU()
    system = System()

    def __init__(self, top_side: Axis = Axis.Z, front_side: Axis = Axis.X):
        """PrimeHub(top_side=Axis.Z, front_side=Axis.X)

        Initializes the hub. Optionally, specify how the hub is
        :ref:`placed in your design <robotframe>` by saying in which
        direction the top side (with the buttons) and front side (with the USB
        port) are pointing.

        Arguments:
            top_side (Axis): The axis that passes through the *top side* of
                the hub.
            front_side (Axis): The axis that passes through the *front side* of
                the hub.
        """
        pass


class InventorHub(PrimeHub):
    """LEGO® MINDSTORMS Inventor Hub."""

    pass
