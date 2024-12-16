from django import template

register = template.Library()


@register.filter
def first_letters(value, team_name):

    # si la valeur est une chaine de caractère
    if value and isinstance(value, str):
        words = value.split()
        
        if len(words) > 1:      # Si le nom de la ville contient plus d'un mot
            town_initial = ''.join([word[0].upper() for word in words])
            # Si les initial de la ville ne sont pas NY et LA
            if town_initial != 'NY' and town_initial != 'LA':
                return town_initial   
            else:
                team_initial = team_name[0].upper()
                return  town_initial + team_initial  # concatène les 2 première lettre de chaque mot
        else:
            return value[:3].upper()    # sinon on retourne les 3 premières lettres
    return value
# Utiliser les fonction first_letters dans mon template après | sans oublier de {% load le fichier.py %}

@register.filter
def add_suffix(value):
    # Convertir en entier
    try:
        value = int(value)
    except ValueError:
        return value  # Retourne tel quel si ce n'est pas un nombre

    # Déterminer le suffixe
    if 11 <= value % 100 <= 13:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(value % 10, "th")

    return f"{value}{suffix}"