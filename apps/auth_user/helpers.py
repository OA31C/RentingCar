from django.utils import translation


def sets_language(language):
    """Sets the project language depending on the user settings"""

    if language == 'en':
        translation.activate(language)
    elif language == 'ru':
        translation.activate(language)
