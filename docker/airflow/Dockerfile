FROM apache/airflow:2.7.0-python3.9

ENV PATH="/usr/local/bin:$PATH"
ENV PATH="/home/airflow/.local/bin:$PATH"

ARG AIRFLOW_VERSION=2.7.0
ARG PYTHON_VERSION=3.9

COPY requirements.txt .
COPY constraints-3.9.txt .

ENV PIP_NO_USER=1

RUN pip install --upgrade pip && \
    # pip install --no-cache-dir -r requirements.txt --constraint constraints-3.9.txt && \
    pip install --no-cache-dir feast[cli] --user   && \ 
    pip install --no-cache-dir --upgrade --force-reinstall "email-validator>=2.0" --user
# RUN rm -rf /home/airflow/.local





