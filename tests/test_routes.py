from app.models.planet import Planet
def test_get_all_planets_with_no_records(client):
    # act
    response = client.get("/planets")
    response_body = response.get_json()

    # assert
    assert response.status_code == 200
    assert response_body == []

# test 1
def test_get_one_planet_returns_planet(client, one_saved_planet):
    # act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # assert
    assert response.status_code == 200
    assert response_body["id"] == one_saved_planet.id
    assert response_body["name"] == one_saved_planet.name
    assert response_body["description"] == one_saved_planet.description
    assert response_body["size"] == one_saved_planet.size

# test 2
def test_get_planet_with_no_data_returns_404(client):
    # act
    response = client.get("planets/1")

    # assert
    assert response.status_code == 404

# test 3
def test_get_all_planets_with_two_records(client, two_saved_planets):
    # act
    response = client.get("/planets")
    response_body = response.get_json()

    # assert
    assert response.status_code == 200
    assert len(response_body) == 2
    assert response_body[0] == {
        "id": 1,
        "name": "Jupiter",
        "description": "The fifth planet form the sun.",
        "size": "large"
    }
    assert response_body[1] == {
        "id": 2,
        "name": "Saturn",
        "description": "The ringed planet.",
        "size": "large"
    }

# test 4
def test_create_planet_with_valid_data(client):
    # arrange
    EXPECTED_PLANET = {
        "name": "pluto",
        "description": "The last planet.",
        "size": "tiny"
    }

    # act
    response = client.post("/planets", json=EXPECTED_PLANET)
    response_body = response.get_data(as_text=True)
    actual_planet = Planet.query.get(1)

    # assert
    assert response.status_code == 201
    assert response_body == f"Planet {EXPECTED_PLANET['name']} successfully created"
    assert actual_planet.name == EXPECTED_PLANET["name"]
    assert actual_planet.description == EXPECTED_PLANET["description"]
    assert actual_planet.size == EXPECTED_PLANET["size"]