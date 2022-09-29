from otree.api import Currency as c, currency_range

from ._builtin import Page


class Instructions(Page):
    form_model = 'player'
    form_fields = ['ex1', 'ex2']

    def error_message(self, value):
        if value["ex1"] != 400:
            return 'The first question is not answered correctly. Consult the instructions and try again.'
        elif value["ex2"] != 350:
            return 'The second question is not answered correctly. Consult the instructions and try again.'


# class StartRule(Page):
#     pass


class Rules(Page):
    form_model = 'player'
    form_fields = ['balls_A', 'balls_B', 'balls_I']


page_sequence = [Instructions, Rules]
