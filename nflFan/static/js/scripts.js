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

// Affichage des images de l'équipe dans le select de recherche d'un joueur
document.addEventListener('DOMContentLoaded', function() {
    const teamSelect = document.getElementById('team-select');
    const options = teamSelect.querySelectorAll('option');

    // Ajoute l'image à chaque option
    options.forEach(function(option) {
        const teamLogo = option.text.split(' ')[0]; // Récupère le chemin de l'image (url)
        const teamName = option.text.split(' ')[1]; // Récupère le nom de l'équipe
        const image = document.createElement('img');
        image.src = teamLogo;
        image.alt = teamName;
        image.style.width = '20px'; // Vous pouvez ajuster la taille ici
        image.style.marginRight = '10px'; // Espacement entre l'image et le texte
        option.innerHTML = '';  // Efface le texte de l'option
        option.appendChild(image); // Ajoute l'image à l'option
        option.appendChild(document.createTextNode(` ${teamName}`)); // Ajoute le texte après l'image
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