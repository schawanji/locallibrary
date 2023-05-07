
// JavaScript code to toggle the menu 
function toggleMenu() {
    

    const menuItems = document.querySelector('.menu-items');
    menuItems.classList.toggle('open');
}

//and dropdown

function toggleDropdown(event) {

    event.preventDefault();
    const dropdown = event.target.parentNode;
    const menu = dropdown.querySelector('.manage-catalogue');
    menu.classList.toggle('show');
}


