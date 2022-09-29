from otree.api import *

import random


class Constants(BaseConstants):
    name_in_url = 'die_rolling'
    players_per_group = None
    num_rounds = 1
    lying_reward_die_roll = cu(100)  # payoff for die roll for the paying number
    no_lying_reward_die_roll = cu(0)  # payoff for die roll for any other number


class Subsession(BaseSubsession):
    def creating_session(self):
        print('in creating_session', self.round_number)

        for p in self.get_players():
            p.actual_roll = random.randint(1, 6)
            print('set the actual roll for player', p.id_in_subsession, 'and round', self.round_number, 'to', p.actual_roll)
            if self.round_number == 1:
                # only one part is paid at random. 1 is part 1, 2 is part 2.
                p.participant.vars['paying_part'] = random.choice([1, 2])
                print('set the paying part for player', p.id_in_subsession, 'to', p.participant.vars['paying_part'])


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    q1 = models.IntegerField(initial=None, label="")
    q2 = models.IntegerField(initial=None, label="")
    q3 = models.IntegerField(initial=None, label="")
    q4 = models.IntegerField(initial=None, label="")
    q5 = models.IntegerField(initial=None, label="")
    q6 = models.IntegerField(initial=None, label="")

    truthful = models.IntegerField()

    report = models.IntegerField()

    room_for_lying = models.IntegerField()

    lying_behavior = models.FloatField()

    reported_roll = models.IntegerField(min=1, max=6, label="The outcome of the die roll was", doc="""reported roll""")

    actual_roll = models.IntegerField(min=1, max=6, label="", doc="""actual roll""")

    # Set payoffs assigns the rewards for each round.
    def set_payoffs(self):
        print('in set_payoffs')
        if self.reported_roll == 5:
            self.payoff = Constants.lying_reward_die_roll
            self.report = 1
        else:
            self.payoff = Constants.no_lying_reward_die_roll
            self.report = 0
        if self.actual_roll == 5:
            self.truthful = 1
        else:
            self.truthful = 0

    # def set_results_dieroll(self):
    #     print('in set_results')
    #     self.room_for_lying = Constants.num_rounds - sum([p.truthful for p in self.in_all_rounds()])
    #     self.lying_behavior = (
    #                 sum([p.report for p in self.in_all_rounds()]) - sum([p.truthful for p in self.in_all_rounds()]))
    #     if self.room_for_lying == 0:
    #         self.participant.vars['lying_part1'] = 0.55
    #     else:
    #         self.participant.vars['lying_part1'] = self.lying_behavior / self.room_for_lying
    #     print("The room for lying for", self.id_in_subsession, 'was', self.room_for_lying)
    #     print("The actual fraction of lying for", self.id_in_subsession, 'was', self.participant.vars['lying_part1'])
    #     self.participant.vars['score_part1'] = sum([p.payoff for p in self.in_all_rounds()])
    #     print('Overall score for part 1 and player', self.id_in_subsession, 'was', self.participant.vars['score_part1'])
    #     self.participant.vars['reports'] = [p.reported_roll for p in self.in_all_rounds()]
    #     self.participant.vars['actual_rolls'] = [p.actual_roll for p in self.in_all_rounds()]
