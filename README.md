# Price Tracker - Wishlist & Price Monitoring

A self-hosted, mono-user price tracking application for personal use. Monitor your wishlist items across multiple e-commerce platforms and get notified when prices drop.

![Python](https://img.shields.io/badge/python-3.12-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104-green.svg)
![Vue.js](https://img.shields.io/badge/Vue.js-3.4-brightgreen.svg)
![Docker](https://img.shields.io/badge/Docker-Compose-blue.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## Features

- **Wishlist Management**: Add products from any e-commerce website with URLs
- **Automated Price Tracking**: Regular scraping with Celery workers
- **Price History**: Track price evolution over time with charts
- **Smart Alerts**: Get notified when prices drop below your target
- **Multi-Platform Support**: Generic parser system configurable per domain
- **Self-Hosted**: Complete control over your data on your own VPS
- **No Authentication Required**: Designed for personal, local use

## Architecture

### Backend
- **FastAPI**: High-performance REST API
- **PostgreSQL**: Robust data persistence
- **Celery**: Distributed task queue for scraping jobs
- **Redis**: Message broker and caching layer
- **Playwright + BeautifulSoup**: Powerful web scraping capabilities
- **SQLAlchemy**: ORM with Alembic migrations

### Frontend
- **Vue 3**: Modern, reactive UI framework
- **Vite**: Lightning-fast development and build tool
- **TailwindCSS**: Utility-first styling
- **Pinia**: State management
- **Chart.js**: Price history visualization

### Workers
- **Celery Beat**: Scheduled scraping tasks
- **Celery Workers**: Parallel scraping execution
- **Generic Parser Engine**: Configurable CSS/XPath selectors per domain

## Quick Start

### Prerequisites

- Docker & Docker Compose
- Git
- Ports 8000 (API), 5173 (Frontend), 5432 (PostgreSQL), 6379 (Redis)

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd price-tracker
git checkout v1  # Development branch
```

2. Configure environment variables:
```bash
cp backend/.env.example backend/.env
# Edit backend/.env with your configuration
```

3. Launch with Docker Compose:
```bash
docker-compose up -d
```

4. Access the application:
- Frontend: http://localhost:5173
- API Docs: http://localhost:8000/docs
- API Health: http://localhost:8000/health

### Development

Stop services:
```bash
docker-compose down
```

View logs:
```bash
docker-compose logs -f
```

Rebuild after changes:
```bash
docker-compose up -d --build
```

## Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| API Framework | FastAPI | REST API with automatic OpenAPI docs |
| Database | PostgreSQL | Relational data storage |
| ORM | SQLAlchemy | Database models and queries |
| Migrations | Alembic | Database schema versioning |
| Task Queue | Celery | Asynchronous scraping jobs |
| Message Broker | Redis | Celery backend and caching |
| Scraping | Playwright + BeautifulSoup | Dynamic and static page scraping |
| Frontend Framework | Vue 3 (Composition API) | Reactive UI |
| Build Tool | Vite | Fast dev server and bundler |
| Styling | TailwindCSS | Utility-first CSS |
| State Management | Pinia | Vue state management |
| Charts | Chart.js | Price history visualization |
| Containerization | Docker + Docker Compose | Service orchestration |

## Branching Strategy

- `main`: Production-ready code (stable releases)
- `v1`: Active development branch (MVP features)
- Feature branches: `feature/<name>` merged into `v1`

## Roadmap (MVP)

### Phase A: Repository Initialization
- [x] Git repository setup
- [x] Project structure
- [x] Documentation files

### Phase B: Backend Foundation
- [ ] FastAPI application skeleton
- [ ] Database models (Product, PriceHistory, Alert)
- [ ] Basic CRUD endpoints
- [ ] PostgreSQL integration with Alembic

### Phase C: Parser Engine
- [ ] Generic parser architecture
- [ ] Domain-specific configurations (JSON/YAML)
- [ ] Playwright integration
- [ ] BeautifulSoup fallback

### Phase D: Celery Workers
- [ ] Celery configuration
- [ ] Scraping tasks
- [ ] Periodic scheduling (Celery Beat)
- [ ] Error handling and retries

### Phase E: Frontend Application
- [ ] Vue 3 project setup with Vite
- [ ] TailwindCSS configuration
- [ ] Product listing and detail views
- [ ] Price history charts
- [ ] Wishlist management UI

### Phase F: Integration & Testing
- [ ] API integration
- [ ] End-to-end testing
- [ ] Performance optimization

### Phase G: Deployment
- [ ] Docker Compose production configuration
- [ ] VPS deployment guide
- [ ] Backup and monitoring setup

## Contributing

This is a personal project, but contributions are welcome!

### Commit Guidelines
- Use atomic commits (one logical change per commit)
- Write clear, descriptive commit messages
- Follow conventional commits format: `type(scope): message`
  - Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`
  - Example: `feat(parser): add Amazon product scraper`

### Development Workflow
1. Create feature branch from `v1`
2. Implement changes with tests
3. Submit pull request to `v1`
4. Code review and merge

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Project Status

Currently in MVP development (v1 branch). Not production-ready.
