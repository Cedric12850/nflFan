// message lors de l'ajout d'un joueur

document.addEventListener('DOMContentLoaded', () => {
    const messages = document.getElementsByClassName('messages');
    if (messages) {
        setTimeout(() => {
            messages.style.transition = 'opacity 1s';
            messages.style.opacity = 0; // Disparaît en douceur
            setTimeout(() => messages.remove(), 1000); // Supprime après la transition
        }, 10000); // 10 secondes
    }
});

// Affichage des images dans le sel