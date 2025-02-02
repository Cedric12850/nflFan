// message lors de l'ajout d'un joueur
document.addEventListener('DOMContentLoaded', () => {
    const messages = document.getElementsByClassName('messages');
    if (messages.length > 0) {
        setTimeout(() => {
            Array.from(messages).forEach((message) => {
                message.style.transition = 'opacity 1s';
                message.style.opacity = 0; // Disparaît en douceur
                setTimeout(() => message.remove(), 1000); // Supprime après la transition
            });
        }, 5000); // 5 secondes
    }
});

// REdirection vers la page détail du joueur grace à data-link
document.querySelectorAll('.playerCard').forEach(card => {
    card.addEventListener('click', () => {
        const link = card.getAttribute('data-link');
        window.location.href = link;
    });
});

// Affichage des équipes par division dans la navBar
document.addEventListener("DOMContentLoaded", () => {
    fetch('/navbar/divisions/')
        .then(response => response.json())
        .then(data => {
            const navBar = document.getElementById('navbar-divisions')

        // Boucle sur les divisions et équipes
        data.forEach(division => {
            
            // Création d'un li pour chaque division
            const divisionLi = document.createElement('div');
            divisionLi.textContent = division.division;
            divisionLi.classList.add('divDivision')

            // Création des li équipes dans chaque li de division
            const teamList = document.createElement('div');
            // Boucle sur chaque division pour avoir la liste des équipes
            division.teams.forEach(team => {
                const teamItem = document.createElement('li');

                // Ajoute l'image de l'équipe
                const teamImg = document.createElement('img');
                teamImg.src = `/media/${team.thumbnail}`;
                teamImg.alt = `${team.name} logo`;
                teamImg.style.width = '20px';
                teamImg.style.marginRight = '10px';

                // Création du lien pour accéder à l'équipe
                const teamLink = document.createElement('a');
                teamLink.classList.add('dropdown-item', 'linkTeamMenu'),
                teamLink.href = `/teams/${team.id}`;
                // Ajout des éléments dans le lien
                teamLink.appendChild(teamImg); // Ajoute l'image d'abord
                teamLink.appendChild(document.createTextNode(`${team.town} ${team.name}`)); // Ajoute le texte après

                
                teamItem.appendChild(teamLink);
                teamList.appendChild(teamItem);
            });

            // Ajout des division dans la navbar
            divisionLi.appendChild(teamList);
            navBar.appendChild(divisionLi);
        });
    })
    .catch(error => console.error('Erreur lors du chargement des divisions :', error));
})


// Js pour récupérer les week by season
document.addEventListener("DOMContentLoaded", function () {
    const seasonSelect = document.getElementById("id_season");
    const weekSelect = document.getElementById("id_week");

    if (seasonSelect) {
        seasonSelect.addEventListener("change", function () {
            const seasonId = this.value;

            if (seasonId) {
                fetch(`/ajax/load-weeks/?season=${seasonId}`)
                    .then((response) => response.json())
                    .then((data) => {
                        weekSelect.innerHTML = "";

                        // Ajouter une option vide
                        const emptyOption = document.createElement("option");
                        emptyOption.textContent = "Sélectionnez une semaine";
                        emptyOption.value = "";
                        weekSelect.appendChild(emptyOption);

                        // Ajouter les options de semaines
                        data.forEach(function (week) {
                            const option = document.createElement("option");
                            option.value = week.id;
                            option.textContent = `Semaine ${week.week_number}`;
                            weekSelect.appendChild(option);
                        });
                    })
                    .catch((error) => console.error("Erreur lors du chargement des semaines :", error));
            } else {
                // Si aucune saison n'est sélectionnée, vider le champ "week"
                weekSelect.innerHTML = "";
            }
        });
    }
});

// Scroll button
const buttonLeft = document.getElementById('scrollLeft');
const buttonRight = document.getElementById('scrollRight');

    buttonLeft.onclick = function (){
        document.querySelector('.viewResultMatch').scrollLeft -=100;
    };
    buttonRight.onclick = function (){
        document.querySelector('.viewResultMatch').scrollLeft +=100;
    };

// effet blur sur les résultats
const buttonBlurEffect = document.getElementById('blurEffect');
const resultTeam = document.querySelectorAll('#blurScore');
    for (let i = 0; i < resultTeam.length; i++) {
        resultTeam[i].style.filter = 'blur(3px)';
    let isBlurred = false;

    buttonBlurEffect.onclick = function () {
        // Alterner l'état du flou
        isBlurred = !isBlurred;

        // Appliquer ou retirer l'effet de flou selon l'état
        for (let i = 0; i < resultTeam.length; i++) {
            if (isBlurred) {
                resultTeam[i].style.filter = 'none';
            }
            else{
                resultTeam[i].style.filter = 'blur(3px)';
            }
        }
    }
}

// autocomplete players
document.addEventListener("DOMContentLoaded", function () {
    const searchInput = document.getElementById("search");
    const autocompleteResults = document.getElementById("autocomplete-results");

    searchInput.addEventListener("input", function () {
        const query = this.value;

        if (query.length > 2) { // Lancer l'autocomplétion après 2 caractères
            fetch(`/players/autocomplete/?term=${query}`)
                .then((response) => response.json())
                .then((data) => {
                    autocompleteResults.innerHTML = "";
                    autocompleteResults.style.display = "block";

                    data.forEach((item) => {
                        const li = document.createElement("li");
                        li.textContent = item.label;
                        li.classList.add("list-group-item");
                        li.style.cursor = "pointer";

                        li.addEventListener("click", function () {
                            searchInput.value = item.value;
                            autocompleteResults.style.display = "none";
                        });

                        autocompleteResults.appendChild(li);
                    });
                });
        } else {
            autocompleteResults.style.display = "none";
        }
    });

    // Cacher les résultats si l'utilisateur clique ailleurs
    document.addEventListener("click", function (event) {
        if (!autocompleteResults.contains(event.target)) {
            autocompleteResults.style.display = "none";
        }
    });
});

// Affichage des logo equipes dasn addPlaygames.html
$(document).ready(function () {
    $('.team-select').select2({
        width: '100%',  // Assurez-vous que le select prend toute la largeur
        dropdownCssClass: 'form-select', // Appliquer la classe de Bootstrap à l'élément du dropdown
        selectionCssClass: 'form-select', // Appliquer la classe de Bootstrap au champ sélectionné
        minimumResultsForSearch: Infinity, // Supprimer la recherche si ce n'est pas nécessaire
        templateResult: function (data) {
            if (!data.id) {
                return data.text;
            }
            const imgUrl = $(data.element).data('image');
            return $(
                `<span style="display: flex; align-items: center;">
                    <img src="${imgUrl}" style="width: 30px; height: 30px; margin-right: 10px; border-radius: 5px;" />
                    ${data.text}
                </span>`
            );
        },
        templateSelection: function (data) {
            const imgUrl = $(data.element).data('image');
            return $(
                `<span style="display: flex; align-items: center;">
                    <img src="${imgUrl}" style="width: 30px; height: 30px; margin-right: 10px; border-radius: 5px;" />
                    ${data.text}
                </span>`
            );
        }
    });
});