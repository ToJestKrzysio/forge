from fastapi import APIRouter, status

from src.common.schemas import MessageResponse

router = APIRouter(prefix="/health")

@router.get(
    "/",
    tags=["healthcheck"],
    summary="Perform a Health Check",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
    response_model=MessageResponse,
)
def get_health() -> MessageResponse:
    return MessageResponse(message="OK")