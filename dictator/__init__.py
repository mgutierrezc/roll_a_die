from otree.api import *



doc = """
One player decides how to divide a certain amount between himself and the other
player.
"""


class Constants(BaseConstants):
    name_in_url = 'dictator'
    players_per_group = None
    num_rounds = 1
    #instructions_template = 'dictator/instructions.html'
    # Initial amount allocated to the dictator
    endowment_dictator = 500
    endowment_not_dictator = 0


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    def make_field(label):
        return models.IntegerField(
            choices=[1,2,3,4],
            label=label,
            widget=widgets.RadioSelect,
        )

    dg1 = make_field('Participant A gives 0 points to Participant B and keeps 500 points to themself.')
    dg2 = make_field('Participant A gives 100 points to Participant B and keeps 400 points to themself.')
    dg3 = make_field('Participant A gives 200 points to Participant B and keeps 300 points to themself.')
    dg4 = make_field('Participant A gives 250 points to Participant B and keeps 250 points to themself.')
    dg5 = make_field('Participant A gives 300 points to Participant B and keeps 200 points to themself.')
    dg6 = make_field('Participant A gives 400 points to Participant B and keeps 100 points to themself.')
    dg7 = make_field('Participant A gives 500 points to Participant B and keeps 0 points to themself.')

    ex1 = models.CurrencyField(
        doc="""Answer to first example""",
        min=0,
        max=Constants.endowment_dictator,
        label="",
    )

    ex2 = models.CurrencyField(
        doc="""Answer to second example""",
        min=0,
        max=Constants.endowment_dictator,
        label="",
    )


# PAGES
class Instructions(Page):
    form_model = 'player'
    form_fields = ['ex1', 'ex2']

    def error_message(self, value):
        if value["ex1"] != 375:
            return 'The first question is not answered correctly. Consult the instructions and try again.'
        elif value["ex2"] != 350:
            return 'The second question is not answered correctly. Consult the instructions and try again.'


class Elicitation(Page):
    form_model = 'player'
    form_fields = ['dg1', 'dg2', 'dg3', 'dg4', 'dg5', 'dg6', 'dg7']


page_sequence = [Instructions, Elicitation]
