import asyncio
import os
from playwright.async_api import async_playwright

async def run_verification():
    print("Initializing Playwright...")
    async with async_playwright() as p:
        # Launch browser headlessly
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={"width": 800, "height": 600})
        page = await context.new_page()

        # Load the index.html page using a file:// URL
        html_path = os.path.abspath("index.html")
        file_url = f"file://{html_path}"
        print(f"Loading page: {file_url}")
        await page.goto(file_url)

        # 1. Verify title
        title = await page.title()
        print(f"Page title is: '{title}'")
        assert title == "Mr.connection_006-hub", "Page title mismatch!"

        # 2. Check theme-toggle button exists
        theme_btn = page.locator("#theme-toggle")
        await theme_btn.wait_for(state="visible")
        print("Theme toggle button is visible.")

        # 3. Check shortcuts panel is initially hidden
        shortcuts_panel = page.locator("#shortcuts-panel")
        assert await shortcuts_panel.get_attribute("aria-hidden") == "true", "Shortcuts help panel should be hidden by default"

        # 4. Trigger connection by pressing key 'H'
        print("Pressing key 'H' to connect...")
        await page.keyboard.press("h")

        # Verify title transition to "Connecting..."
        connecting_title = await page.title()
        print(f"Title during connection: '{connecting_title}'")
        assert "Connecting..." in connecting_title, "Title during connection transition mismatch!"

        # Wait for the transition to finish and 'node-row' to become visible
        node_row = page.locator("#node-row")
        print("Waiting for connection sequence and node-row to display...")
        await node_row.wait_for(state="visible", timeout=5000)

        # Verify title becomes "Connected"
        connected_title = await page.title()
        print(f"Title after connection: '{connected_title}'")
        assert "Connected" in connected_title, "Title after connection mismatch!"

        # Verify dropdown select exists and default value is 'us'
        node_select = page.locator("#node-select")
        assert await node_select.is_visible(), "Gateway Node Selector select element is not visible!"
        selected_val = await node_select.evaluate("el => el.value")
        print(f"Initially selected node value: '{selected_val}'")
        assert selected_val == "us", "Default selected node should be 'us'"

        # Wait for latency-val to show a number (initially 'Measuring...')
        latency_val = page.locator("#latency-val")
        print("Waiting for initial latency measurement to complete...")
        await page.wait_for_function("document.getElementById('latency-val').textContent !== 'Measuring...'")
        initial_ping_text = await latency_val.text_content()
        print(f"Initial US Ping latency: {initial_ping_text}")
        initial_ping = int(initial_ping_text.replace(" ms", "").strip())
        # US-East range: 10 to 24 ms
        assert 10 <= initial_ping <= 24, f"US Ping {initial_ping} out of bounds!"

        # 5. Cycle node using keyboard shortcut 'N'
        print("Pressing key 'N' to cycle node to EU...")
        await page.keyboard.press("n")

        # Select value should change to 'eu'
        await page.wait_for_function("document.getElementById('node-select').value === 'eu'")
        print("Dropdown successfully updated to 'eu' via keyboard shortcut 'N'.")

        # Wait for latency to complete EU measurement
        print("Waiting for EU latency measurement...")
        await page.wait_for_function("document.getElementById('latency-val').textContent !== 'Measuring...'")
        eu_ping_text = await latency_val.text_content()
        print(f"EU Ping latency: {eu_ping_text}")
        eu_ping = int(eu_ping_text.replace(" ms", "").strip())
        # EU-Central range: 35 to 59 ms
        assert 35 <= eu_ping <= 59, f"EU Ping {eu_ping} out of bounds!"

        # 6. Cycle node again using keyboard shortcut 'N' (should go to AP)
        print("Pressing key 'N' again to cycle node to AP...")
        await page.keyboard.press("n")

        await page.wait_for_function("document.getElementById('node-select').value === 'ap'")
        print("Dropdown successfully updated to 'ap' via keyboard shortcut 'N'.")

        print("Waiting for AP latency measurement...")
        await page.wait_for_function("document.getElementById('latency-val').textContent !== 'Measuring...'")
        ap_ping_text = await latency_val.text_content()
        print(f"AP Ping latency: {ap_ping_text}")
        ap_ping = int(ap_ping_text.replace(" ms", "").strip())
        # AP-Tokyo range: 130 to 179 ms
        assert 130 <= ap_ping <= 179, f"AP Ping {ap_ping} out of bounds!"

        # 7. Check selecting 'us' manually via dropdown element
        print("Selecting 'us' manually via dropdown menu option...")
        await node_select.select_option("us")
        await page.wait_for_function("document.getElementById('latency-val').textContent !== 'Measuring...'")
        us_ping_text = await latency_val.text_content()
        print(f"US Ping latency after manual switch: {us_ping_text}")

        # 8. Check polite screen-reader status updates
        sr_status = page.locator("#sr-status")
        sr_text = await sr_status.text_content()
        print(f"Latest screen reader status update: '{sr_text}'")
        assert "Latency updated" in sr_text, "Screen reader update mismatch!"

        # Take screenshot of the dark mode state to save visual evidence
        # Let's toggle to dark mode first to see if screenshots look amazing
        print("Toggling theme to Dark Mode...")
        await page.keyboard.press("t")
        await page.wait_for_timeout(300) # Wait for CSS theme transition
        screenshot_path = "screenshot_dark_connected.png"
        await page.screenshot(path=screenshot_path)
        print(f"Screenshot successfully saved to: {screenshot_path}")

        # Clean up
        print("Disconnecting from secure gateway...")
        await page.keyboard.press("h")

        # Verify title transition to "Disconnecting..."
        disconnecting_title = await page.title()
        print(f"Title during disconnection: '{disconnecting_title}'")
        assert "Disconnecting..." in disconnecting_title, "Title during disconnection transition mismatch!"

        await page.wait_for_timeout(1000)

        # Verify title restores to default
        final_title = await page.title()
        print(f"Final restored title: '{final_title}'")
        assert final_title == "Mr.connection_006-hub", "Restored title mismatch!"

        await context.close()
        await browser.close()
        print("All visual and functional checks passed successfully!")

if __name__ == "__main__":
    asyncio.run(run_verification())
