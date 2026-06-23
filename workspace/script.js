document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    // Here you can add your login logic, e.g., API call to verify credentials
    alert(`Username: ${username}
Password: ${password}`);
});