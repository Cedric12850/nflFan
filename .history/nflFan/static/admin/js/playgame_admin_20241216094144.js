(function($) {
    $(document).ready(function() {
        function updateWeeks() {
            const seasonId = $("#id_season").val();  // Récupère la saison sélectionnée
            const weekField = $("#id_week");

            if (!seasonId) {
                weekField.empty();
                weekField.append('<option value="">Select a week</option>');
                return;
            }

            $.ajax({
                url: "/admin/playgames/get_weeks/",  // Endpoint pour récupérer les semaines
                data: {
                    season: seasonId
                },
                success: function(data) {
                    weekField.empty();  // Vide la liste des semaines
                    weekField.append('<option value="">Select a week</option>');  // Option par défaut
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

        // Lorsqu'une saison est sélectionnée, mettre à jour les semaines
        $("#id_season").change(function() {
            updateWeeks();
        });

        // Initialisation au chargement
        updateWeeks();
    });
})(django.jQuery);