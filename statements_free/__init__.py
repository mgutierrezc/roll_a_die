from otree.api import *

doc = """
Read quiz questions from a CSV (simple version).
See also the 'complex' version of this app. 
"""


def read_csv():
    import csv
    import random

    f = open(__name__ + '/stimuli.csv', encoding='utf-8-sig')
    rows = list(csv.DictReader(f))
    random.shuffle(rows)
    return rows


class Constants(BaseConstants):
    name_in_url = 'statements_free'
    players_per_group = None
    QUESTIONS = read_csv()
    num_rounds = len(QUESTIONS)
    section1_endowment = 750


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    current_question = Constants.QUESTIONS[subsession.round_number - 1]
    for p in subsession.get_players():
        p.question = current_question['question']
        p.option1 = current_question['option1']
        p.option2 = current_question['option2']
        p.option3 = current_question['option3']
        p.option4 = current_question['option4']
        p.option5 = current_question['option5']
        # p.solution = current_question['solution']

        # p.participant.quiz_num_correct = 0


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    question = models.StringField()
    option1 = models.StringField()
    option2 = models.StringField()
    option3 = models.StringField()
    option4 = models.StringField()
    option5 = models.StringField()
    # solution = models.StringField()
    choice = models.StringField(label='',
                                widget=widgets.RadioSelect)
    # is_correct = models.BooleanField()


def choice_choices(player: Player):
    return [
        ['1', player.option1],
        ['2', player.option2],
        ['3', player.option3],
        ['4', player.option4],
        ['5', player.option5],
    ]


class Start(Page):
    def is_displayed(self):
        return self.round_number == 1


class Instructions(Page):
    def is_displayed(self):
        return self.round_number == 1


class Instructions2(Page):
    def is_displayed(self):
        return self.round_number == 1


class StartFree(Page):
    def is_displayed(self):
        return self.round_number == 1


class Stimuli(Page):
    form_model = 'player'
    form_fields = ['choice']

    def vars_for_template(self):
        return dict(
            progress=100*(self.round_number/Constants.num_rounds),
        )

    # @staticmethod
    # def before_next_page(player: Player, timeout_happened):
    #     participant = player.participant
    #
    #     player.is_correct = player.choice == player.solution
    #     participant.quiz_num_correct += int(player.is_correct)


class Results(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == Constants.num_rounds

    @staticmethod
    def vars_for_template(player: Player):
        return dict(round_players=player.in_all_rounds())


page_sequence = [Start, Instructions, Instructions2, StartFree, Stimuli]
