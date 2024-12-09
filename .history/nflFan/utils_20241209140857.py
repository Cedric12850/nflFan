from collections import defaultdict
from playgames.models import PlayGame

def get_playgame_data():
    total_playgames = PlayGame.objects.count()  # Nombre total de matchs
    
    # Récupérer tous les matchs et organiser par semaine
    playgames_by_week = defaultdict(list)
    playgames = PlayGame.objects.select_related('team_local', 'team_visitor', 'week')  # Optimiser les requêtes pour les équipes et la semaine
    
    latest_week = None  # Variable pour stocker la dernière semaine
    for game in playgames:
        playgames_by_week[game.week].append(game)
        # Si c'est la première itération ou que la semaine du match est plus grande
        if not latest_week or game.week.week_number > latest_week.week_number:
            latest_week = game.week
    
    return {
        'playgame_count': total_playgames,
        'playgames_by_week': playgames_by_week,
        'latest_week': latest_week  # Ajout de la semaine la plus récente
    }