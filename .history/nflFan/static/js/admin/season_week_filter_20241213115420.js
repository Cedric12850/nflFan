// static/js/admin/season_week_filter.js
function updateWeeks(seasonId) {
    // Effectuer une requête pour obtenir les semaines associées à la saison sélectionnée
    $.ajax({
        url: '/admin/season/' + seasonId + '/weeks/',  // Vous devrez créer une vue pour cela
        method: 'GET',
        success: function(data) {
            let weekSelect = $('select[name="week"]');
            weekSelect.empty();  // Vider les semaines existantes
            data.weeks.forEach(function(week) {
                weekSelect.append(new Option(week.text, week.id));  // Ajouter les options pour chaque semaine
            });
        }
    });
}