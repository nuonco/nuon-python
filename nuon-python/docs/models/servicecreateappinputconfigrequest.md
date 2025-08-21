# ServiceCreateAppInputConfigRequest


## Fields

| Field                                                                           | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `app_config_id`                                                                 | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | N/A                                                                             |
| `groups`                                                                        | Dict[str, [models.ServiceAppGroupRequest](../models/serviceappgrouprequest.md)] | :heavy_check_mark:                                                              | N/A                                                                             |
| `inputs`                                                                        | Dict[str, [models.ServiceAppInputRequest](../models/serviceappinputrequest.md)] | :heavy_check_mark:                                                              | N/A                                                                             |