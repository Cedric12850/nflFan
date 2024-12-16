from celery import shared_task
from nflFan.utils import get_playgame_data

@shared_task
def update_playgame_display():
    playgame_data = get_playgame_data()
    # Vous pouvez maintenant mettre à jour la base de données ou envoyer des notifications
    # Par exemple, stocker le résultat dans un cache, ou notifier les utilisateurs
    print("Données de la semaine en cours :", playgame_data)
