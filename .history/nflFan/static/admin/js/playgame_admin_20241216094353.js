(function($) {
    $(document).ready(function() {
        const seasonField = $("#id_season");
        const weekField = $("#id_week");

        function updateWeeks() {
            const seasonId = seasonField.val();
            if (!seasonId) {
                weekField.empty();
                weekField.append('<option value="">Select a week</option>');
                return;
            }

            $.ajax({
                url: "/admin/playgames/get_weeks/",  // L'endpoint Django que nous allons créer
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

        // Lorsque la saison change, met à jour les weeks
        seasonField.change(updateWeeks);

        // Met à jour les weeks au chargement de la page (en cas de pré-sélection)
        updateWeeks();
    });
})(django.jQuery);