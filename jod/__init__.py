from otree.api import *



doc = """
One player decides how much of the other player's endowment to destroy.
"""


class Constants(BaseConstants):
    name_in_url = 'jod'
    players_per_group = None
    num_rounds = 1
    endowment = 250
    destruction_strength = 10


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

    jod11 = make_field('Participant A spends 0 points on reducing the earnings of Participant B.')
    jod12 = make_field('Participant A spends 0 points on reducing the earnings of Participant B.')
    jod13 = make_field('Participant A spends 0 points on reducing the earnings of Participant B.')
    jod14 = make_field('Participant A spends 0 points on reducing the earnings of Participant B.')
    jod15 = make_field('Participant A spends 0 points on reducing the earnings of Participant B.')
    jod16 = make_field('Participant A spends 0 points on reducing the earnings of Participant B.')
    jod21 = make_field('Participant A spends 0 points on reducing the earnings of Participant B.')
    jod22 = make_field('Participant A spends 0 points on reducing the earnings of Participant B.')
    jod23 = make_field('Participant A spends 0 points on reducing the earnings of Participant B.')
    jod24 = make_field('Participant A spends 0 points on reducing the earnings of Participant B.')
    jod25 = make_field('Participant A spends 0 points on reducing the earnings of Participant B.')
    jod26 = make_field('Participant A spends 0 points on reducing the earnings of Participant B.')

    ex1 = models.CurrencyField(
        doc="""Answer to first example""",
        min=0,
        max=Constants.endowment,
        label="",
    )
    ex2 = models.CurrencyField(
        doc="""Answer to second example""",
        min=0,
        max=Constants.endowment,
        label="",
    )


# PAGES
class Instructions(Page):
    form_model = 'player'
    form_fields = ['ex1', 'ex2']

    # def vars_for_template(self):
    #     ratio = Constants.endowment/Constants.destruction_strength
    #     return dict(
    #         ratio=ratio,
    #     )

    def error_message(self, value):
        if value["ex1"] != 238:
            return 'The first question is not answered correctly. Consult the instructions and try again.'
        elif value["ex2"] != 130:
            return 'The second question is not answered correctly. Consult the instructions and try again.'


class Elicitation1(Page):
    form_model = 'player'
    form_fields = ['jod11', 'jod12', 'jod13', 'jod14', 'jod15', 'jod16']


class Elicitation2(Page):
    form_model = 'player'
    form_fields = ['jod21', 'jod22', 'jod23', 'jod24', 'jod25', 'jod26']


page_sequence = [Instructions, Elicitation1, Elicitation2]
