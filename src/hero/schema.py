from pydantic import ConfigDict, RootModel

from src.common.base_model import CustomBaseModel


class GetHeroSchema(CustomBaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)


ListHeroSchema = RootModel[list[GetHeroSchema]]


class CreateHeroSchema(CustomBaseModel):
    name: str
