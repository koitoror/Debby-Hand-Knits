## Debby-Hand-Knits
- Cross-Platform E-Commerce App for Hand Knits Show-Casing of all demographic

Author: Daniel Kamar


## Installation

- Read the [requirements](frontend-service/docs/install/requirements.md) guide first

- To install and run the whole dockerized application, read the [Microservices installation guide](frontend-service/docs/install/microservices.md)

- To install just the frontend read the [Frontend installation guide](frontend-service/docs/install/frontend.md)


## Online-Presence 

* Access the hosted application [HERE](http://debby.ga/)
<=======

## Technologies Built With
  * HTML5 - CSS3 - Vanilla JS
  * Python-Flask (Full-stack) Microservices
  * Docker
  * GKE

### Terraform make commands
```
TF_ACTION=apply make terraform action

ENV=staging make check-env

ENV=prod TF_ACTION=apply make terraform action
```