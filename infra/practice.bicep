param staticWebAppName string = 'it-status-dashboard-lab'
param location string = 'centralus'

resource staticWebApp 'Microsoft.Web/staticSites@2025-03-01' = {
    name: staticWebAppName
    location: location
    sku: {
        name: 'Free'
        tier: 'Free'

    }
    properties: {}
}
