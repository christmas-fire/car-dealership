import pytest

@pytest.mark.anyio
async def test_create_car(test_client, created_model_id):
    payload = {
        "model_id": f"{created_model_id}",
        "year": 2005,
        "generation": 2,
        "color": "Grey",
        "price": 350000,
        "mileage": 180000,
        "transmission": "Manual",
        "drive": "FWD",
        "engine_cap": 1.6,
        "engine_type": "Gasoline",
        "engine_power": 102,
        "description" : "Some test description"
    }
    response = await test_client.post(url="/cars", json=payload)
    assert response.status_code == 201
    
 
@pytest.mark.anyio
async def test_create_car_with_invalid_transmission(test_client, created_model_id):
    payload = {
        "model_id": f"{created_model_id}",
        "year": 2005,
        "generation": 2,
        "color": "Grey",
        "price": 350000,
        "mileage": 180000,
        "transmission": "Random invalid transmission",
        "drive": "FWD",
        "engine_cap": 1.6,
        "engine_type": "Gasoline",
        "engine_power": 102,
        "description" : "Some test description"
    }
    response = await test_client.post(url="/cars", json=payload)
    assert response.status_code == 422
    
    
@pytest.mark.anyio
async def test_create_car_with_invalid_drive(test_client, created_model_id):
    payload = {
        "model_id": f"{created_model_id}",
        "year": 2005,
        "generation": 2,
        "color": "Grey",
        "price": 350000,
        "mileage": 180000,
        "transmission": "Manual",
        "drive": "Random invalid drive",
        "engine_cap": 1.6,
        "engine_type": "Gasoline",
        "engine_power": 102,
        "description" : "Some test description"
    }
    response = await test_client.post(url="/cars", json=payload)
    assert response.status_code == 422
    
    
@pytest.mark.anyio
async def test_create_car_with_invalid_engine_type(test_client, created_model_id):
    payload = {
        "model_id": f"{created_model_id}",
        "year": 2005,
        "generation": 2,
        "color": "Grey",
        "price": 350000,
        "mileage": 180000,
        "transmission": "Manual",
        "drive": "FWD",
        "engine_cap": 1.6,
        "engine_type": "Random invalid engine type",
        "engine_power": 102,
        "description" : "Some test description"
    }
    response = await test_client.post(url="/cars", json=payload)
    assert response.status_code == 422
        
        
@pytest.mark.anyio
async def test_read_cars(test_client):
    response = await test_client.get("/cars")
    assert response.status_code == 200
    

@pytest.mark.parametrize(
    "payload",
    [
        pytest.param({"year": 2024}, id="update_year"),                                
        pytest.param({"color": "Black"}, id="update_color"),                           
        pytest.param({"price": 500000}, id="update_price"),                            
        pytest.param({"mileage": 100}, id="update_miliage"),                             
        pytest.param({"transmission": "Automatic"}, id="update_transmission"),                
        pytest.param({"drive": "AWD"}, id="update_drive"),                             
        pytest.param({"engine_cap": 2.0}, id="update_engine_cap"),                          
        pytest.param({"engine_type": "Diesel"}, id="update_engine_type"),                    
        pytest.param({"engine_power": 250}, id="update_engine_power"),                        
        pytest.param({"description": "Update full description"}, id="update_description"),
        pytest.param(
            {
                "year": 2022,
                "color": "Red",
                "price": 1000000,
                "mileage": 5000,
                "transmission": "Automatic",
                "drive": "RWD",
                "engine_cap": 3.0,
                "engine_type": "Electric",
                "engine_power": 450,
                "description": "Full overhaul"
            },
            id="update_all_fields"
        ),
    ],
)
@pytest.mark.anyio
async def test_update_car_fields(test_client, created_car_id, payload: dict):
    response = await test_client.patch(url=f"/cars/{created_car_id}", json=payload)
    assert response.status_code == 200
    
    for key, value in payload.items():
        assert response.json()[key] == value
        
        
@pytest.mark.parametrize(
    "payload",
    [                            
        pytest.param({"transmission": "Random invalid transmission"}, id="update_invalid_transmission"),                
        pytest.param({"drive": "Random invalid drive"}, id="update_invalid_drive"),                                                      
        pytest.param({"engine_type": "Random invalid engine type"}, id="update_invalid_engine_type"),                    
    ],
)
@pytest.mark.anyio
async def test_update_car_with_invalid_fields(test_client, created_car_id, payload: dict):
    response = await test_client.patch(url=f"/cars/{created_car_id}", json=payload)
    assert response.status_code == 422
        
        
@pytest.mark.anyio
async def test_update_car_model_id(test_client, created_model_id, created_car_id):
    payload = {
        "model_id": f"{created_model_id}",
    }
    response = await test_client.patch(url=f"/cars/{created_car_id}", json=payload)
    assert response.status_code == 200
    assert response.json()["model_id"] == f"{created_model_id}"
        
        
@pytest.mark.anyio
async def test_delete_car(test_client, created_car_id):
    response = await test_client.delete(url=f"/cars/{created_car_id}")
    assert response.status_code == 204
    