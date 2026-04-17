import pytest

@pytest.mark.anyio
async def test_create_brands(test_client):
    payload = {
        "name": "Test brand",
        "country": "Test country",
    }
    response = await test_client.post(url="/brands", json=payload)
    assert response.status_code == 201
        
        
@pytest.mark.anyio
async def test_read_brands(test_client):
    response = await test_client.get("/brands")
    assert response.status_code == 200
        

@pytest.mark.anyio
async def test_update_brand_name(test_client, created_brand_id):
    payload = {
        "name": "Test update name",
    }
    response = await test_client.patch(url=f"/brands/{created_brand_id}", json=payload)
    assert response.status_code == 200
    assert response.json()["name"] == "Test update name"
    
    
@pytest.mark.anyio
async def test_update_brand_country(test_client, created_brand_id):
    payload = {
        "country": "Test update country",
    }
    response = await test_client.patch(url=f"/brands/{created_brand_id}", json=payload)
    assert response.status_code == 200
    assert response.json()["country"] == "Test update country"


@pytest.mark.anyio
async def test_update_brand(test_client, created_brand_id):
    payload = {
        "name": "Test update name",
        "country": "Test update country",
    }
    response = await test_client.patch(url=f"/brands/{created_brand_id}", json=payload)
    assert response.status_code == 200
    assert (response.json()["name"] == "Test update name") and \
           (response.json()["country"] == "Test update country")
        
        
@pytest.mark.anyio
async def test_delete_brand(test_client, created_brand_id):
    response = await test_client.delete(url=f"/brands/{created_brand_id}")
    assert response.status_code == 204
    