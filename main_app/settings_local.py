try:
    from .settings_platform_specific import (
        DATABASES,
        DEBUG,
        ALLOWED_HOSTS,
        CORS_ORIGIN_WHITELIST,
    )
except ModuleNotFoundError as identifier:
    from .settings_dev import (
        DATABASES,
        DEBUG,
        ALLOWED_HOSTS,
        CORS_ORIGIN_WHITELIST,
    )
