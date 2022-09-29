from otree.api import *



doc = """
welcome page
"""


class Constants(BaseConstants):
    players_per_group = None
    num_rounds = 1
    name_in_url = 'welcome'
    bonus = 250


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    ex1 = models.CurrencyField(
        doc="""Answer to first example""",
        min=0,
        max=5*Constants.bonus,
        label="",
    )
    ex2 = models.CurrencyField(
        doc="""Answer to second example""",
        min=0,
        max=5*Constants.bonus,
        label="",
    )
    ex3 = models.CurrencyField(
        doc="""Answer to third example""",
        min=0,
        max=5*Constants.bonus,
        label="",
    )


# FUNCTIONS
# PAGES
class Welcome(Page):
    pass


class Instructions(Page):
    def vars_for_template(self):
        return dict(
            participation_fee=self.session.config['participation_fee'],
            currency_per_point=self.session.config['real_world_currency_per_point'],
            country=self.session.config['country'],
        )


class Start(Page):
    pass


class ElicitationIntro(Page):
    pass


class ElicitationInstructions(Page):
    form_model = 'player'
    form_fields = ['ex1', 'ex2', 'ex3']

    def error_message(self, value):
        if value["ex1"] != 0:
            return 'The first question is not answered correctly. Consult the instructions and try again.'
        elif value["ex2"] != 0:
            return 'The second question is not answered correctly. Consult the instructions and try again.'
        elif value["ex3"] != 250:
            return 'The third question is not answered correctly. Consult the instructions and try again.'

    def vars_for_template(self):
        return dict(
            bonus0=0,
            bonus1=Constants.bonus,
            bonus2=2*Constants.bonus,
            bonus3=3*Constants.bonus,
            bonus4=4*Constants.bonus,
            bonus5=5*Constants.bonus,
        )


class StartPartI(Page):
    pass


page_sequence = [Welcome, Instructions, Start, ElicitationIntro, ElicitationInstructions, StartPartI]
