const nameInput = document.getElementById('name');
nameInput.addEventListener('focusout', function(e) {
    const value = e.target.value.trim();
    let newDiv = document.getElementById('name-error');

    if (value.length < 2 || value.length > 30) {
        if (!newDiv) {
            newDiv = document.createElement('div');
            newDiv.id = 'name-error';
            nameInput.insertAdjacentElement("afterend", newDiv);
        }
        newDiv.innerHTML = '<p class="error">Name must be between 2 and 30 characters long.</p>';
    } else {
        if (newDiv) {
            newDiv.remove();
        }
    }
});

const emailInput = document.getElementById('email');
emailInput.addEventListener('focusout', function (e) {
    const value = e.target.value.trim();
    let newDiv = document.getElementById('email-error');

    if (!value.includes('@')) {
        if (!newDiv) {
            newDiv = document.createElement('div');
            newDiv.id = 'email-error';
            emailInput.insertAdjacentElement("afterend", newDiv);
        }
        newDiv.innerHTML = '<p class="error">Email must contain "@".</p>';
    } else {
        if (newDiv) {
            newDiv.remove();
        }
    }
});

const subjectInput = document.getElementById('subject');
subjectInput.addEventListener('focusout', function (e) {
    const value = e.target.value.trim();
    let newDiv = document.getElementById('subject-error');

    if (value.length < 3 || value.length > 50) {
        if (!newDiv) {
            newDiv = document.createElement('div');
            newDiv.id = 'subject-error';
            subjectInput.insertAdjacentElement("afterend", newDiv);
        }
        newDiv.innerHTML = '<p class="error">Subject must be between 3 and 50 characters.</p>';
    } else {
        if (newDiv) {
            newDiv.remove();
        }
    }
});

const messageInput = document.getElementById('message');
messageInput.addEventListener('focusout', function (e) {
    const value = e.target.value.trim();
    let newDiv = document.getElementById('message-error');

    if (value.length < 10 || value.length > 1000) {
        if (!newDiv) {
            newDiv = document.createElement('div');
            newDiv.id = 'message-error';
            messageInput.insertAdjacentElement("afterend", newDiv);
        }
        newDiv.innerHTML = '<p class="error">Message must be between 10 and 1000 characters.</p>';
    } else {
        if (newDiv) {
            newDiv.remove();
        }
    }
});
