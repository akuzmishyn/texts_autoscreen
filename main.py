from playwright.sync_api import sync_playwright
import time
import json


def screen_paytable(page, lang, mode):
    page.click('//*[@id="game_canvas"]')
    page.keyboard.press("i")
    page.click('//*[@id="game_canvas"]')

    for i in range(7):
        page.screenshot(path=f"{lang}/{mode}/paytable_{lang}_{i}.png")
        page.mouse.wheel(0, 100)

    page.click('//*[@id="game_canvas"]')
    page.keyboard.press("Escape")


def screen_bonus_start(page, lang, mode):
    # page.wait_for_selector('//*[@class="close-button close-bottom drag"]').click()
    shifts = ""
    with open("config.json") as file:
        config = json.load(file)
        shifts = "".join(config['shifts'])

    page.wait_for_selector('//*[text()="Open Controls"]').click()
    page.wait_for_selector('//*[text()="shifter"]').click()
    with page.context.expect_page() as tab:
        new_tab = tab.value
        time.sleep(2)
        new_tab.wait_for_selector('//input[@class="combination-edit-input"]').fill(shifts)
        time.sleep(1)
        new_tab.wait_for_selector('//input[@class="combination-edit-input"]').click()
        time.sleep(2)
        new_tab.keyboard.press("Tab")
        new_tab.keyboard.press("Enter")
        new_tab.wait_for_selector('//*[contains(text(), "Clear & Send")]').click()
        # new_tab.wait_for_selector('//*[@class="shift-list-button"] >> nth=3').click()

        time.sleep(2)
        new_tab.close()

    page.wait_for_selector('//*[text()="Close Controls"]').click()
    page.click('//*[@id="game_canvas"]')
    page.keyboard.press("Enter")
    time.sleep(15)
    page.screenshot(path=f"{lang}/{mode}/start_bonus_{lang}.png")


def screen_main(page, lang, mode):
    page.click('//*[@id="game_canvas"]')
    page.keyboard.press("Enter")
    page.screenshot(path=f"{lang}/{mode}/main_{lang}.png")


# def input_langs():
#     langs_str = input("Input Languages Separated by space: ")
#     return list(filter(None, langs_str.split(" ")))


def test_mobile_landscape(languages, game, branch):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, channel="chrome")
        page = browser.new_page()
        for lang in languages:
            page.goto(f"https://dgm-beta.ps-gamespace.com/launch?link_title={branch}&gameName={game}_mob&partner={branch}-gs-beta-platform-new&force_mobile=1&key=TEST50000&lang={lang}")
            time.sleep(60)
            screen_main(page, lang, "landscape")
            screen_paytable(page, lang, "landscape")
            screen_bonus_start(page, lang, "landscape")
        browser.close()


def test_mobile_portrait(languages, game, branch):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, channel="chrome")
        page = browser.new_page(viewport={'width': 400, 'height': 840})
        for lang in languages:
            page.goto(f"https://dgm-beta.ps-gamespace.com/launch?link_title={branch}&gameName={game}_mob&partner={branch}-gs-beta-platform-new&force_mobile=1&key=TEST50000&lang={lang}")
            time.sleep(60)
            screen_main(page, lang, "portrait")
            screen_paytable(page, lang, "portrait")
            screen_bonus_start(page, lang, "portrait")
        browser.close()


def test_desktop(languages, game, branch):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, channel="chrome")
        page = browser.new_page()
        for lang in languages:
            page.goto(f"https://dgm-beta.ps-gamespace.com/launch?link_title={branch}&gameName={game}&partner={branch}-gs-beta-platform-new&key=test50000&viewid=gameFrame&lang={lang}")
            time.sleep(60)
            screen_main(page, lang, "desktop")
            screen_paytable(page, lang, "desktop")
            screen_bonus_start(page, lang, "desktop")
        browser.close()


if __name__ == "__main__":
    # languages = input_langs()
    # game = input("Input game_name")
    # branch = input("Input branch_name")

    with open("config.json") as file:
        config = json.load(file)
        game = config['game_name']
        languages = config['languages']
        branch = config['branch']

    test_desktop(languages, game, branch)
    test_mobile_portrait(languages, game, branch)
    test_mobile_landscape(languages, game, branch)
