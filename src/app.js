const servicesContainer = document.getElementById("services");

fetch("status.json", {cache: "no-store"})
    .then(response => {
        if(!response.ok) {
            throw new Error("Failed to load status.json");
        }
        return response.json();
    })
    .then(data => {
        servicesContainer.replaceChildren();
        data.services.forEach(service=> {
            const serviceCard = document.createElement("div");
            serviceCard.className = "service-card";

            const serviceName = document.createElement("h2");
            serviceName.textContent = service.name;

            const validStatuses = ["operational", "maintenance"];

            let displayStatus = service.status;

            if (!validStatuses.includes(displayStatus)) {
                displayStatus = "unknown";
            }

            const serviceStatus = document.createElement("p");
            serviceStatus.className = `status ${displayStatus}`;
            serviceStatus.textContent = displayStatus;

            serviceCard.appendChild(serviceName);
            serviceCard.appendChild(serviceStatus);
            servicesContainer.appendChild(serviceCard);
        });
    })
.catch(error => {
    console.error(error);
    servicesContainer.textContent = "Failed to load services.";
})