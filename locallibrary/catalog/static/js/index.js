function toggleDropdown(event) {
    event.preventDefault();
    const parentListItem = event.target.parentNode;
    parentListItem.classList.toggle('open');
  }
  