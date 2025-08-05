from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, HTTPException, Query

from ..model.generic import Message
from ..model.item import Item, ItemsResponse, Tag
from ..service.item import service as item_service

item_routes = APIRouter(tags=["item"])


@item_routes.get("/items", response_model=ItemsResponse, responses={404: {"model": Message}})
async def get_items(
    skip: Annotated[int, Query(ge=0)] = 0,
    limit: Annotated[int, Query(ge=1)] = 100,
    price: Annotated[float, Query(ge=0.0)] = 0.0,
    tag: Tag | None = None,
):
    items: list[Item] = item_service.get_items(skip, limit, price, tag)
    return {"items": items, "count": len(items)}


@item_routes.get("/items/{item_id}", response_model=Item, responses={404: {"model": Message}})
async def get_item(item_id: UUID):
    item: Item = item_service.get_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
