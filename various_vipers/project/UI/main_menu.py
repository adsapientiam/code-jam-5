"""
Main Menu page.

Handling input and creating new events.
"""

import pygame as pg

from project.UI.button import generate_buttons
from project.constants import Button, Color


class MainMenu:
    """Represents Main Menu page."""

    def __init__(self, screen: pg.Surface):
        """Set initial main menu values."""
        self.screen = screen

        self.play_btn, self.opt_btn, self.quit_btn = generate_buttons(
            btn_w=Button.main_btn_w,
            btn_h=Button.main_btn_h,
            btn_count=3,
            gap=Button.btn_gap,
        )

    def handle_events(self, mouse_x: int, mause_y: int, mouse_click: bool):
        """Hadle all main menu events."""
        pass

    def draw(self,):
        """Draw all main menu elements."""
        pg.draw.rect(self.screen, Color.white, self.play_btn.rect)
        pg.draw.rect(self.screen, Color.white, self.opt_btn.rect)
        pg.draw.rect(self.screen, Color.white, self.quit_btn.rect)
