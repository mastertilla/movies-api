# IMDb Movies Application

API backend service for a IMDb movies application
[![Python 3.12.3](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/release/python-3120/)

## Getting started

This project uses:

- [fastapi](https://fastapi.tiangolo.com/) as http framework
- [rye](https://rye.astral.sh/) as dependency manager
- [mypy](http://mypy-lang.org/) for static typing analysis
- [black](https://black.readthedocs.io/) for code formatting
- [flake8](http://flake8.pycqa.org/) for linting
- [pytest](https://docs.pytest.org/) as testing framework
- [coverage](https://coverage.readthedocs.io/) for code coverage reporting
- [pre-commit](https://pre-commit.com/) to setup git hooks (formatting and linting before commits)

```sh
# Clone the repository
git clone git@bitbucket.org:newtralmedia/chatbot-svc

# Install the dependencies using poetry
poetry install

# Setup pre commit hooks
poetry run pre-commit install
poetry run pre-commit run --all-files
```

## Configuration

The application can be configured using environment variables as well as a `.env` file (`.env.pre` for `pre` environment and `.env.dev` for `development` environment). Below there
is a list of the supported configuration. Every configuration is declared at [settings.py](./chatbot_svc/settings.py) event if it comes from the environment or is manually set.

| Variable                         | Description                                                                                                                                                                | Type                              | Required | Default               |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- | :------: | --------------------- |
| `PYTHON_ENV`                     | The environment where the app is running                                                                                                                                   | `development - production - test` |    âŒ    | `development`         |
| `JAEGER_AGENT_HOST`              | Jaeger agent host                                                                                                                                                          | `str`                             |    âŒ    | `localhost`           |
| `JAEGER_AGENT_PORT`              | Jaeger agent port                                                                                                                                                          | `int`                             |    âŒ    | `6831`                |
| `JAEGER_DISABLED`                | Disable jaeger tracing                                                                                                                                                     | `bool`                            |    âŒ    | `False`               |
| `OPENAI_API_KEY`                 | OpenAI key                                                                                                                                                                 | `str`                             |    âœ”     |                       |
| `CLIENTS_API_KEY`                | Newtral's clients managment api key                                                                                                                                        | `str`                             |    âœ”     |                       |
| `ELASTIC_BASE_URL`               | Elasticsearch enpoint                                                                                                                                                      | `str`                             |    âœ”     |                       |
| `AWS_ACCESS_KEY_ID`              | AWS key                                                                                                                                                                    | `str`                             |    âœ”     |                       |
| `AWS_SECRET_ACCESS_KEY`          | AWS secret key                                                                                                                                                             | `str`                             |    âœ”     |                       |
| `AWS_DEFAULT_REGION`             | Region Aws ES                                                                                                                                                              | `str`                             |    âœ”     |                       |
| `TOKENIZERS_PARALLELISM`         | Tokenizers parallelism                                                                                                                                                     | `str`                             |    âœ”     |                       |
| `MYSQL_HOST`                     | Mysql connection host                                                                                                                                                      | `str`                             |    âœ”     |                       |
| `MYSQL_DATABASE`                 | Mysql connection database                                                                                                                                                  | `str`                             |    âœ”     |                       |
| `MYSQL_USER`                     | Mysql connection user                                                                                                                                                      | `str`                             |    âœ”     |                       |
| `MYSQL_PASSWORD`                 | Mysql connection password                                                                                                                                                  | `str`                             |    âœ”     |                       |
| `MONGO_URI`                      | MongoDB connection URI to Normalize Database                                                                                                                               | `str`                             |    âœ”     |                       |
| `SECRET_KEY`                     | Secret key                                                                                                                                                                 | `str`                             |    âœ”     |                       |
| `USE_HISTORIAL`                  | Choose if use historial                                                                                                                                                    | `bool`                            |    âœ”     |                       |
| `K_NEIGHBOURS`                   | Total knn neighbours                                                                                                                                                       | `int`                             |    âœ”     |                       |
| `SIMILARITY_TH`                  | Similarity threshold between 0 - 1. When the `ELASTICSEARCH_SIM` is cosine similarity the `SIMILARITY_TH` = 0.55, and if the `ELASTICSEARCH_SIM` is `SIMILARITY_TH` = 0.08 | `float`                           |    âœ”     |                       |
| `ELASTICSEARCH_SIM`              | Type of similarity used: cosine similarity or dot product                                                                                                                  | `str`                             |    âœ”     |                       |
| `BARD_PROJECT_NAME`              | Name of the project in Google Cloud Platform                                                                                                                               | `str`                             |    âœ”     |                       |
| `GOOGLE_APPLICATION_CREDENTIALS` | Route to json where the credentials of GCP are stored                                                                                                                      | `str`                             |    âœ”     |                       |
| `ELASTIC_INDEX_NAME`             | Name of elastic index                                                                                                                                                      | `str`                             |    âœ”     |                       |
| `INDEX_MODEL_EMBEDDINGS`         | Type of embeddings we will read from index                                                                                                                                 | `str`                             |    âœ”     |                       |
| `VECTOR_NAME_ELASTIC`            | Field of embeddings we will read from index                                                                                                                                | `str`                             |    âœ”     |                       |
| `VECTOR_FIELD_CONTENT`           | Field of content we will read from Mongo to create the embeddings                                                                                                          | `str`                             |    âœ”     |                       |
| `YEARS`                          | Number of years used to consider an article as outdated                                                                                                                    | `int`                             |    âœ”     |                       |
| `COHERE_MODEL`                   | Rerank model for cohere                                                                                                                                                    | `str`                             |    âœ”     |                       |
| `COHERE_API_KEY`                 | Key for cohere                                                                                                                                                             | `str`                             |    âœ”     |                       |
| `RERANK`                         | If set to True the rerank will be applied.                                                                                                                                 | `bool`                            |    âœ”     |                       |
| `K_RERANK`                       | Number of final articles outputed by reranker                                                                                                                              | `int`                             |    âœ”     |                       |
| `MEDIA`                          | If want to filter by media, include list of names here. Otherwise leave empty to take all.                                                                                 | `str`                             |    âœ”     |                       |
| `AWS_S3_BUCKET`                  | AWS S3 Bucket name                                                                                                                                                         | `int`                             |    âœ”     |                       |
| `GOOGLE_FACTCHECK_TOOLS_API_KEY` | Google Factchecktools api key                                                                                                                                              | `int`                             |    âœ”     |                       |
| `S3_ENV_BUCKET`                  | S3 Bucket to store env files                                                                                                                                               | `str`                             |    âœ”     | `newtral-env-storage` |

## Running migrations and application

```sh
make run
```

The swagger can be explored at [http://localhost:8000/swagger](http://localhost:8000/swagger)

## Release

In order to generate a new release you will need:

**Node LTS**

```sh
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.37.2/install.sh | bash
nvm install lts # You may need to open a new shell
```

**[standard-version](https://www.npmjs.com/package/standard-version)**

```sh
npm install --global standard-version
```

Just run the following script. It will:

- Checkout to master
- Merge the most recent develop changes
- Update package version and create a new tag
- Push changes to master and develop
- Build and push the :latest :dev and :\$version docker images

```sh
make release
```

This `make release` is also responsible for updating the `.env` file stored in s3 with the current local `.env`. The file is stored in a folder with the name of the bitbucket repo.
For updating the `.env` for other environments (`pre`, `dev`), see section below.

## Update .env for other environments

The `.env` file is only updated automatically for the `pro` environment when running `make release`. For updating the `.env` file for other environments, you can run the following command:

```sh
make [update_env_pre | update_env_dev]
```

This command will update either `.env.pre` or `.env.dev` in the s3 bucket with the current local corresponding file. It is stored in a folder with the name of the bitbucket repo + suffix with the environment (e.g. `chatbot-ai-svc-pre`).

## Test

Run every tests

```sh
poetry run pytest
```

## Coverage

Run tests and generate a code coverage report

```sh
poetry run coverage run -m pytest
poetry run coverage report -m

# Remove a previously generated coverage reports
poetry run coverage erase
```

## Docker

### Build

#### docker_build_dev

Build an image with the tag [newtral/chatbot-svc:dev](https://hub.docker.com/repository/docker/newtral/chatbot-svc)

```sh
make docker_build_dev
```

#### docker_build_latest

Build an image with the tag [newtral/chatbot-svc:latest](https://hub.docker.com/repository/docker/newtral/chatbot-svc)

```sh
make docker_build_latest
```

#### docker_build_version

Build an image with the current version tag

```sh
make docker_build_version
```

## Push

Push to the registry a previously built image. You need to run `docker login` before pushing any
image.

```sh
make docker_push_dev
make docker_push_latest
make docker_push_version
```

## DB Migrations

Create new migration. Whenever you make changes into the models then create the revision and upgrade it, even if you remove fields from the models upgrade command will be used

```sh
alembic revision --autogenerate -m "message to identify migration"
```

Migrate all changes to the database

```sh
alembic upgrade head
```

To downgrade the recent migration simply alembic downgrade first three or four initials of your version

```sh
alembic downgrade 2a43
```