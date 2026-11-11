# Reflection: Secure User Model, Testing & CI/CD Pipeline

### 1. Key Architectural & Security Decisions

- **Password Security**: Implemented salted key derivation using bcrypt to guarantee raw user credentials never exist in plain text in the database layer.
- **Data Integrity**: Enforced strict uniqueness constraints and indexes on `username` and `email` columns via SQLAlchemy, coupled with Pydantic v2 email and password policy validation.
- **Serialization Safety**: Kept password hashes strictly isolated from public serialization schemas (`UserResponse`), preventing security leaks in API responses.

### 2. Testing & CI/CD Workflow

- **Database Integration**: Leveraged a live PostgreSQL 15 service container in GitHub Actions to run tests against an authentic SQL dialect rather than in-memory mocks.
- **Multi-Stage Delivery**: Structured an automated pipeline that gates container building and Docker Hub deployment behind unit/integration testing and vulnerability scanning.
- **Multi-Architecture Images**: Configured QEMU and Docker Buildx to cross-compile and push dual-architecture (`linux/amd64`, `linux/arm64`) images to Docker Hub.

### 3. Challenges & Resolutions

- **Postgres Authentication in CI**: Resolved database authentication mismatches between default container environments and test harness connection strings by explicitly injecting matching `DATABASE_URL` credentials.
- **Browser Dependencies**: Resolved Playwright binary compatibility on Ubuntu GitHub Actions runners by pinning to `ubuntu-22.04` and targeting Chromium dependencies directly.
- **Dependency Vulnerability Management**: Handled legacy pinned dependency warnings during Trivy container scans using target exclusions (`.trivyignore`) while keeping the build deterministic.
