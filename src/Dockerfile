ARG VERSION=3.9.2

FROM python:${VERSION}-buster as builder

RUN python3 -m venv /opt/venv

COPY requirements.txt /tmp/requirements.txt
RUN /opt/venv/bin/python -m pip install \
    -r /tmp/requirements.txt \
    --no-cache-dir \
    --disable-pip-version-check

FROM python:${VERSION}-slim-buster as runtime
COPY --from=builder /opt/venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /usr/src/app

COPY entrypoint.sh /bin/entrypoint
COPY app ./app
ENTRYPOINT [ "entrypoint" ]
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0"]