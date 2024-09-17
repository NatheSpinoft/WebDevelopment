function updateCpuUsage(usage) {
    const circle = document.querySelector('.circle');
    const percentage = document.getElementById('cpu-percentage');
    
    // Update the conic-gradient to reflect the CPU usage percentage
    circle.style.background = `conic-gradient(#3498db 0% ${usage}%, #ddd ${usage}% 100%)`;
    percentage.textContent = `${usage}%`;
}

// Example usage:
setInterval(() => {
    // Replace this with actual CPU usage value
    const cpuUsage = Math.floor(Math.random() * 101);
    updateCpuUsage(cpuUsage);
}, 1000);
