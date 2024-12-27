// Get the hamburger icon and the nav links container
const hamburger = document.getElementById('hamburger-icon');
const navLinks = document.querySelector('.nav-link');

// Add event listener to toggle 'active' class
hamburger.addEventListener('click', () => {
    navLinks.classList.toggle('active'); // This toggles the visibility of the menu
});

