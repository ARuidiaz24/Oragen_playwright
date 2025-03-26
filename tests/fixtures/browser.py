import pytest
from playwright.sync_api import sync_playwright
import os
import shutil

@pytest.fixture(scope="function")
def browser(request):
    testcase_name = request.node.name

    if testcase_name.startswith("test_login"):
        subdir = "test_login"
    elif testcase_name.startswith("test_resetPass"):
        subdir = "test_resetPass"
    else:
        subdir = "other"

    video_dir = f"videos/{subdir}"
    os.makedirs(video_dir, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        ## yield browser
        ## browser.close()
        context = browser.new_context(
            record_video_dir = video_dir,
            record_video_size = {"width": 1280, "height": 720}
        )
        yield context
        context.close()
        browser.close()