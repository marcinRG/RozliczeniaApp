const deleteButtons = document.querySelectorAll('.remove-button')

const popUpMessage = document.querySelector('.modal .modal-body')
const popUpRemoveButton = document.querySelector('.modal .action-remove')

for (const deleteBtn of deleteButtons) {
    deleteBtn.addEventListener('click', (event) => {
        const btn = event.target;
        const itemName = btn.getAttribute('data-name');
        const itemId = btn.getAttribute('data-id');
        popUpMessage.textContent = `Czy chcesz usunąć ${itemName} z bazy danych?`;
        popUpRemoveButton.setAttribute('href',
            `${window.location.pathname}?mode=remove&id_elem=${itemId}`);
    });
}
