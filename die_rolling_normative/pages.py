from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants


class Introduction_dieroll(Page):
    def is_displayed(self):
        return self.round_number == 1


class Start_Practice1(Page):
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return dict(
            country=self.session.config['country'],
        )


class Comp1(Page):
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        #Construct table input
        rounds = list(range(1, 4))

        return dict(
            rounds=rounds,
            reports=['die_rolling_normative/5.png', 'die_rolling_normative/5.png', 'die_rolling_normative/5.png'],
            observations=['die_rolling_normative/5.png', 'die_rolling_normative/3.png', 'die_rolling_normative/4.png'],
        )


class Comp2(Page):
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        #Construct table input
        rounds = list(range(1, 4))

        return dict(
            rounds=rounds,
            reports=['die_rolling_normative/5.png', 'die_rolling_normative/5.png', 'die_rolling_normative/5.png'],
            observations=['die_rolling_normative/2.png', 'die_rolling_normative/3.png', 'die_rolling_normative/6.png'],
        )


class Comp3(Page):
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        #Construct table input
        rounds = list(range(1, 4))

        return dict(
            rounds=rounds,
            reports=['die_rolling_normative/5.png', 'die_rolling_normative/5.png', 'die_rolling_normative/5.png'],
            observations=['die_rolling_normative/6.png', 'die_rolling_normative/1.png', 'die_rolling_normative/4.png'],
        )


class Start_Part1(Page):
    def is_displayed(self):
        return self.round_number == 1


class Roll(Page):
    def vars_for_template(self):
        return dict(
            image_path='die_rolling_normative/{}.mp4'.format(self.player.actual_roll)
        )


class Report_dieroll(Page):
    form_model = 'player'
    form_fields = ['reported_roll']

    def vars_for_template(self):
        reports = [[k, 'die_rolling_normative/{}.png'.format(k)] for k in range(1, 7)]

        return dict(
            next_round=self.subsession.round_number+1,
            reports=reports,
        )

    def before_next_page(self):
        self.player.set_payoffs()
        # In the last round, results for this part are fixed
        # if self.round_number == Constants.num_rounds:
        #     self.player.set_results_dieroll()


# class Results_dieroll(Page):
#     def is_displayed(self):
#         return self.round_number == Constants.num_rounds
#
#     def vars_for_template(self):
#         #Construct table input
#         rounds = list(range(1, Constants.num_rounds+1))
#         reports = ['die_rolling_prosocial/{}.png'.format(self.player.in_round(i).reported_roll) for i in rounds]
#         payoffs = [self.player.in_round(i).payoff for i in rounds]
#
#         return dict(
#             rounds=rounds,
#             reports=reports,
#             payoffs=payoffs,
#         )


page_sequence = [
    Introduction_dieroll,
    Start_Practice1,
    Comp1,
    Comp2,
    Comp3,
    Start_Part1,
    Roll,
    Report_dieroll,
]
