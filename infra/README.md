# Azure Infrastructure as Code (Bicep)

## Purpose

This exercise demonstrates how to define, validate, and provision Azure infrastructure using Bicep

## What I Implemented

- Creted Bicep templates for Azure Static Websites.
- Complied and validated the infrastructure configuration.
- Used Azure What-If to preview proposed changes.
- Provisioned a temporay Azure Static Web App using Bicep.
- Verified the resource through Azure CLI and Azure Portal. 
- Deleted the temporary resource after testing.

## Engineering Takeaway

Bicep allows Azure infrastructure to be defined through code instead of relying entirely on manual configuration in the Azure Portal.

This makes infrastructure configurations easier to review, maintain, and reproduce.

I also learned the importance of reviewing proposed infrastructure changes before deploying them to avoid unintentionally modifying existing resources.

## Project Scope

The temporary Static Web App was used to practice infrastructure provisioning and cleanup.

The existing IT Status Dashboard was not modified through Bicep. Its infrastructure template was validated but not deployed against the live application.