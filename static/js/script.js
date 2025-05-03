function openEditPopup(popupId) {
    const popup = document.getElementById(popupId);
    popup.style.display = 'flex';
    
    // Focus on the input field
    const input = popup.querySelector('input[name="title"]');
    if (input) {
        setTimeout(() => input.focus(), 100);
    }
    
    // Close when clicking outside
    popup.addEventListener('click', function(e) {
        if (e.target === popup) {
            closeEditPopup(popupId);
        }
    });
}

function closeEditPopup(popupId) {
    const popup = document.getElementById(popupId);
    popup.style.display = 'none';
}

// Close popup with Escape key
document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
        const openPopups = document.querySelectorAll('.popup-container[style="display: flex;"]');
        openPopups.forEach(popup => {
            popup.style.display = 'none';
        });
    }
});

// HTMX event handlers for debugging
document.body.addEventListener('htmx:beforeRequest', function(evt) {
    console.log('Request starting:', evt.detail);
});

document.body.addEventListener('htmx:afterRequest', function(evt) {
    console.log('Request completed:', evt.detail);
});

document.body.addEventListener('htmx:responseError', function(evt) {
    console.error('Response error:', evt.detail);
});