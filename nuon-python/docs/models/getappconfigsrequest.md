# GetAppConfigsRequest


## Fields

| Field                            | Type                             | Required                         | Description                      |
| -------------------------------- | -------------------------------- | -------------------------------- | -------------------------------- |
| `app_id`                         | *str*                            | :heavy_check_mark:               | app ID                           |
| `offset`                         | *Optional[int]*                  | :heavy_minus_sign:               | offset of jobs to return         |
| `limit`                          | *Optional[int]*                  | :heavy_minus_sign:               | limit of jobs to return          |
| `page`                           | *Optional[int]*                  | :heavy_minus_sign:               | page number of results to return |
| `x_nuon_pagination_enabled`      | *Optional[bool]*                 | :heavy_minus_sign:               | Enable pagination                |