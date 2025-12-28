# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Completed (2025-12-28)

**Phase A - Repository Initialization** ✅
- Git repository with main + v1 branches
- Project structure (backend/ + frontend/)
- Documentation files (README, LICENSE, CHANGELOG, ARCHITECTURE)
- .gitignore for Python, Node.js, Docker, IDE files

**Phase B - Backend Data Models** ✅
- SQLAlchemy models: Product, PriceHistory, Alert, ParserConfig
- Pydantic Settings configuration
- Database connection with pooling (PostgreSQL)
- Alembic migrations system (initial schema 001)
- Complete requirements.txt with dependencies

**Phase C - CRUD API Endpoints** ✅
- Pydantic schemas with validation
- 6 REST endpoints: list, get, create, update, delete, domains
- Pagination (page/page_size) + filtering (status, domain) + sorting
- Automatic domain extraction from URL
- HTTP status codes (200, 201, 204, 404, 400)
- CORS configured for Vue frontend

**Phase T - Docker Compose (Minimal)** ✅
- 3 services: PostgreSQL 16, Redis 7, FastAPI
- Backend Dockerfile (Python 3.12 + Playwright)
- Auto-migration on API startup
- Hot reload for development
- Health checks for dependencies
- Volume persistence for data
- QUICKSTART.md guide with curl examples
- API tested and working on http://localhost:8001

### In Progress

**Next: Phases D-M** (Backend completion)
- Phase D: Generic parser engine
- Phase E-G: Site-specific parsers (Amazon, FR sites, BE sites)
- Phase H: Parser admin API endpoints
- Phase I-J: Celery workers + scheduler
- Phase K: Price history API
- Phase L: Promo detection
- Phase M: Alert system

### Technical Details

**Database Schema:**
- products: wishlist items with tracking status
- price_history: time-series price data
- alerts: price change notifications
- parser_configs: domain-specific scraping configs (JSON selectors)

**API Endpoints:**
- GET /api/v1/products/ - List products (paginated, filtered, sorted)
- GET /api/v1/products/domains - Unique domains
- GET /api/v1/products/{id} - Single product
- POST /api/v1/products/ - Create product
- PUT /api/v1/products/{id} - Update product
- DELETE /api/v1/products/{id} - Delete product

**Infrastructure:**
- PostgreSQL with proper indexes and cascade deletes
- Redis for Celery broker and caching
- FastAPI with automatic OpenAPI documentation
- Docker Compose orchestration
