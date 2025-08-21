# AppOtelLogRecord


## Fields

| Field                       | Type                        | Required                    | Description                 |
| --------------------------- | --------------------------- | --------------------------- | --------------------------- |
| `body`                      | *Optional[str]*             | :heavy_minus_sign:          | N/A                         |
| `created_at`                | *Optional[str]*             | :heavy_minus_sign:          | N/A                         |
| `created_by_id`             | *Optional[str]*             | :heavy_minus_sign:          | N/A                         |
| `id`                        | *Optional[str]*             | :heavy_minus_sign:          | N/A                         |
| `log_attributes`            | Dict[str, *str*]            | :heavy_minus_sign:          | N/A                         |
| `log_stream_id`             | *Optional[str]*             | :heavy_minus_sign:          | N/A                         |
| `org_id`                    | *Optional[str]*             | :heavy_minus_sign:          | internal attributes         |
| `resource_attributes`       | Dict[str, *str*]            | :heavy_minus_sign:          | N/A                         |
| `resource_schema_url`       | *Optional[str]*             | :heavy_minus_sign:          | N/A                         |
| `runner_group_id`           | *Optional[str]*             | :heavy_minus_sign:          | N/A                         |
| `runner_id`                 | *Optional[str]*             | :heavy_minus_sign:          | N/A                         |
| `runner_job_execution_id`   | *Optional[str]*             | :heavy_minus_sign:          | N/A                         |
| `runner_job_execution_step` | *Optional[str]*             | :heavy_minus_sign:          | N/A                         |
| `runner_job_id`             | *Optional[str]*             | :heavy_minus_sign:          | N/A                         |
| `scope_attributes`          | Dict[str, *str*]            | :heavy_minus_sign:          | N/A                         |
| `scope_name`                | *Optional[str]*             | :heavy_minus_sign:          | N/A                         |
| `scope_schema_url`          | *Optional[str]*             | :heavy_minus_sign:          | N/A                         |
| `scope_version`             | *Optional[str]*             | :heavy_minus_sign:          | N/A                         |
| `service_name`              | *Optional[str]*             | :heavy_minus_sign:          | N/A                         |
| `severity_number`           | *Optional[int]*             | :heavy_minus_sign:          | N/A                         |
| `severity_text`             | *Optional[str]*             | :heavy_minus_sign:          | N/A                         |
| `span_id`                   | *Optional[str]*             | :heavy_minus_sign:          | N/A                         |
| `timestamp`                 | *Optional[str]*             | :heavy_minus_sign:          | OTEL log message attributes |
| `timestamp_date`            | *Optional[str]*             | :heavy_minus_sign:          | N/A                         |
| `timestamp_time`            | *Optional[str]*             | :heavy_minus_sign:          | N/A                         |
| `trace_flags`               | *Optional[int]*             | :heavy_minus_sign:          | N/A                         |
| `trace_id`                  | *Optional[str]*             | :heavy_minus_sign:          | N/A                         |
| `updated_at`                | *Optional[str]*             | :heavy_minus_sign:          | N/A                         |