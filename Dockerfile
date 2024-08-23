FROM mcr.microsoft.com/devcontainers/python:1-3.12-bookworm

EXPOSE 8000

RUN pip install "fastapi[standard]"

COPY * .

CMD fastapi dev main.py

