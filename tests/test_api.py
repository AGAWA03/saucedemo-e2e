import pytest
from playwright.sync_api import APIRequestContext, Playwright

BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.fixture(scope="session")
def api(playwright: Playwright):
    context = playwright.request.new_context(base_url=BASE_URL)
    yield context
    context.dispose()


@pytest.mark.smoke
def test_get_posts_returns_list(api: APIRequestContext):
    response = api.get("/posts")
    assert response.status == 200
    assert len(response.json()) == 100


@pytest.mark.regression
def test_get_single_post(api: APIRequestContext):
    response = api.get("/posts/1")
    assert response.ok
    body = response.json()
    assert body["id"] == 1
    assert "title" in body


@pytest.mark.regression
def test_get_nonexistent_post_returns_404(api: APIRequestContext):
    response = api.get("/posts/99999")
    assert response.status == 404


@pytest.mark.regression
def test_create_post(api: APIRequestContext):
    payload = {"title": "QA test", "body": "created by automation", "userId": 1}
    response = api.post("/posts", data=payload)
    assert response.status == 201
    body = response.json()
    assert body["title"] == payload["title"]
    assert "id" in body


@pytest.mark.regression
def test_update_post(api: APIRequestContext):
    payload = {"id": 1, "title": "updated", "body": "changed", "userId": 1}
    response = api.put("/posts/1", data=payload)
    assert response.ok
    assert response.json()["title"] == "updated"


@pytest.mark.regression
def test_delete_post(api: APIRequestContext):
    response = api.delete("/posts/1")
    assert response.ok


@pytest.mark.regression
def test_posts_filtered_by_user(api: APIRequestContext):
    response = api.get("/posts", params={"userId": 1})
    assert response.ok
    posts = response.json()
    assert len(posts) > 0
    assert all(post["userId"] == 1 for post in posts)
