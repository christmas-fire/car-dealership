import pytest

@pytest.mark.anyio
async def test_create_model(test_client, created_brand_id):
    payload = {
        "brand_id": f"{created_brand_id}",
        "name": "Accent",
        "type": "Sedan",
    }
    response = await test_client.post(url="/models", json=payload)
    assert response.status_code == 201
        
        
@pytest.mark.anyio
async def test_read_models(test_client):
    response = await test_client.get("/models")
    assert response.status_code == 200
    
    
@pytest.mark.anyio
async def test_update_model_brand_id(test_client, created_brand_id, created_model_id):
    payload = {
        "brand_id": f"{created_brand_id}",
    }
    response = await test_client.patch(url=f"/models/{created_model_id}", json=payload)
    assert response.status_code == 200
    assert response.json()["brand_id"] == f"{created_brand_id}"
    
    
@pytest.mark.anyio
async def test_update_model_name(test_client, created_model_id):
    payload = {
        "name": "Sonata",
    }
    response = await test_client.patch(url=f"/models/{created_model_id}", json=payload)
    assert response.status_code == 200
    assert response.json()["name"] == "Sonata"
    
    
@pytest.mark.anyio
async def test_update_model_type(test_client, created_model_id):
    payload = {
        "type": "Coupe",
    }
    response = await test_client.patch(url=f"/models/{created_model_id}", json=payload)
    assert response.status_code == 200
    assert response.json()["type"] == "Coupe"
    
    
@pytest.mark.anyio
async def test_update_model_type_with_invalid_type(test_client, created_model_id):
    payload = {
        "type": "Random invalid type",
    }
    response = await test_client.patch(url=f"/models/{created_model_id}", json=payload)
    assert response.status_code == 422
    
        
@pytest.mark.anyio
async def test_update_model(test_client, created_brand_id, created_model_id):
    payload = {
        "brand_id": f"{created_brand_id}",
        "name": "Elantra",
        "type": "Hatchback"
    }
    response = await test_client.patch(url=f"/models/{created_model_id}", json=payload)
    assert response.status_code == 200
    assert (response.json()["brand_id"] == f"{created_brand_id}") and \
           (response.json()["name"] == "Elantra") and \
           (response.json()["type"] == "Hatchback")
    
        
@pytest.mark.anyio
async def test_delete_model(test_client, created_model_id):
    response = await test_client.delete(url=f"/models/{created_model_id}")
    assert response.status_code == 204
    