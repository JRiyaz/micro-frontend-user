from datetime import datetime
from enum import Enum
from uuid import UUID, uuid4

from pydantic import BaseModel, Field
from pydantic.json_schema import SkipJsonSchema


class Tag(str, Enum):
    ELECTRONICS = "Electronics"
    BOOKS = "Books"
    CLOTHING = "Clothing"
    HOME = "Home"
    TOYS = "Toys"
    SPORTS = "Sports"
    BEAUTY = "Beauty"
    AUTOMOTIVE = "Automotive"
    GROCERY = "Grocery"
    FURNITURE = "Furniture"
    MUSIC = "Music"
    OFFICE = "Office Supplies"
    PETS = "Pet Supplies"
    GARDEN = "Garden"
    HEALTH = "Health"
    JEWELRY = "Jewelry"
    SHOES = "Shoes"
    BABY = "Baby Products"
    VIDEO_GAMES = "Video Games"
    MOVIES = "Movies & TV"
    OUTDOORS = "Outdoors"


class Item(BaseModel):
    id: SkipJsonSchema[UUID] = Field(uuid4())
    name: str = Field(min_length=3, max_length=64)
    price: float = Field(gt=0.0)
    quantity: int = Field(gt=0)
    tags: list[Tag] = Field(default_factory=list, exclude=True)


class ItemsBought(BaseModel):
    id: UUID
    quantity: int = Field(gt=0)
    date: datetime = datetime.now()


class ItemsResponse(BaseModel):
    items: list[Item]
    count: int
