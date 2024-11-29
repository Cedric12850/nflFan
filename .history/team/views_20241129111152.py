from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

#import des models
from team.models import Teams

# Create your views here.
def teams_index(request):
    teams = Teams.objects.all()
    return render(request,'team/index.html', {'teams': teams})

def dynamics_css(request):
    teams = Teams.objects.all()
    css = ""
    for team in teams:
        css += f"""
        .teamColorOne-{team.id} {{
            background-color: {team.colorOne or "#FFFFFF"};
            color: white;
            
        }}
        .teamColorTwo-{team.id} {{
            background-color: {team.colorTwo or "#FFFFFF"},
        }}
        .teamBoxShadow
        """
    return HttpResponse(css, content_type="text/css")

def get_team_by_id(team_id):
    try:
        team = Teams.objects.get(id=team_id)
        return team
    except Teams.DoesNotExist:
        return None
    
def team_detail_view(request, team_id):
    team = get_object_or_404(Teams, id=team_id)
    coaches = team.coachs.all()
    return render(request, 'team/team_detail.html', {'team': team, 'coaches': coaches})