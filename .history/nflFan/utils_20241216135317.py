from collections import defaultdict
from datetime import datetime, timedelta
from nflFan.services import get_team_results
from playgames.models import PlayGame

# def get_playgame_data():
#     total_playgames = PlayGame.objects.count()  # Nombre total de matchs
    
#     # Récupérer tous les matchs et organiser par semaine
#     playgames_by_week = defaultdict(list)
#     playgames = PlayGame.objects.select_related('team_local', 'team_visitor', 'week')  # Optimiser les requêtes pour les équipes et la semaine
#     presentday = datetime.now()
#     print(presentday)
    
#     # Organiser les matchs par semaine
#     for game in playgames:
#         playgames_by_week[game.week].append(game)

#     # Obtenir la dernière semaine
#     latest_week = max(playgames_by_week.keys(), key=lambda x: x.week_number, default=None)
#     latest_playgames = playgames_by_week.get(latest_week, [])
#     latest_week_number = latest_week.week_number if latest_week else None

#     # print("Dernière semaine:", latest_week)
#     # print("Matchs de la dernière semaine:", latest_playgames)
#     # Ajouter les bilans des équipes locales et visiteuses pour chaque match
#     enhanced_playgames = []
#     for game in latest_playgames:
#         local_wins, local_losses = get_team_results(game.team_local.id)
#         visitor_wins, visitor_losses = get_team_results(game.team_visitor.id)
#         enhanced_playgames.append({
#             'game': game,
#             'local_results': {'wins': local_wins, 'losses': local_losses},
#             'visitor_results': {'wins': visitor_wins, 'losses': visitor_losses},
#         })

#     return {
#         'latest_week': latest_week,  # Dernière semaine
#         'latest_week_number': latest_week_number,
#         'latest_playgames': enhanced_playgames,
#     }

def get_playgame_data():
    # Obtenir les dates de la semaine en cours
    thursday, tuesday = get_current_week_dates()

    print("Semaine en cours :")
    print("Jeudi:", thursday)
    print("Mardi:", tuesday)

    # Récupérer tous les matchs qui se déroulent entre jeudi et mardi
    playgames_in_current_week = PlayGame.objects.filter(
        played_at__gte=thursday,
        played_at__lt=tuesday + timedelta(days=1)
    ).select_related('team_local', 'team_visitor', 'week')  # Optimiser les requêtes pour les équipes et la semaine

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

    return {
        'thursday': thursday,  # Jeudi de la semaine en cours
        'tuesday': tuesday,  # Mardi de la semaine en cours
        'current_week_playgames': enhanced_playgames,  # Matchs de la semaine en cours
    }