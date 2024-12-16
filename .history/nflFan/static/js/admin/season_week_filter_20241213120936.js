http://127.0.0.1:8000/admin/season/1/weeks/
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