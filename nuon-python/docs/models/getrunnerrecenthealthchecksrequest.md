# GetRunnerRecentHealthChecksRequest


## Fields

| Field                             | Type                              | Required                          | Description                       |
| --------------------------------- | --------------------------------- | --------------------------------- | --------------------------------- |
| `runner_id`                       | *str*                             | :heavy_check_mark:                | runner ID                         |
| `window`                          | *Optional[str]*                   | :heavy_minus_sign:                | window of health checks to return |
| `offset`                          | *Optional[int]*                   | :heavy_minus_sign:                | offset of results to return       |
| `limit`                           | *Optional[int]*                   | :heavy_minus_sign:                | limit of results to return        |
| `page`                            | *Optional[int]*                   | :heavy_minus_sign:                | page number of results to return  |
| `x_nuon_pagination_enabled`       | *Optional[bool]*                  | :heavy_minus_sign:                | Enable pagination                 |