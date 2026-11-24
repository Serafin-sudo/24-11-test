from app import app


def test_health():
    client = app.test_client()
    risposta = client.get("/health")
    assert risposta.status_code == 200
    assert risposta.get_json() == {"status": "ok"}
