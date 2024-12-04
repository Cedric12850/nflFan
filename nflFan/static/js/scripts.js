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