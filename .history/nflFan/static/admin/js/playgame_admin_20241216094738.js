(function($) {
    $(document).ready(function() {
        const seasonField = $("#id_season");
        const weekField = $("#id_week");

        function updateWeeks() {
            const seasonId = seasonField.val();
            console.log("Selected season ID:", seasonId); // Debug
            if (!seasonId) {
                weekField.empty();
                weekField.append('<option value="">Select a week</option>');
                return;
            }

            $.ajax({
                url: "/admin/playgames/get_weeks/",
                data: {
                    season: seasonId
                },
                success: function(data) {
                    console.log("Weeks received:", data); // Debug
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
                },
                error: function(xhr, status, error) {
                    console.log("AJAX error:", status, error); // Debug
                }
            });
        }

        seasonField.change(updateWeeks);
        updateWeeks();
    });
})(django.jQuery);