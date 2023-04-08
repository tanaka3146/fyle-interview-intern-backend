def test_server_up(client) :
    response = client.get(
        "/"
    )

    assert response.status_code == 200

    status = response.json["status"]
    assert status == "ready"

def test_invalid_route(client) :
    response = client.get(
        "/invalid/route"
    )

    assert response.status_code == 404

    error = response.json["error"]
    assert error == "NotFound"

def test_principal_authentication(client) :
    response = client.get(
        "/student/assignments"
    )

    assert response.status_code == 401

    error = response.json["error"]
    message = response.json["message"]

    assert error == "FyleError"
    assert message == "principal not found"


def test_api_access_cross(client,h_teacher_1) :
    response = client.get(
        '/student/assignments',
        headers=h_teacher_1
    )

    assert response.status_code == 403

    error = response.json["error"]
    assert error == "FyleError"