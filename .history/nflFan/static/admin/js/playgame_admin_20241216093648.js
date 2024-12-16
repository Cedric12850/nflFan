(function($) {
    $(document).ready(function() {
        // Met à jour les options de la liste déroulante "week" en fonction de la saison sélectionnée
        function updateWeeks() {
            const seasonId = $("#id_season").val();
            const weekField = $("#id_week");
            if (!seasonId) {
                weekField.empty();
                weekField.append('<option value="">Select a week</option>');
                return;
            }

            $.ajax({
                url: "/admin/playgames/get_weeks/",  // Endpoint à créer
                data: {
                    season: seasonId
                },
                success: function(data) {
                    weekField.empty();
                    weekField.append('<option value="">Select a week</option>');
                    data.forEach(function(week) {
                        weekField.append(
                            $('<option>', {
                                value: week.id,
                                text: week.name
                            })
                        );
                    });
                }
            });
        }

        // Écoute les changements sur le champ saison
        $("#id_season").change(function() {
            updateWeeks();
        });

        // Initialise lors du chargement
        updateWeeks();
    });
})(django.jQuery);