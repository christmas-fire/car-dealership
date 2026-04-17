import pytest
from httpx import AsyncClient, ASGITransport

from src.main import app
from src.models.base import Base
from src.db.session import engine

@pytest.fixture(scope="session", autouse=True)
def setup_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    
    
@pytest.fixture
async def test_client():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
        headers={"Content-Type": "application/json"},
    ) as client:
        yield client
    

@pytest.fixture()
async def created_brand_id(test_client: AsyncClient) -> str:
    response = await test_client.post("/brands", json={"name": "Temp", "country": "Temp"})
    return response.json()["id"]


@pytest.fixture()
async def created_model_id(test_client: AsyncClient, created_brand_id) -> str:
    response = await test_client.post(
        url="/models",
        json={
            "brand_id": f"{created_brand_id}",
            "name": "Temp",
            "type": "Sedan"
        }
    )
    return response.json()["id"]


@pytest.fixture()
async def created_car_id(test_client: AsyncClient, created_model_id) -> str:
    response = await test_client.post(
        url="/cars",
        json={
            "model_id": f"{created_model_id}",
            "year": 2016,
            "generation": 3,
            "color": "White",
            "price": 1000000,
            "mileage": 50000,
            "transmission": "Manual",
            "drive": "FWD",
            "engine_cap": 1.6,
            "engine_type": "Gasoline",
            "engine_power": 115,
            "description" : "Some test description"
    }
    )
    return response.json()["id"]
