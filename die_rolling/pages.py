from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants


class Introduction_dieroll(Page):
    form_model = 'player'
    form_fields = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6']

    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return dict(
            image_path1='die_rolling/3.mp4',
            image_path2='die_rolling/5.mp4'
        )

    def error_message(self, value):
        if value["q1"] != 0:
            return 'The first question is not answered correctly. Consult the instructions and try again.'
        if value["q2"] != 100:
            return 'The second question is not answered correctly. Consult the instructions and try again.'
        if value["q3"] != 0:
            return 'The third question is not answered correctly. Consult the instructions and try again.'
        if value["q4"] != 0:
            return 'The first question is not answered correctly. Consult the instructions and try again.'
        if value["q5"] != 100:
            return 'The second question is not answered correctly. Consult the instructions and try again.'
        if value["q6"] != 0:
            return 'The third question is not answered correctly. Consult the instructions and try again.'

# class Start_Practice1(Page):
#     def is_displayed(self):
#         return self.round_number == 1


# class Comp1(Page):
#     form_model = 'player'
#     form_fields = ['q1', 'q2', 'q3']
#
#     def is_displayed(self):
#         return self.round_number == 1
#
#     def vars_for_template(self):
#         return dict(
#             image_path='die_rolling/3.mp4'
#         )
#
#     def error_message(self, value):
#         if value["q1"] != 0:
#             return 'The first question is not answered correctly. Consult the instructions and try again.'
#         if value["q2"] != 100:
#             return 'The second question is not answered correctly. Consult the instructions and try again.'
#         if value["q3"] != 0:
#             return 'The third question is not answered correctly. Consult the instructions and try again.'


# class Comp2(Page):
#     form_model = 'player'
#     form_fields = ['q4', 'q5', 'q6']
#
#     def is_displayed(self):
#         return self.round_number == 1
#
#     def vars_for_template(self):
#         return dict(
#             image_path='die_rolling/5.mp4'
#         )
#
#     def error_message(self, value):
#         if value["q4"] != 0:
#             return 'The first question is not answered correctly. Consult the instructions and try again.'
#         if value["q5"] != 100:
#             return 'The second question is not answered correctly. Consult the instructions and try again.'
#         if value["q6"] != 0:
#             return 'The third question is not answered correctly. Consult the instructions and try again.'


class Start_Part1(Page):
    def is_displayed(self):
        return self.round_number == 1


class Roll(Page):
    def vars_for_template(self):
        return dict(
            image_path='die_rolling/{}.mp4'.format(self.player.actual_roll)
        )


class Report_dieroll(Page):
    form_model = 'player'
    form_fields = ['reported_roll']


    def vars_for_template(self):
        reports = [[k, 'die_rolling/{}.png'.format(k)] for k in range(1, 7)]

        return dict(
            next_round=self.subsession.round_number+1,
            reports=reports,
        )

    def before_next_page(self):
        self.player.set_payoffs()
        # In the last round, results for this part are fixed
        # if self.round_number == Constants.num_rounds:
        #     self.player.set_results_dieroll()


class Results_dieroll(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        #Construct table input
        rounds = list(range(1, Constants.num_rounds+1))
        reports = ['die_rolling/{}.png'.format(self.player.in_round(i).reported_roll) for i in rounds]
        payoffs = [self.player.in_round(i).payoff for i in rounds]

        return dict(
            rounds=rounds,
            reports=reports,
            payoffs=payoffs,
        )


page_sequence = [
    Introduction_dieroll,
    Start_Part1,
    Roll,
    Report_dieroll
]
