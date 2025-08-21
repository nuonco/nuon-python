# ServiceCreateAppStackConfigRequest


## Fields

| Field                                            | Type                                             | Required                                         | Description                                      |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `app_config_id`                                  | *str*                                            | :heavy_check_mark:                               | N/A                                              |
| `description`                                    | *str*                                            | :heavy_check_mark:                               | N/A                                              |
| `name`                                           | *str*                                            | :heavy_check_mark:                               | N/A                                              |
| `runner_nested_template_url`                     | *Optional[str]*                                  | :heavy_minus_sign:                               | N/A                                              |
| `type`                                           | [models.AppStackType](../models/appstacktype.md) | :heavy_check_mark:                               | N/A                                              |
| `vpc_nested_template_url`                        | *Optional[str]*                                  | :heavy_minus_sign:                               | N/A                                              |