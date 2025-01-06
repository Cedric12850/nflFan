from collections import defaultdict
from datetime import datetime, timedelta
from nflFan.services import get_team_results
from playgames.models import PlayGame

def get_playgame_data():
    # Nombre total de matchs (peut être utilisé pour afficher des stats globales si nécessaire)
    total_playgames = PlayGame.objects.count()

    # Récupération optimisée des matchs avec les relations nécessaires
    playgames = PlayGame.objects.select_related('team_local', 'team_visitor', 'week')

    # Calcul des dates pour déterminer la "semaine NFL" actuelle
    presentday = datetime.now()
    days_since_wednesday = (presentday.weekday() - 2) % 7  # Le mercredi est le jour 2
    start_of_week = presentday - timedelta(days=days_since_wednesday)
    end_of_week = start_of_week + timedelta(days=5)

    # Conversion en `date` pour comparaison avec `week.start_date`
    start_of_week = start_of_week.date()
    end_of_week = end_of_week.date()

    # Afficher les dates pour debug
    # print(f"Début de la semaine NFL : {start_of_week}")
    # print(f"Fin de la semaine NFL : {end_of_week}")

    # Organisation des matchs par semaine
    playgames_by_week = defaultdict(list)
    for game in playgames:
        playgames_by_week[game.week].append(game)

    # Récupérer la semaine actuelle ou, par défaut, la dernière semaine disponible
    current_week = None
    playgames_in_current_week = []

    for week, games in playgames_by_week.items():
        # Si la semaine commence entre les dates NFL actuelles (mercredi à mardi suivant)
        if start_of_week <= week.start_date <= end_of_week:
            current_week = week
            playgames_in_current_week = games
            break

    # Si aucun match trouvé pour la semaine actuelle, récupérer la dernière semaine disponible
    if not current_week:
        latest_week = max(playgames_by_week.keys(), key=lambda x: x.week_number, default=None)
        playgames_in_current_week = playgames_by_week.get(latest_week, [])
        latest_week_number = latest_week.week_number if latest_week else None
    else:
        latest_week = current_week
        latest_week_number = current_week.week_number

    # Ajouter les bilans des équipes locales et visiteuses pour chaque match
    enhanced_playgames = []
    for game in playgames_in_current_week:
        local_wins, local_losses = get_team_results(game.team_local.id)
        visitor_wins, visitor_losses = get_team_results(game.team_visitor.id)
        enhanced_playgames.append({
            'game': game,
            'local_results': {'wins': local_wins, 'losses': local_losses},
            'visitor_results': {'wins': visitor_wins, 'losses': visitor_losses},
        })

    # Retour du contexte avec les données nécessaires pour le template
    return {
        'latest_week': latest_week,
        'latest_week_number': latest_week_number,
        'latest_playgames': enhanced_playgames,
    }
