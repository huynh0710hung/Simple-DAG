FROM quay.io/astronomer/astro-runtime:8.5.0

# Install dbt-snowflake globally
RUN pip install --no-cache-dir dbt-snowflake



