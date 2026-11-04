# Engineering Decision Notes

## 1. Business Problem

An IT service status dashboard is useful for internal IT teams and employees who need to stay informed about service outages, scheduled maintenance, and updates. It helps improve communication across the organization by providing visibility into the status of important IT services.

## 2. Cloud Hosting Decision

I decided to use Azure Static Web Apps because the application only requires HTML, CSS, JavaScript, and JSON. Using a virtual machine would introduce unnecessary operating system maintenance and infrastructure overhead. Static hosting provides a simpler solution for this type of application.

## 3. Data Storage Decision

I chose a JSON file to store information about the IT services because it is simple, easy to manage, and does not require a database. However, service statuses must be updated manually because the application does not automatically monitor the services.

## 4. Deployment Strategy

I used GitHub Actions to automate application deployments to Azure. Whenever changes are pushed to the main branch, the workflow runs validation and regression tests before deployment. This helps prevent invalid service data from reaching the live website.

## 5. Reliability and Recovery

I intentionally introduced invalid service data to verify that the deployment pipeline would reject it. I also used Git revert to reverse a previous change and restore the expected application state. These tests demonstrate how the project detects certain errors and recovers from unwanted changes.

## 6. Current Limitations

The application currently requires manual updates to service statuses and does not provide automated, real-time monitoring. In a production environment, I would consider adding automated health checks, alerting capabilities, and a backend service. These improvements would make the dashboard more useful for an organization's IT operations.