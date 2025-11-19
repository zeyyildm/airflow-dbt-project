# Airflow & DBT Data Pipeline Project

A comprehensive data engineering project that combines Apache Airflow for workflow orchestration and DBT (Data Build Tool) for data transformation. This project demonstrates a complete ETL pipeline using Docker containers for easy deployment and scalability.

## 🚀 Features

- **Apache Airflow 2.7.1**: Workflow orchestration with CeleryExecutor
- **DBT**: Data transformation and modeling with staging and marts layers
- **Docker Compose**: Containerized infrastructure for easy setup
- **PostgreSQL**: Database for Airflow metadata and data storage
- **Redis**: Message broker for Celery tasks
- **Python Scripts**: Custom data processing functions integrated with Airflow

## 📋 Project Structure

```
project/
├── airflow/
│   ├── dags/              # Airflow DAG definitions
│   │   └── ilkdagim.py    # Main DAG with data processing tasks
│   ├── logs/              # Airflow execution logs
│   └── plugins/           # Custom Airflow plugins
├── dbt/
│   ├── models/
│   │   ├── staging/       # Staging layer models
│   │   └── marts/        # Business logic models
│   ├── seeds/            # CSV seed files
│   └── profiles.yml      # DBT connection configuration
├── scripts/
│   └── data_processor.py # Python data processing functions
└── docker-compose.yml    # Docker services configuration
```

## 🛠️ Technologies

- **Apache Airflow 2.7.1**: Workflow management
- **DBT**: Data transformation
- **PostgreSQL 13**: Relational database
- **Redis 6**: Message broker
- **Docker & Docker Compose**: Containerization
- **Python**: Data processing scripts
- **Pandas**: Data manipulation

## 📦 Prerequisites

- Docker Desktop installed and running
- Docker Compose v2.0+
- At least 4GB of available RAM
- Ports 8080, 5432 available

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/zeyyildm/airflow-dbt-project.git
cd airflow-dbt-project
```

### 2. Start the Services

```bash
docker-compose up -d
```

This will start the following services:
- **PostgreSQL**: Database for Airflow metadata
- **Redis**: Message broker for Celery
- **Airflow Webserver**: Web UI on http://localhost:8080
- **Airflow Scheduler**: Task scheduler

### 3. Access Airflow Web UI

1. Open your browser and navigate to: `http://localhost:8080`
2. Default credentials:
   - Username: `airflow`
   - Password: `airflow`

### 4. View DAGs

Once logged in, you'll see the `DAG-1` workflow which includes:
- **start**: Initialization task
- **process_data**: Data processing using Python scripts
- **validate_data**: Data validation
- **delete_past**: Cleanup old records from database
- **end**: Completion task

## 📊 DBT Models

### Staging Layer
- `staging_genres`: Genre data staging
- `staging_mgenres`: Movie-genre relationships
- `staging_movies`: Movie data staging
- `staging_ratings`: Rating data staging
- `staging_user`: User data staging
- `staging_user_ratings`: User rating relationships

### Marts Layer (Business Logic)
- `most_genres`: Analysis of most common genres
- `movie_rate_avg`: Average movie ratings
- `oldest_user`: User registration analysis
- `user_activity`: User engagement metrics

## 🔧 Configuration

### Airflow Configuration
Airflow is configured with:
- **Executor**: CeleryExecutor for distributed task execution
- **Database**: PostgreSQL for metadata storage
- **Broker**: Redis for task queue management

### DBT Configuration
DBT profiles are configured in `dbt/profiles.yml`. Update connection details as needed for your database.

## 📝 DAG Workflow

The main DAG (`DAG-1`) runs daily and performs:
1. Data processing from CSV files
2. Data validation
3. Database cleanup (removes records older than 360 days)

## 🐳 Docker Services

| Service | Port | Description |
|---------|------|-------------|
| Airflow Webserver | 8080 | Web UI for monitoring DAGs |
| PostgreSQL | 5432 | Database server |
| Redis | 6379 | Message broker |

## 📂 Data Sources

The project includes sample CSV seed files in `dbt/seeds/`:
- `genres.csv`
- `movie_genres.csv`
- `movies.csv`
- `user_ratings.csv`
- `users.csv`

## 🔍 Monitoring

- **Airflow UI**: Monitor DAG runs, task status, and logs at http://localhost:8080
- **Logs**: Check `airflow/logs/` for detailed execution logs
- **DBT Logs**: View DBT execution logs in `dbt/logs/`

## 🛑 Stopping the Services

```bash
docker-compose down
```

To remove volumes (⚠️ this will delete all data):

```bash
docker-compose down -v
```

## 📚 Key Components

### Airflow DAG
The DAG (`airflow/dags/ilkdagim.py`) orchestrates:
- Python-based data processing tasks
- PostgreSQL database operations
- Task dependencies and scheduling

### Python Scripts
Custom data processing functions in `scripts/data_processor.py`:
- `process_data()`: Main data processing logic
- `validate_data()`: Data quality validation

### DBT Models
Transform raw data through staging to marts layers following data modeling best practices.

## 📄 License

This project is open source and available for educational purposes.

## 👤 Author

**Zeynep Yıldırım**
- GitHub: [@zeyyildm](https://github.com/zeyyildm)


---

⭐ If you find this project helpful, please consider giving it a star!
