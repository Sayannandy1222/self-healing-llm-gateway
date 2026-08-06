# System Components

## Overview

The Self-Healing LLM Gateway follows Clean Architecture and Hexagonal Architecture principles.

Each component has a single responsibility and communicates through well-defined interfaces.

---

# High-Level Components

Client
↓

API Layer
↓

Application Layer
↓

Domain Layer
↓

Provider Layer
↓

Infrastructure Layer

---

# API Layer

Responsibilities

- Accept HTTP requests
- Request validation
- Authentication
- Response serialization
- Exception handling
- API versioning

Technologies

- FastAPI
- Pydantic

---

# Application Layer

Responsibilities

- Execute business use cases
- Coordinate workflows
- Call domain services
- Orchestrate providers

Examples

- Chat Completion
- Retry Execution
- Provider Routing

---

# Domain Layer

Responsibilities

Contains pure business rules.

No dependency on:

- FastAPI
- Redis
- PostgreSQL
- Groq
- Docker

Examples

- Routing Policies
- Token Accounting
- Cost Estimation
- Provider Selection Rules

---

# Provider Layer

Responsibilities

Communicate with external LLM providers.

Initial Provider

- Groq

Future Providers

- OpenAI
- Anthropic
- Gemini
- Ollama

Responsibilities

- Prompt execution
- Streaming
- Error translation
- Response normalization

---

# Infrastructure Layer

Responsibilities

External dependencies.

Includes

- PostgreSQL
- Redis
- Logging
- Configuration
- Metrics
- Tracing

---

# Repository Layer

Responsibilities

Database access.

No business logic.

Only persistence.

---

# Telemetry Layer

Responsibilities

- Structured logging
- Metrics
- Tracing
- Request IDs
- Correlation IDs

---

# Configuration Layer

Responsibilities

Centralized application configuration.

Examples

- Environment Variables
- API Keys
- Database URLs
- Redis URLs
- Timeout Configuration

---

# Security Layer

Responsibilities

- API Key Authentication
- JWT-ready Authentication
- Security Headers
- Input Validation
- Rate Limiting

---

# Monitoring Layer

Responsibilities

Expose

- Health Endpoint
- Readiness Endpoint
- Liveness Endpoint
- Prometheus Metrics

---

# Cache Layer

Technology

Redis

Responsibilities

- Prompt Cache
- Response Cache
- TTL Management

---

# Database Layer

Technology

PostgreSQL

Responsibilities

- Audit Logs
- Request History
- Usage Statistics
- Token Records

---

# Future Components

- Model Registry
- Prompt Versioning
- Cost Dashboard
- Admin Dashboard
- Usage Analytics
- Multi-Tenant Support
- Distributed Rate Limiter