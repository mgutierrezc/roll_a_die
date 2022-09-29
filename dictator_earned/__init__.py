from otree.api import *



doc = """
One player decides how to divide a certain amount between himself and the other
player.
"""


class Constants(BaseConstants):
    name_in_url = 'dictator_earned'
    players_per_group = None
    num_rounds = 1
    #instructions_template = 'dictator/instructions.html'
    # Initial amount allocated to the dictator
    endowment_dictator = 600


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

    dg1a = make_field('Participant A gives 0 points to Participant B and keeps 600 points to themself.')
    dg2a = make_field('Participant A gives 200 points to Participant B and keeps 400 points to themself.')
    dg3a = make_field('Participant A gives 300 points to Participant B and keeps 300 points to themself.')
    dg4a = make_field('Participant A gives 400 points to Participant B and keeps 200 points to themself.')
    dg5a = make_field('Participant A gives 600 points to Participant B and keeps 0 points to themself.')
    dg1b = make_field('Participant A gives 0 points to Participant B and keeps 600 points to themself.')
    dg2b = make_field('Participant A gives 200 points to Participant B and keeps 400 points to themself.')
    dg3b = make_field('Participant A gives 300 points to Participant B and keeps 300 points to themself.')
    dg4b = make_field('Participant A gives 400 points to Participant B and keeps 200 points to themself.')
    dg5b = make_field('Participant A gives 600 points to Participant B and keeps 0 points to themself.')

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

    t1 = models.IntegerField(label='')
    t2 = models.IntegerField(label='')
    t3 = models.IntegerField(label='')


# PAGES
class InstructionsCounting(Page):
    pass


class Table1(Page):
    form_model = 'player'
    form_fields = ['t1']

    def error_message(self, value):
        if value["t1"] != 14:
            return 'Please try again.'


class Table2(Page):
    form_model = 'player'
    form_fields = ['t2']

    def error_message(self, value):
        if value["t2"] != 8:
            return 'Please try again.'


class Table3(Page):
    form_model = 'player'
    form_fields = ['t3']

    def error_message(self, value):
        if value["t3"] != 11:
            return 'Please try again.'


class Instructions(Page):
    form_model = 'player'
    form_fields = ['ex1', 'ex2']

    def error_message(self, value):
        if value["ex1"] != 200:
            return 'The first question is not answered correctly. Consult the instructions and try again.'
        elif value["ex2"] != 400:
            return 'The second question is not answered correctly. Consult the instructions and try again.'


class Elicitation(Page):
    form_model = 'player'
    form_fields = ['dg1a', 'dg2a', 'dg3a', 'dg4a', 'dg5a', 'dg1b', 'dg2b', 'dg3b', 'dg4b', 'dg5b']

    # @staticmethod
    # def vars_for_template(player: Player):
    #
    #     a_fields = ['dg1a', 'dg2a', 'dg3a', 'dg4a', 'dg5a']
    #     b_fields = ['dg1b', 'dg2b', 'dg3b', 'dg4b', 'dg5b']
    #
    #     return dict(a_fields=a_fields, b_fields=b_fields)


page_sequence = [InstructionsCounting, Table1, Instructions, Elicitation]
