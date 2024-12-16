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
                url: "/admin/playgames/get_weeks/", // URL de la vue
                data: { season: seasonId },
                success: function(data) {
                    weekField.empty();
                    weekField.append('<option value="">Select a week</option>');
                    data.forEach(function(week) {
                        weekField.append(
                            $('<option>', { value: week.id, text: week.name })
                        );
                    });
                },
                error: function(xhr, status, error) {
                    console.error("Error fetching weeks:", error);
                }
            });
        }

        seasonField.change(updateWeeks);
        updateWeeks(); // Met à jour les semaines au chargement initial
    });
})(django.jQuery);