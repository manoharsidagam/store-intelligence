# CHOICES.md

## AI-Assisted Engineering Decisions

This project was intentionally developed using an AI-assisted engineering workflow.

Rather than using AI only for code generation, AI was used as a design and decision-making partner throughout the development lifecycle.

The objective was to accelerate prototyping, evaluate architectural tradeoffs, improve event schema quality, and strengthen system design decisions.

---

## Why FastAPI?

Several backend frameworks were considered, including Flask and FastAPI.

### Decision

FastAPI was selected because:

* High performance ASGI framework
* Automatic OpenAPI documentation
* Built-in request validation
* Easy API testing
* Production-ready architecture

### AI Contribution

AI was used to compare FastAPI against Flask and evaluate tradeoffs for a real-time analytics platform.

Result:

FastAPI provided a cleaner and more scalable foundation for analytics APIs.

---

## Why Streamlit?

Several dashboard technologies were evaluated:

* React
* Dash
* Streamlit

### Decision

Streamlit was selected because:

* Rapid dashboard development
* Excellent data visualization support
* Built-in interactivity
* Faster iteration cycle

### AI Contribution

AI-assisted brainstorming was used to design dashboard layouts, KPI placement, funnel visualization, anomaly presentation, and executive reporting views.

Result:

Development speed increased significantly while maintaining dashboard quality.

---

## Why Docker?

### Decision

Docker was introduced to ensure:

* Consistent execution environment
* Easy deployment
* Reproducibility
* Simplified project setup

### AI Contribution

AI helped generate containerization workflows, Docker configuration strategies, dependency management approaches, and deployment validation steps.

Result:

The application can be deployed consistently across different systems.

---

## Why JSON-Based Event Storage?

Several storage options were considered:

* SQL Database
* NoSQL Database
* JSON Files

### Decision

JSON storage was selected because:

* Lightweight
* Easy debugging
* Fast prototyping
* Suitable for challenge scope

### AI Contribution

AI-assisted evaluation was used to compare implementation complexity against project requirements.

Result:

JSON enabled rapid experimentation while maintaining event traceability.

---

## Why Session-Based Funnel Analytics?

Traditional event counting can overestimate visitor journeys because a single visitor may generate multiple events.

### Decision

Session-based tracking was implemented using:

* Visitor IDs
* Session IDs
* Store IDs

### AI Contribution

AI-assisted reasoning was used to identify duplicate counting risks and design a session-deduplication strategy.

Result:

More accurate funnel analytics and conversion measurement.

---

## Why Rule-Based Anomaly Detection?

Two approaches were evaluated:

1. Machine Learning-based detection
2. Rule-based detection

### Decision

Rule-based detection was selected because:

* Transparent
* Explainable
* Easy to validate
* Suitable for operational monitoring

Examples:

* High Occupancy
* Traffic Spike
* Low Conversion
* Counting Error

### AI Contribution

AI-assisted analysis was used to identify meaningful retail operational anomalies and define detection thresholds.

Result:

Reliable anomaly detection with fully explainable outputs.

---

## Testing Strategy

Automated API testing was implemented using Pytest and FastAPI TestClient.

Tests validate:
- Health endpoint availability
- Event retrieval
- Anomaly retrieval
- Store metrics retrieval
- Invalid store handling

This ensures API reliability and reduces regression issues during future development

## Event Schema Design Decisions

The event schema evolved through multiple iterations.

Fields added through AI-assisted design reviews include:

* event_id
* session_id
* visitor_id
* track_id
* store_id
* event_version
* confidence score
* source metadata

### Result

A production-oriented event structure capable of supporting:

* Funnel Analytics
* Session Tracking
* Event Auditing
* Multi-Store Analytics
* Future Database Integration

---

## Dashboard Design Decisions

The dashboard was designed using an executive-first approach.

AI-assisted design reviews helped improve:

* KPI hierarchy
* Funnel presentation
* Health score visualization
* Anomaly visibility
* Store comparison views

### Result

A dashboard optimized for operational decision-making rather than raw metric display.

---

## AI Collaboration Workflow

AI was used throughout the project as an engineering copilot rather than a code-generation tool.

### Architecture Exploration

AI-assisted brainstorming was used to evaluate multiple system architectures, event-processing pipelines, and dashboard integration approaches before implementation.

### API Contract Validation

AI was used to review endpoint structures, response formats, schema consistency, and API usability from a consumer perspective.

### Edge Case Discovery

AI-assisted reviews helped identify potential failure scenarios including:

* Duplicate session events
* Re-entry behavior
* Empty event streams
* Invalid store requests
* Conversion funnel inconsistencies
* Missing metadata fields

These scenarios were later incorporated into testing and validation workflows.

### Test Case Generation

AI was used to generate and refine test scenarios covering:

* Health endpoint validation
* Event retrieval
* Metrics computation
* Anomaly endpoint verification
* Invalid input handling

This improved confidence in system reliability and reduced regression risk.

### Documentation Generation and Review

AI-assisted writing and review processes were used to improve:

* README structure
* DESIGN documentation
* Architectural explanations
* Deployment instructions
* Engineering decision records

### Human-in-the-Loop Approach

While AI accelerated analysis, documentation, and prototyping, all final engineering decisions, implementation choices, anomaly rules, and validation logic were reviewed and approved manually.

This ensured that the final system remained explainable, auditable, and aligned with project requirements.

## Summary

AI was used throughout the project lifecycle as an engineering copilot for:

* Architecture evaluation
* Technology selection
* Event schema design
* API design
* Funnel analytics design
* Anomaly detection logic
* Dashboard UX improvements
* Deployment strategy

The final solution combines human decision-making with AI-assisted engineering to accelerate development while maintaining transparency and explainability.
