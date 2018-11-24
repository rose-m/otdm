from typing import List

from ._builtin import Page, WaitPage
from .config import GAIN_PER_WEEK
from .step import ChoiceStep


class ChoiceListPage(Page):
    form_model = 'player'

    def get_form_fields(self) -> List[str]:
        return [ChoiceStep.get_variable_name(self.player.get_current_choice())]

    def vars_for_template(self):
        # TODO: calculate "ranges" for A and B options

        return {
            'gain': GAIN_PER_WEEK,
            'progress': self.player.get_current_step() / 5 * 100,
            'var_name': ChoiceStep.get_variable_name(self.player.get_current_choice())
        }

    def before_next_page(self):
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
