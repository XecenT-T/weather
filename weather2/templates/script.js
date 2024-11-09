document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const cityInput = document.querySelector('input[name="city"]');

    form.addEventListener('submit', function(event) {
        if (cityInput.value.trim() === '') {
            event.preventDefault(); // Prevent form submission
            alert('Please enter a city name.');
        }
    });
});
