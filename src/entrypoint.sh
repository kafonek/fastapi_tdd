#!/bin/bash
mkdir -p db
alembic upgrade head

exec "$@"