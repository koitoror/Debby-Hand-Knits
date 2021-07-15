<!-- [![CircleCI](https://circleci.com/gh/koitoror/Debby-Hand-Knits.svg?style=svg)](https://circleci.com/gh/koitoror/Debby-Hand-Knits) -->

[![CircleCI](https://img.shields.io/circleci/build/github/koitoror/Debby-Hand-Knits?label=main&logo=circleci)](https://circleci.com/gh/koitoror/Debby-Hand-Knits/tree/main)
![GitHub Workflow Status (branch)](https://img.shields.io/github/workflow/status/koitoror/Debby-Hand-Knits/Build%20and%20Deploy%20to%20Google%20Compute%20Engine/master?label=GH-Action%20WF&style=social)
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
  * Github-Actions

### Terraform make commands
```
TF_ACTION=apply make terraform action

ENV=staging make check-env

ENV=prod TF_ACTION=apply make terraform action
```
