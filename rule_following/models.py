from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

doc = 'Survey of trust attitudes and demographics'


class Constants(BaseConstants):
    name_in_url = 'rule_following'
    players_per_group = None
    num_rounds = 1
    num_balls = 50
    points_a = 5
    points_b = 10


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    balls_A = models.IntegerField()
    balls_B = models.IntegerField()
    balls_I = models.IntegerField(min=0, max=0)

    ex1 = models.CurrencyField(
        doc="""Answer to first example""",
        min=0,
        max=Constants.num_balls*Constants.points_b,
        label="",
    )

    ex2 = models.CurrencyField(
        doc="""Answer to second example""",
        min=0,
        max=Constants.num_balls*Constants.points_b,
        label="",
    )
