// Function to update weeks based on selected season
function updateWeeks(seasonId) {
    console.log("Updating weeks for season ID:", seasonId);

    if (typeof $ === 'undefined') {
        console.error('jQuery is not loaded.');
        return;
    }

    if (!seasonId) {
        return;
    }

    $.ajax({
        url: '/admin/season/' + seasonId + '/weeks/',  // URL correcte
        method: 'GET',
        success: function(data) {
            console.log("Weeks data:", data);  // Vérifiez les données renvoyées

            let weekSelect = $('select[name="week"]');
            weekSelect.empty();  // Vider les options actuelles

            if (data.weeks.length === 0) {
                weekSelect.append(new Option("Aucune semaine disponible", ""));
            } else {
                data.weeks.forEach(function(week) {
                    weekSelect.append(new Option(week.text, week.id));
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