import random
from otree.api import (
    BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    models
)

from .config import PAYOFF_TYPE
from .payoffType import PayoffType

author = 'Michael Rose <michael_rose@gmx.de>'

doc = """
otdm provides an easy way of creating experiments to measure the temporal discounting of money
using the Direct Method (DM) [Attema et al., 2016]
"""


class Constants(BaseConstants):
    name_in_url = 'otdm'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):

    def creating_session(self):
        players = self.get_players()
        if PAYOFF_TYPE == PayoffType.RANDOM_PLAYER and len(players) > 0:
            chosen = random.randint(0, len(players) - 1)
            players[chosen].is_selected_for_payoff = True


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    current_step = models.IntegerField(initial=1)
    """Current step the player is in
    
    Equals the elicitation round, i.e. ranges from 1 (for c12) to 5 (c78).
    """

    c12 = models.IntegerField(initial=-1)
    """Represents the measured value of c_(1/2)"""

    c14 = models.IntegerField(initial=-1)
    """Represents the measured value of c_(1/4)"""

    c34 = models.IntegerField(initial=-1)
    """Represents the measured value of c_(3/4)"""

    c18 = models.IntegerField(initial=-1)
    """Represents the measured value of c_(1/8)"""

    c78 = models.IntegerField(initial=-1)
    """Represents the measured value of c_(7/8)"""

    is_selected_for_payoff = models.BooleanField(initial=(PAYOFF_TYPE == PayoffType.ALL_PLAYERS))
    """Indicates whether this player was chosen for payoff"""

    def goto_next_step(self) -> None:
        self.current_step = self.current_step + 1

    def cancel_game(self) -> None:
        self.current_step = -1

    def get_current_step(self) -> int:
        return self.current_step
