// Laptop Fingerprint Authentication
document.getElementById('laptopAuth').addEventListener('click', async () => {
    const studentId = prompt("Enter your Student ID:");
    try {
        const response = await fetch('http://localhost:5000/laptop-auth', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ studentId })
        });
        const data = await response.json();
        alert(data.message);
    } catch (error) {
        alert("Authentication failed. Please try again.");
        console.error(error);
    }
});

// Hardware Fingerprint Authentication
document.getElementById('hardwareAuth').addEventListener('click', async () => {
    const studentId = prompt("Enter your Student ID:");
    try {
        const response = await fetch('http://localhost:5000/hardware-auth', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ studentId })
        });
        const data = await response.json();
        alert(data.message);
    } catch (error) {
        alert("Authentication failed. Please try again.");
        console.error(error);
    }
});
