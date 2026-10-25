from fastapi.testclient import TestClient

from app import main



def _app_with_db_state(monkeypatch, reachable: bool):
    monkeypatch.setenv("DATABASE_URL", "postgresql+psycopg://u:p@localhost:5432/test")
    from app.config import get_settings

    get_settings.cache_clear()
    monkeypatch.setattr(main, "check_database", lambda _engine: reachable)
    return main.create_app()


def test_health_reports_up_when_database_reachable(monkeypatch):
    app = _app_with_db_state(monkeypatch, reachable=True)
    with TestClient(app) as client:
        response = client.get("/health")
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "ok"
    assert body["database"] == "up"


def test_health_reports_degraded_when_database_unreachable(monkeypatch):
    app = _app_with_db_state(monkeypatch, reachable=False)
    with TestClient(app) as client:
        response = client.get("/health")
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "degraded"
    assert body["database"] == "down"
