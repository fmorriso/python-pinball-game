# import screen size utility module that helps us scale the game based on screen size
import sys
import pathlib
import pyautogui


class GuiSettings:
    """A class to store all settings for Pinball game."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings

        # calculate game size as a percentage of device screen size
        device_width, device_height = pyautogui.size()
        self.screenPct: float = float(0.5)

        game_width: int = int((device_width * self.screenPct // 100) * 100)
        game_height: int = int((device_height * self.screenPct // 100) * 100)

        self.scaleFactor = device_width / device_height + self.screenPct
        # print(f'scale factor = {self.scaleFactor}')
        self.screen_width = game_width
        self.screen_height = game_height