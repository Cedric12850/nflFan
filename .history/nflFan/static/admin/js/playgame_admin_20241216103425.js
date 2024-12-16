(function($) {
    $(document).ready(function() {
        // Exemple : Lors du changement de la saison
        $('#id_season').change(function() {
            var seasonId = $(this).val(); // Récupère l'ID de la saison sélectionnée
            if (seasonId) {
                // Envoie une requête AJAX pour récupérer les semaines
                $.ajax({
                    url: '/admin/playgames/get_weeks/', // URL de la vue Django
                    data: { season: seasonId },
                    success: function(data) {
                        // Mets à jour le champ des semaines
                        var weekSelect = $('#id_week');
                        weekSelect.empty(); // Vide les options existantes
                        data.forEach(function(week) {
                            weekSelect.append(new Option(week.name, week.id));
                        });
                    },
                    error: function(xhr, status, error) {
                        console.error('Erreur lors de la récupération des semaines:', error);
                    }
                });
            }
        });
    });
})(django.jQuery); // Utilise django.jQuery comme $ si jQuery est chargé par Django