document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");
    const emailInput = document.querySelector("#id_email");
    const passwordInput = document.querySelector("#id_password");

    form.addEventListener("submit", function(event) {
        if (!validateEmail(emailInput.value)) {
            event.preventDefault();
            alert("Please enter a valid email address.");
        } else if (passwordInput.value.length < 8) {
            event.preventDefault();
            alert("Password must be at least 8 characters long.");
        }
    });

    function validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    }
});
