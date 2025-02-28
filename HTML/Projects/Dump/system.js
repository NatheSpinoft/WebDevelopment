// CPU Load Simulation
function simulateCpuLoad() {
    const startTime = performance.now();
    // Simulate CPU work
    for (let i = 0; i < 1000000; i++) {
        Math.sqrt(i);
    }
    const endTime = performance.now();
    const cpuLoad = ((endTime - startTime) / 100).toFixed(2); // Simulated CPU load
    document.getElementById("cpu-load").textContent = `${cpuLoad}%`;
}

// Network Information
function updateNetworkInfo() {
    if (navigator.connection) {
        const connection = navigator.connection;
        const networkInfo = `
            Type: ${connection.effectiveType}, 
            Downlink: ${connection.downlink} Mbps, 
            RTT: ${connection.rtt} ms
        `;
        document.getElementById("network-info").textContent = networkInfo;
    } else {
        document.getElementById("network-info").textContent = "Network API not supported";
    }
}

// Battery Status
function updateBatteryStatus() {
    if (navigator.getBattery) {
        navigator.getBattery().then(battery => {
            const batteryStatus = `
                Level: ${(battery.level * 100).toFixed(2)}%, 
                Charging: ${battery.charging ? "Yes" : "No"}
            `;
            document.getElementById("battery-status").textContent = batteryStatus;
        });
    } else {
        document.getElementById("battery-status").textContent = "Battery API not supported";
    }
}

// Screen Resolution
function updateScreenResolution() {
    const screen = window.screen;
    const resolution = `
        Width: ${screen.width}, 
        Height: ${screen.height}, 
        Color Depth: ${screen.colorDepth} bits
    `;
    document.getElementById("screen-resolution").textContent = resolution;
}

// Update all stats every second
setInterval(() => {
    simulateCpuLoad();
    updateNetworkInfo();
    updateBatteryStatus();
    updateScreenResolution();
}, 1000);