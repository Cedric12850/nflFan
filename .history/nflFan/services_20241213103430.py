# Service qui permet l'utilisation des fonctions dans tous le projet

from django.db.models import F

from playgames.models import PlayGame
from team.models import Teams

# Récupération des réusltats et calcul du bilan de l'équipe
def get_team_results(team_id):
    # Nombre de victoires en tant qu'équipe locale
    local_wins = PlayGame.objects.filter(
        team_local_id=team_id, 
        score_local__gt=F("score_visitor")  # Victoire si le score_local est supérieur au score_visitor
    ).count()

    # Nombre de victoires en tant qu'équipe visiteuse
    visitor_wins = PlayGame.objects.filter(
        team_visitor_id=team_id, 
        score_visitor__gt=F("score_local")  # Victoire si le score_visitor est supérieur au score_local
    ).count()

    # Total des victoires
    total_wins = local_wins + visitor_wins

    # Nombre de défaites en tant qu'équipe locale
    local_losses = PlayGame.objects.filter(
        team_local_id=team_id, 
        score_local__lt=F("score_visitor")  # Défaite si le score_local est inférieur au score_visitor
    ).count()

    # Nombre de défaites en tant qu'équipe visiteuse
    visitor_losses = PlayGame.objects.filter(
        team_visitor_id=team_id, 
        score_visitor__lt=F("score_local")  # Défaite si le score_visitor est inférieur au score_local
    ).count()

    # Total des défaites
    total_losses = local_losses + visitor_losses

    return total_wins, total_losses


# Calcul de la place de l'équipe dans sa division
def get_division_classement(team_id):
    team = Teams.objects.get(id=team_id)

    # récupération de toutes les équipes d'une division
    team_in_division = Teams.objects.filter(division = team.division)

    # calcul des victoires
    team_result = []
    for division_team in team_in_division:
        total_wins , total_losses = get_team_results(division_team.id)
        team_result.append({
            "team_id": division_team.id,
            "team_name": division_team.name,
            "team_town": division_team.town,
            "team_wins": total_wins,
            "team_losses": total_losses
        })
    
    # 