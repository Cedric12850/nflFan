// static/js/admin/season_week_filter.js
function updateWeeks(seasonId) {
    // Vérifiez si jQuery est bien chargé
    if (typeof $ === 'undefined') {
        console.error('jQuery is not loaded.');
        return;
    }

    // Vérifiez si une saison est sélectionnée
    if (!seasonId) {
        return; // Si aucune saison n'est sélectionnée, ne rien faire
    }

    // Effectuer une requête AJAX pour obtenir les semaines de la saison sélectionnée
    $.ajax({
        url: '/admin/season/' + seasonId + '/weeks/',  // Cette URL doit appeler la vue
        method: 'GET',
        success: function(data) {
            let weekSelect = $('select[name="week"]');
            weekSelect.empty();  // Vider les semaines existantes

            if (data.weeks.length === 0) {
                weekSelect.append(new Option("Aucune semaine disponible", ""));  // Option par défaut
            } else {
                data.weeks.forEach(function(week) {
                    weekSelect.append(new Option(week.text, week.id));  // Ajouter les options de semaine
                });
            }
        },
        error: function() {
            console.error("Erreur lors de la récupération des semaines.");
        }
    });
}

// Ajouter l'écouteur d'événement pour le champ saison
$(document).ready(function() {
    // Si une saison est déjà sélectionnée à l'initialisation, charger les semaines
    let selectedSeason = $('select[name="season"]').val();
    if (selectedSeason) {
        updateWeeks(selectedSeason);
    }

    // Mettre à jour les semaines lorsque la saison change
    $('select[name="season"]').on('change', function() {
        let seasonId = $(this).val();
        updateWeeks(seasonId);
    });
});