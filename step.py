from enum import Enum


class ChoiceStep(Enum):
    C_12 = 1
    C_14 = 2
    C_34 = 3
    C_18 = 4
    C_78 = 5

    @staticmethod
    def get_variable_name(step: 'ChoiceStep') -> str:
        if step is ChoiceStep.C_12:
            return 'c12'
        elif step is ChoiceStep.C_14:
            return 'c14'
        elif step is ChoiceStep.C_34:
            return 'c34'
        elif step is ChoiceStep.C_18:
            return 'c18'
        elif step is ChoiceStep.C_78:
            return 'c78'
        else:
            raise ValueError('invalid step: %s' % step)
