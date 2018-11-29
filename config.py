"""
This file includes all available configuration options for the otdm app.

Modify this file to set all your preferences - also modify `templates/otdm/Results.html` to your liking
which will be displayed after all questions of all blocks have been answered.

It's not recommended to edit any of the other files.
"""

from .payoffType import PayoffType

#: The total number of weeks
NUM_WEEKS = 52

#: The gain to be paid out per week
GAIN_PER_WEEK = 20

#: The payoff type - whether a random player of the session should be payed
#   or all players (ALL_PLAYERS). Payoff will be chosen as a random choice.
#   Only players with fully valid selections can be payed off.
#   When set to `None` no payoff for players according to their choices will be calculated
PAYOFF_TYPE = PayoffType.RANDOM_PLAYER

#: The fixed choice round that the payoff should be selected from
#   The first round is the elicitation of c12, the last round the one of c78
#   If set to `None` then a random round will be chosen
PAYOFF_CHOICE_ROUND = None
