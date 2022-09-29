from otree.api import *

import random

doc = """
Risk task
"""


class Constants(BaseConstants):
    players_per_group = None
    num_rounds = 1
    name_in_url = 'risk'
    endowment = 200
    multiplier = float(2.5)  # multiplier for the asset, in case successful
    prob = float(0.5)  # success probability


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    ex1 = models.CurrencyField(
        doc="""Answer to first example""",
        min=0,
        max=Constants.multiplier*Constants.endowment,
        label="",
    )
    ex2 = models.CurrencyField(
        doc="""Answer to second example""",
        min=0,
        max=Constants.multiplier*Constants.endowment,
        label="",
    )

    # ex3 = models.CurrencyField(
    #     doc="""Answer to third example""",
    #     min=0,
    #     max=Constants.multiplier*Constants.endowment,
    #     label="",
    # )
    # ex4 = models.CurrencyField(
    #     doc="""Answer to fourth example""",
    #     min=0,
    #     max=Constants.multiplier*Constants.endowment,
    #     label="",
    # )

    invested = models.IntegerField(
        min=0, max=Constants.endowment, label="How much do you want to invest in the asset?",
        doc="""Invested"""
    )
    not_invested = models.CurrencyField(min=0, max=Constants.endowment,
                                   doc="""Not invested""")

    success = models.BooleanField()

    # Set payoffs assigns the rewards for each round.
    def set_payoffs_risk(self, player):
        self.not_invested = Constants.endowment - cu(self.invested)
        draw_invest = random.random()
        print('The random draw for the success of investment in round', self.round_number, 'is', draw_invest)
        if draw_invest < Constants.p_success_risk:
            self.payoff = Constants.multiplier * c(self.invested) + c(self.not_invested)
            self.success = 1
        else:
            self.payoff = cu(self.not_invested)
            self.success = 0
        print('The payoff in round', self.round_number, 'is', self.payoff)

    def set_results_risk(self, player):
        player.participant.vars['payoff_risk'] = player.payoff
        print('Overall score for risk and player', player.id_in_subsession, 'was', player.participant.vars['payoff_risk'])


# PAGES
class Instructions(Page):
    form_model = 'player'
    form_fields = ['ex1', 'ex2']

    def error_message(self, value):
        if value["ex1"] != 380:
            return 'The first question is not answered correctly. Consult the instructions and try again.'
        elif value["ex2"] != 80:
            return 'The second question is not answered correctly. Consult the instructions and try again.'
        # elif value["ex3"] != 260:
        #     return 'The third question is not answered correctly. Consult the instructions and try again.'
        # elif value["ex4"] != 160:
        #     return 'The fourth question is not answered correctly. Consult the instructions and try again.'


class RiskInvestment(Page):
    form_model = 'player'
    form_fields = ['invested']


page_sequence = [Instructions, RiskInvestment]

