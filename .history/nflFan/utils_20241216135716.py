from collections import defaultdict
from datetime import datetime, timedelta
from nflFan.services import get_team_results
from playgames.models import PlayGame

def get_playgame_data():
    total_playgames = PlayGame.objects.count()  # Nombre total de matchs
    
    # Récupérer tous les matchs et organiser par semaine
    playgames_by_week = defaultdict(list)
    playgames = PlayGame.objects.select_related('team_local', 'team_visitor', 'week')  # Optimiser les requêtes pour les équipes et la semaine
    presentday = datetime.now()
    print(presentday)
    
    # Trouver la date du jeudi de la semaine en cours
    days_since_thursday = (presentday.weekday() - 3) % 7  # Le jeudi est le jour 3 de la semaine
    start_of_week = presentday - timedelta(days=days_since_thursday)

    # Trouver la date du mardi suivant
    end_of_week = start_of_week + timedelta(days=6)

    # Afficher les dates pour vérifier
    print("Début de la semaine NFL:", start_of_week)
    print("Fin de la semaine NFL:", end_of_week)

    # Organiser les matchs par semaine
    for game in playgames:
        playgames_by_week[game.week].append(game)

    # Obtenir la dernière semaine
    latest_week = max(playgames_by_week.keys(), key=lambda x: x.week_number, default=None)
    latest_playgames = playgames_by_week.get(latest_week, [])
    latest_week_number = latest_week.week_number if latest_week else None

    # print("Dernière semaine:", latest_week)
    # print("Matchs de la dernière semaine:", latest_playgames)
    # Ajouter les bilans des équipes locales et visiteuses pour chaque match
    enhanced_playgames = []
    for game in latest_playgames:
        local_wins, local_losses = get_team_results(game.team_local.id)
        visitor_wins, visitor_losses = get_team_results(game.team_visitor.id)
        enhanced_playgames.append({
            'game': game,
            'local_results': {'wins': local_wins, 'losses': local_losses},
            'visitor_results': {'wins': visitor_wins, 'losses': visitor_losses},
        })

    return {
        'latest_week': latest_week,  # Dernière semaine
        'latest_week_number': latest_week_number,
        'latest_playgames': enhanced_playgames,
    }
