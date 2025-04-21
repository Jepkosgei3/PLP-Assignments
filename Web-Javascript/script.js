// Event Listeners
document.getElementById('click-me').addEventListener('click', function() {
    const output = document.getElementById('event-output');
    output.classList.remove('hidden');
    setTimeout(() => output.classList.add('hidden'), 2000);
});

document.getElementById('hover-me').addEventListener('mouseover', function() {
    this.textContent = "You're hovering!";
});
document.getElementById('hover-me').addEventListener('mouseout', function() {
    this.textContent = "Hover Over Me";
});

// Form Validation
const form = document.getElementById('demo-form');
form.addEventListener('submit', function(e) {
    e.preventDefault();
    let isValid = true;

    // Name validation
    const name = document.getElementById('name').value.trim();
    if (name === '') {
        document.getElementById('name-error').textContent = 'Name is required';
        isValid = false;
    } else {
        document.getElementById('name-error').textContent = '';
    }

    // Email validation
    const email = document.getElementById('email').value.trim();
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        document.getElementById('email-error').textContent = 'Please enter a valid email';
        isValid = false;
    } else {
        document.getElementById('email-error').textContent = '';
    }

    // Password validation
    const password = document.getElementById('password').value;
    if (password.length < 8) {
        document.getElementById('password-error').textContent = 'Password must be at least 8 characters';
        isValid = false;
    } else {
        document.getElementById('password-error').textContent = '';
    }

    if (isValid) {
        form.reset();
        const successMsg = document.getElementById('form-success');
        successMsg.classList.remove('hidden');
        setTimeout(() => successMsg.classList.add('hidden'), 3000);
    }
});

// Interactive Elements
let count = 0;
const counterDisplay = document.getElementById('counter');

document.getElementById('increment').addEventListener('click', function() {
    count++;
    counterDisplay.textContent = count;
});

document.getElementById('decrement').addEventListener('click', function() {
    count--;
    counterDisplay.textContent = count;
});

document.getElementById('color-select').addEventListener('change', function() {
    const colorBox = document.getElementById('color-box');
    colorBox.style.backgroundColor = this.value;
});
