from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.plantypes_docker_build_plan_build_args import PlantypesDockerBuildPlanBuildArgs


T = TypeVar("T", bound="PlantypesDockerBuildPlan")


@_attrs_define
class PlantypesDockerBuildPlan:
    """
    Attributes:
        build_args (Union[Unset, PlantypesDockerBuildPlanBuildArgs]):
        context (Union[Unset, str]):
        dockerfile (Union[Unset, str]):
        target (Union[Unset, str]):
    """

    build_args: Union[Unset, "PlantypesDockerBuildPlanBuildArgs"] = UNSET
    context: Union[Unset, str] = UNSET
    dockerfile: Union[Unset, str] = UNSET
    target: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        build_args: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.build_args, Unset):
            build_args = self.build_args.to_dict()

        context = self.context

        dockerfile = self.dockerfile

        target = self.target

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if build_args is not UNSET:
            field_dict["build_args"] = build_args
        if context is not UNSET:
            field_dict["context"] = context
        if dockerfile is not UNSET:
            field_dict["dockerfile"] = dockerfile
        if target is not UNSET:
            field_dict["target"] = target

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.plantypes_docker_build_plan_build_args import PlantypesDockerBuildPlanBuildArgs

        d = dict(src_dict)
        _build_args = d.pop("build_args", UNSET)
        build_args: Union[Unset, PlantypesDockerBuildPlanBuildArgs]
        if isinstance(_build_args, Unset):
            build_args = UNSET
        else:
            build_args = PlantypesDockerBuildPlanBuildArgs.from_dict(_build_args)

        context = d.pop("context", UNSET)

        dockerfile = d.pop("dockerfile", UNSET)

        target = d.pop("target", UNSET)

        plantypes_docker_build_plan = cls(
            build_args=build_args,
            context=context,
            dockerfile=dockerfile,
            target=target,
        )

        plantypes_docker_build_plan.additional_properties = d
        return plantypes_docker_build_plan

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
