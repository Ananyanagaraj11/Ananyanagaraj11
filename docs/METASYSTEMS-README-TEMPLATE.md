# MetaSystems — Enterprise Backend Platform (Portfolio Summary)

> **Note:** This documents professional work at MetaSystems. Source code is proprietary and not published.  
> This README is a **sanitized engineering summary** for portfolio / interview discussion.

[![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)](https://www.java.com/)
[![Spring Boot](https://img.shields.io/badge/Spring_Boot-6DB33F?style=for-the-badge&logo=springboot&logoColor=white)](https://spring.io/projects/spring-boot)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Kafka](https://img.shields.io/badge/Apache_Kafka-231F20?style=for-the-badge&logo=apache-kafka&logoColor=white)](https://kafka.apache.org/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)](https://kubernetes.io/)

## Overview

Developed **Java Spring Boot microservices** and **event-driven data pipelines** for enterprise financial and regulatory reporting workflows.

| | |
|---|---|
| **Role** | Software Engineer |
| **Period** | Jun 2021 – Jul 2024 |
| **Location** | Bangalore, India |
| **Scale** | **80+ financial and regulatory data feeds daily** |

## Architecture

```mermaid
flowchart LR
  subgraph Input
    F[80+ Daily Feeds]
  end
  subgraph Core
    MS[Spring Boot Microservices]
    REST[Secure REST APIs]
  end
  subgraph Events
    K[Kafka]
    R[RabbitMQ]
    C[(Redis)]
  end
  subgraph Store
    DB[(PostgreSQL)]
  end
  subgraph Deploy
    CI[Jenkins / GitHub Actions]
    D[Docker / Kubernetes / AWS]
  end
  F --> MS
  MS --> REST
  MS --> K
  MS --> R
  MS --> DB
  MS --> C
  MS --> CI
  CI --> D
```

## Key Features

| Feature | Engineering Focus | Impact |
|---|---|---|
| **Backend Service Development** | Java Spring Boot microservices + REST APIs | **80+ feeds/day** processing |
| **Microservices & Event Processing** | Kafka, RabbitMQ, Redis async pipelines | Cross-service data synchronization |
| **Secure API Platform** | Spring Security + JWT REST APIs | Authenticated service integrations |
| **Cloud Deployment & Performance** | Jenkins, Docker, K8s, GitHub Actions | **20% SQL performance gain** via indexing + Redis caching |
| **Software Quality & Delivery** | JUnit + PyTest, unit/integration/API tests | **85% code coverage**; Agile delivery |

## Tech Stack

| Category | Technologies |
|---|---|
| Languages | Java, Python |
| Backend | Spring Boot, REST APIs, microservices |
| Security | Spring Security, JWT |
| Messaging | Apache Kafka, RabbitMQ |
| Data | PostgreSQL, Redis |
| DevOps | Jenkins, Docker, Kubernetes, GitHub Actions, AWS |
| Testing | JUnit, PyTest |

## API Surface (Conceptual)

| Area | Capabilities |
|---|---|
| REST APIs | Enterprise reporting and integration endpoints |
| Auth | JWT-based service-to-service authentication |
| Event APIs | Async ingestion via Kafka / RabbitMQ consumers |

> OpenAPI specs and endpoints are proprietary.

## Setup

```text
Not publicly available — proprietary employer codebase.
```

## Screenshots

| Component | Preview |
|---|---|
| Service Dashboard | _Placeholder_ |
| Pipeline Monitoring | _Placeholder_ |
| CI/CD Pipeline | _Placeholder_ |

## Engineering Decisions

- **Kafka + RabbitMQ** for decoupled ingestion and downstream processing
- **Redis caching + SQL indexing** for read-path optimization (**20% query improvement** — resume-stated)
- **JUnit + PyTest** dual-stack testing for Java services and Python utilities
- **Containerized CI/CD** for repeatable production releases

## Future Improvements

- [ ] Expanded integration test coverage beyond 85%
- [ ] Centralized observability (metrics/tracing) across microservices
- [ ] Schema registry for Kafka event contracts
- [ ] Automated performance regression on critical SQL paths

## Contact

[LinkedIn](https://www.linkedin.com/in/ananyanagaraj/)
