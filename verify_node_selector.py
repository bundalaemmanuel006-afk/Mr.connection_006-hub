import os
import sys
from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        file_path = os.path.abspath('index.html')
        page.goto(f'file://{file_path}')

        # Connect hub
        hub_btn = page.locator('#hub-btn')
        hub_btn.click()

        # Wait for connection to complete
        page.wait_for_selector('#node-row', state='visible', timeout=5000)
        page.wait_for_timeout(600) # Ensure initial latency measurement completes

        sr_status = page.locator('#sr-status')
        node_select = page.locator('#node-select')

        # Test focus announcement
        node_select.focus()
        page.wait_for_timeout(100)
        status_text = sr_status.text_content()
        print("SR Status on focus:", status_text)
        assert "Gateway node selector focused" in status_text, f"Unexpected focus SR text: {status_text}"
        assert "US-East" in status_text, f"Expected US-East in focus text: {status_text}"

        # Test select change announcement
        node_select.select_option('eu')
        page.wait_for_timeout(600) # wait for latency measurement triggered on change
        status_text_after_change = sr_status.text_content()
        print("SR Status after node change:", status_text_after_change)
        assert "Latency updated" in status_text_after_change or "node EU" in status_text_after_change, f"Unexpected change SR text: {status_text_after_change}"

        # Test toast notification visual dismiss affordance
        toast = page.locator('#toast')
        assert toast.is_visible(), "Expected toast to be visible after node change"
        toast_close = page.locator('.toast-close')
        assert toast_close.is_visible(), "Expected .toast-close icon in toast notification"
        assert toast_close.get_attribute('aria-label') == "Dismiss notification"

        # Click toast to dismiss
        toast.click()
        page.wait_for_timeout(100)
        toast_class = toast.get_attribute('class') or ''
        assert "show" not in toast_class, "Expected toast to be dismissed on click"

        browser.close()
        print("All tests in verify_node_selector.py passed successfully!")

if __name__ == '__main__':
    main()
