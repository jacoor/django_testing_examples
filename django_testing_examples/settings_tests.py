from django_testing_examples.settings import *  # noqa: F403

Debug = False

try:
    # github action settings
    # template location: .github/workflows/test/settings_local_template.py
    from django_testing_examples.settings_tests_local import *  # noqa: F403
except ImportError:
    pass