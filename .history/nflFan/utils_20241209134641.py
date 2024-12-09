from collections import defaultdict
from playgames.models import PlayGame

def get_playgame_data():
    total_playgames = PlayGame.objects.count()  # Nombre total de matchs
    
    # Récupérer tous les matchs et organiser par semaine
    playgames_by_week = defaultdict(list)
    playgames = PlayGame.objects.select_related('team_local', 'team_visitor', 'week')  # Optimiser les requêtes pour les équipes et la semaine
    
    # Organiser les matchs par semaine
    for game in playgames:
        playgames_by_week[game.week].append(game)

    # Obtenir la dernière semaine
    latest_week = max(playgames_by_week.keys(), default=None)  # Dernière semaine
    latest_playgames = playgames_by_week.get(latest_week, [])

    return {
        'playgame_count': total_playgames,
        'playgames_by_week': playgames_by_week,
        'latest_playgames': latest_playgames,  # Ajout des matchs de la dernière semaine
        'latest_week': latest_week  # Dernière semaine
    }