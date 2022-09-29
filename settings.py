from os import environ

SESSION_CONFIGS = [
    dict(
        name='norms_project1',
        country='nl',
        display_name="norms_project1",
        app_sequence=['welcome', 'dictator', 'dictator_take', 'dictator_earned', 'jod',
                      'statements_free', 'statements_costly', 'start_part3',
                      'risk', 'die_rolling', 'die_rolling_normative','rule_following'],
        num_demo_participants=15,
    ),
    # dict(
    #     name='dictator',
    #     display_name="dictator",
    #     app_sequence=['dictator'],
    #     num_demo_participants=1,
    # ),
    # dict(
    #     name='dictator_earned',
    #     display_name="dictator_earned",
    #     app_sequence=['dictator_earned'],
    #     num_demo_participants=1,
    # ),
    # dict(
    #     name='dictator_take',
    #     display_name="dictator_take",
    #     app_sequence=['dictator_take'],
    #     num_demo_participants=1,
    # ),
    # dict(
    #     name='dictator_third',
    #     display_name="dictator_third",
    #     app_sequence=['dictator_third'],
    #     num_demo_participants=1,
    # ),
    # dict(
    #     name='dictator_third_judge',
    #     display_name="dictator_third_judge",
    #     app_sequence=['dictator_third_judge'],
    #     num_demo_participants=1,
    # ),
    # dict(
    #     name='jod',
    #     display_name="jod",
    #     app_sequence=['jod'],
    #     num_demo_participants=1,
    # ),
    # dict(
    #     name='tog_efficiency',
    #     display_name="tog_efficiency",
    #     app_sequence=['tog_efficiency'],
    #     num_demo_participants=1,
    # ),
    # dict(
    #     name='tog_equity',
    #     display_name="tog_equity",
    #     app_sequence=['tog_equity'],
    #     num_demo_participants=1,
    # ),
    dict(
        name='die_rolling',
        display_name="die_rolling",
        app_sequence=['die_rolling'],
        num_demo_participants=1,
    ),
    # dict(
    #     name='die_rolling_normative',
    #     country='nl',
    #     display_name="die_rolling_normative",
    #     app_sequence=['die_rolling_normative'],
    #     num_demo_participants=1,
    # ),
    # dict(
    #     name='rule_following',
    #     display_name="rule_following",
    #     app_sequence=['rule_following'],
    #     num_demo_participants=1,
    # ),
    # dict(
    #     name='risk',
    #     display_name="risk",
    #     app_sequence=['risk'],
    #     num_demo_participants=1,
    # ),
    # dict(
    #     name='statements_free',
    #     display_name="statements_free",
    #     app_sequence=['statements_free'],
    #     num_demo_participants=1,
    # ),
    # dict(
    #     name='statements_costly',
    #     display_name="statements_costly",
    #     app_sequence=['statements_costly'],
    #     num_demo_participants=1,
    # ),
    # dict(
    #     name='survey',
    #     country='nl',
    #     display_name="survey",
    #     app_sequence=['survey'],
    #     num_demo_participants=1,
    # ),
    # dict(
    #     name='start_part3',
    #     display_name="start_part3",
    #     app_sequence=['start_part3'],
    #     num_demo_participants=1,
    # ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0.01,
    participation_fee=7.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# EUR or TRY
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = True

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
# ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')
ADMIN_PASSWORD = 'adminasli111'

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""

SECRET_KEY = '{{ secret_key }}'

INSTALLED_APPS = ['otree']
