try:
    from .settings_platform_specific import DATABASES
except ModuleNotFoundError as identifier:
    from .settings_dev import DATABASES
