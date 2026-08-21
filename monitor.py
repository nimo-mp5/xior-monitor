from playwright.sync_api import sync_playwright

URL = "https://www.xiorstudenthousing.eu/netherlands/eindhoven/kronehoefstraat-student-accommodation/"

FULLY_BOOKED = "Kronehoefstraat is fully booked at the moment"

print("Starting browser...")
print("Checking Xior Kronehoefstraat...")

with sync_playwright() as p:

    browser = p.chromium.launch(headless=True)

    page = browser.new_page(
        viewport={"width": 1440, "height": 1200},
        user_agent=(
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/140.0.0.0 Safari/537.36"
        ),
    )

    response = page.goto(
        URL,
        wait_until="domcontentloaded",
        timeout=60000
    )

    if response:
        print("HTTP status:", response.status)

    # JavaScriptなどが読み込まれるのを待つ
    page.wait_for_timeout(5000)

    print("Page title:", page.title())

    text = page.locator("body").inner_text()

    # 後で確認できるようスクリーンショットを保存
    page.screenshot(
        path="xior-page.png",
        full_page=True
    )

    if FULLY_BOOKED.lower() in text.lower():

        print("")
        print("❌ FULLY BOOKED")
        print("Kronehoefstraat currently has no available rooms.")

    else:

        print("")
        print("🚨 POSSIBLE AVAILABILITY!")
        print("The fully booked message was NOT found.")
        print("Check Xior immediately:")
        print(URL)

        print("")
        print("Page text preview:")
        print(text[:3000])

    browser.close()

print("")
print("Check complete.")
