from otree.api import *



doc = """
One player decides whether to give to or take from the other player.
"""


class Constants(BaseConstants):
    name_in_url = 'dictator_take'
    players_per_group = None
    num_rounds = 1
    #instructions_template = 'dictator/instructions.html'
    # Initial amount allocated to the dictator
    endowment = 250


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

    dg1 = make_field('Participant A takes 250 points from Participant B.')
    dg2 = make_field('Participant A takes 150 points from Participant B.')
    dg3 = make_field('Participant A takes 50 points from Participant B.')
    dg4 = make_field('Participant A does not give or take any points.')
    dg5 = make_field('Participant A gives 50 points to Participant B.')
    dg6 = make_field('Participant A gives 150 points to Participant B.')
    dg7 = make_field('Participant A gives 250 points to Participant B.')

    ex1 = models.CurrencyField(
        doc="""Answer to first example""",
        min=0,
        max=2*Constants.endowment,
        label="",
    )

    ex2 = models.CurrencyField(
        doc="""Answer to second example""",
        min=0,
        max=2*Constants.endowment,
        label="",
    )


# PAGES
class Instructions(Page):
    form_model = 'player'
    form_fields = ['ex1', 'ex2']

    def error_message(self, value):
        if value["ex1"] != 100:
            return 'The first question is not answered correctly. Consult the instructions and try again.'
        elif value["ex2"] != 200:
            return 'The second question is not answered correctly. Consult the instructions and try again.'


class Elicitation(Page):
    form_model = 'player'
    form_fields = ['dg1', 'dg2', 'dg3', 'dg4', 'dg5', 'dg6', 'dg7']


page_sequence = [Instructions, Elicitation]
