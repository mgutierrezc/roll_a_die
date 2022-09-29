from otree.api import *



doc = """
welcome page
"""


class Constants(BaseConstants):
    players_per_group = None
    num_rounds = 1
    name_in_url = 'start_part3'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class Welcome(Page):
    pass


page_sequence = [Welcome]
