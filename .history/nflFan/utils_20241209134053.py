from collections import defaultdict
from playgames.models import PlayGame

def get_playgame_data():
    total_playgames = PlayGame.objects.count()  # Nombre total de matchs
    
    # Récupérer tous les matchs et organiser par semaine
    playgames_by_week = defaultdict(list)
    playgames = PlayGame.objects.select_related('team_local', 'team_visitor', 'week')  # Optimiser les requêtes pour les équipes et la semaine
    
    for game in playgames:
        playgames_by_week[game.week].append(game)
    print(playgame.)
    return {
        'playgame_count': total_playgames,
        'playgames_by_week': playgames_by_week  # Ajouter les matchs par semaine
    }