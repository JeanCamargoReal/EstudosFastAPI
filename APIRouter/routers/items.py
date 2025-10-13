from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def read_items():
    return [{"name": "Plumbus"}, {"name", "Portal Gun"}]


@router.get("/{item_id}")
async def read_item(item_id: int):
    return {"name": "Item", "item_id": item_id}
