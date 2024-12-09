from playgames.models import PlayGame

def get_playgame_data():
    total_playgames = PlayGame.objects.count()  # Nombre total de matchs
    return {
        'playgame_count': total_playgames,
        'message': "Bienvenue sur la page des matchs!"
    }