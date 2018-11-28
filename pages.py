from math import floor

from typing import List

from ._builtin import Page, WaitPage
from .choices import ChoiceManager
from .config import GAIN_PER_WEEK, NUM_WEEKS


class ChoiceListPage(Page):
    form_model = 'player'

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        return [manager.get_step().get_field()]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)

        week_range = manager.get_week_range()
        week_start = week_range[0]
        week_end = week_range[-1]

        option_a_weeks = week_range[:]
        option_a_weeks.insert(0, week_start)
        option_a_gain_count = [i - week_start + 1 for i in option_a_weeks]

        option_b_weeks = week_range[:]
        option_b_weeks.append(week_end)
        option_b_gain_count = [week_end - i + 1 for i in option_b_weeks]

        week_gain = zip(option_a_weeks, option_a_gain_count,
                        option_b_weeks, option_b_gain_count)

        return {
            'gain': GAIN_PER_WEEK,
            'progress': self.player.get_current_step() / 5 * 100,
            'var_name': manager.get_step().get_field(),

            'week_start': week_start,
            'week_end': week_end,

            'week_gain': week_gain
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        # we fix the computed value as the client gives us the lower bound
        # of the switch
        field_name = manager.get_step().get_field()
        switch_lower_bound = getattr(self.player, field_name)
        if switch_lower_bound > 1:
            if switch_lower_bound < floor(NUM_WEEKS / 2.0):
                # values that are below half of the time frame get the "upper bound"
                switch_lower_bound = switch_lower_bound + 1
            else:
                # values that are above half of the time frame get the "lower bound"
                pass
        setattr(self.player, field_name, switch_lower_bound)

        self.player.goto_next_step()


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    ChoiceListPage,  # elicit c12
    ChoiceListPage,  # elicit c14
    ChoiceListPage,  # elicit c34
    ChoiceListPage,  # elicit c18
    ChoiceListPage,  # elicit c78
    ResultsWaitPage,
    Results
]
