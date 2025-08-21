# GetInstallComponentsSummaryRequest


## Fields

| Field                            | Type                             | Required                         | Description                      |
| -------------------------------- | -------------------------------- | -------------------------------- | -------------------------------- |
| `install_id`                     | *str*                            | :heavy_check_mark:               | install ID                       |
| `types`                          | *Optional[str]*                  | :heavy_minus_sign:               | component types to filter by     |
| `offset`                         | *Optional[int]*                  | :heavy_minus_sign:               | offset of results to return      |
| `limit`                          | *Optional[int]*                  | :heavy_minus_sign:               | limit of results to return       |
| `page`                           | *Optional[int]*                  | :heavy_minus_sign:               | page number of results to return |
| `q`                              | *Optional[str]*                  | :heavy_minus_sign:               | search query for component name  |
| `x_nuon_pagination_enabled`      | *Optional[bool]*                 | :heavy_minus_sign:               | Enable pagination                |