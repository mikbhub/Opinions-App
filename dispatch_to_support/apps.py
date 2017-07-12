from django.apps import AppConfig
from material.frontend.apps import ModuleMixin


class DispatchToSupportConfig(ModuleMixin, AppConfig):
    name = 'dispatch_to_support'
    icon = '<i class="material-icons">flight_takeoff</i>'