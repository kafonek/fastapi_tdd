# fastapi_tdd

This is a cookiecutter set-up for a test-driven development (TDD) FastAPI app.  Before using this one, consider the "official" [full-stack-fastapi-postgresql](https://github.com/tiangolo/full-stack-fastapi-postgresql) project by @tiangolo (creator of FastAPI).

My cookiecutter deals with a minimal subset of features that apply to apps in my own domain.  It does not include any front end code, and replaces an admin UI with Jupyter Notebooks that can interact with the production database.  It uses sqlite for the database instead of postges, and strips out several other features such as celery and email notifications.  

It also configures `docker-compose` to run three apps: the web-app, tests, and jupyter.  Source code and databases are volume mounted into each.  Any time you make a change to source code, you should see the tests run and the web-app will restart.  Restarting any Jupyter kernels and re-importing source code will similarly reflect your changes.

# Run

`git clone https://github.com/kafonek/fastapi_tdd.git`

`docker-compose down && docker-compose up --build -d && docker-compose logs -f`


