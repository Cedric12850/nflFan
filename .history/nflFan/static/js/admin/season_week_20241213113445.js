(function($) {
    // Lorsque le champ saison est modifié
    $('#id_season').change(function() {
        var season_id = $(this).val();  // Récupérer l'ID de la saison sélectionnée

        if (season_id) {
            // Faire une requête AJAX pour obtenir les semaines pour cette saison
            $.ajax({
                url: '/get_weeks_for_season/',  // L'URL de la vue AJAX
                data: {
                    'season_id': season_id  // Envoyer l'ID de la saison
                },
                success: function(data) {
                    var week_select = $('#id_week');
                    week_select.empty();  // Vider le champ de semaine

                    // Ajouter une option vide
                    week_select.append('<option value="">---------</option>');

                    // Remplir le champ de semaines avec les résultats de la requête AJAX
                    $.each(data, function(index, week) {
                        week_select.append('<option value="' + week.id + '">' + week.week_number + '</option>');
                    });
                }
            });
        } else {
            // Si aucune saison n'est sélectionnée, vider le champ de semaine
            $('#id_week').empty();
        }
    });
})(django.jQuery);