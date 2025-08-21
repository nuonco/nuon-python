# GetInstallActionWorkflowsLatestRunsRequest


## Fields

| Field                                      | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `install_id`                               | *str*                                      | :heavy_check_mark:                         | install ID                                 |
| `trigger_types`                            | *Optional[str]*                            | :heavy_minus_sign:                         | filter by action workflow trigger by types |
| `offset`                                   | *Optional[int]*                            | :heavy_minus_sign:                         | offset of results to return                |
| `limit`                                    | *Optional[int]*                            | :heavy_minus_sign:                         | limit of results to return                 |
| `page`                                     | *Optional[int]*                            | :heavy_minus_sign:                         | page number of results to return           |
| `q`                                        | *Optional[str]*                            | :heavy_minus_sign:                         | search query for action workflow name      |
| `x_nuon_pagination_enabled`                | *Optional[bool]*                           | :heavy_minus_sign:                         | Enable pagination                          |