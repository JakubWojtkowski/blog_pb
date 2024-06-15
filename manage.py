#!/usr/bin/env python
"""
Django's command-line utility for administrative tasks.
"""
import os
import sys

def main():
    """
    Run administrative tasks.
    """
    # Ustawienie domyślnego modułu ustawień Django dla projektu
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')
    try:
        # Importowanie funkcji execute_from_command_line z modułu zarządzania Django
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Obsługa błędu importu Django i wyświetlenie komunikatu o możliwych przyczynach błędu
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # Uruchomienie narzędzia wiersza poleceń Django z argumentami przekazanymi do skryptu
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
