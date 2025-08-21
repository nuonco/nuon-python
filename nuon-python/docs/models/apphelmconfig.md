# AppHelmConfig


## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `chart_name`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `namespace`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `storage_driver`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `take_ownership`                                                    | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Newer fields that we don't need to store as columns in the database |
| `values`                                                            | Dict[str, *str*]                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `values_files`                                                      | List[*str*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |