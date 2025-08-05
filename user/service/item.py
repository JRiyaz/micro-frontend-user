from uuid import UUID

from ..model.item import Item, Tag
from ..utils.constants import DEFAULT_ITEMS


class ItemService:
    def __init__(self):
        self._items = []
        for data in DEFAULT_ITEMS:
            data["tags"] = {Tag(tag) for tag in data["tags"]}  # Convert string to Tag enum
            self._items.append(Item(**data))

    def __add_items_to_user(self):
        items: list[Item] = self._items[0:10]
        for item in items:
            pass

    def get_items(self, skip: int, limit: int, price: float, tag: Tag | None) -> list[Item]:
        items: list[Item] = self._items[skip:limit]
        if tag:
            items = [item for item in items if tag in item.tags]
        if price > 0.0:
            items = [item for item in items if item.price <= price]
        return items

    def get_item(self, item_id: UUID) -> Item | None:
        for item in self._items:
            if item.id == item_id:
                return item
        return None
