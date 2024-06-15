from django.apps import AppConfig

class MembersConfig(AppConfig):
    # Domyślne pole automatycznego przyrostu dla modeli w tej aplikacji
    default_auto_field = 'django.db.models.BigAutoField'

    # Nazwa aplikacji, używana przez Django do identyfikacji tej aplikacji
    name = 'members'
