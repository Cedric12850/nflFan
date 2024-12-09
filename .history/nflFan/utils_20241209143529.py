from collections import defaultdict
from nflFan.views import get_team_results
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
    latest_week = max(playgames_by_week.keys(), key=lambda x: x.week_number, default=None)
    latest_playgames = playgames_by_week.get(latest_week, [])
    latest_week_number = latest_week.week_number if latest_week else None

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
        'playgame_count': total_playgames,
        'playgames_by_week': playgames_by_week,
        'latest_playgames': latest_playgames,  # Ajout des matchs de la dernière semaine
        'latest_week': latest_week,  # Dernière semaine
        'latest_week_number': latest_week_number,
        'latest_playgames': enhanced_playgames,  # Ajout des matchs enrichis de la dernière semaine   
    }


