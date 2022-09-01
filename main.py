import json
import time
from tkinter import *
from tkinter.ttk import Checkbutton
from playwright.sync_api import sync_playwright


def start_testing():

    with open("config.json") as file:
        config = json.load(file)
        game = config['game_name']
        languages = config['languages']
        branch = config['branch']

    modes = []
    if chk_mobile_landscape_state.get() == 1:
        modes.append('mobile_portrait')
    if chk_mobile_portrait_state.get() == 1:
        modes.append('mobile_landscape')
    if chk_desktop_state.get() == 1:
        modes.append('desktop')

    lenght_modes = len(modes)
    modes_checked = 0
    lenght_languages = len(languages)

    for mode in modes:
        if mode == "mobile_portrait":
            modes_checked += 1
            print(f'[{game}][{mode}]: in work [{modes_checked}/{lenght_modes}]')
            print("===   ===   ===   ===")
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=False, channel="chrome")
                page = browser.new_page(viewport={'width': 400, 'height': 840})
                languages_checked = 0
                for lang in languages:
                    print(f"[{lang}] in work [{languages_checked}/{lenght_languages}]")
                    page.goto(
                        f"https://dgm-beta.ps-gamespace.com/launch?link_title={branch}&gameName={game}_mob&partner="
                        f"{branch}-gs-beta-platform-new&key=test50000&viewid=gameFrame&lang={lang}")
                    time.sleep(22)  #ВРЕМЯ ЗАГРУЗКИ ИГРЫ
                    correct_modes(game, page, lang, mode)
                    languages_checked += 1
                    print(f"[{lang}] CHECKED [{languages_checked}/{lenght_languages}]")
                    print("- - - - - - -")
            print(f'[{game}][{mode}]: CHECKED [{modes_checked}/{lenght_modes}]')
            print("===============================")

        elif mode == "mobile_landscape":
            modes_checked += 1
            print(f'[{game}][{mode}]: in work [{modes_checked}/{lenght_modes}]')
            print("===   ===   ===   ===")
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=False, channel="chrome")
                page = browser.new_page()
                languages_checked = 0
                for lang in languages:
                    print(f"[{lang}] in work [{languages_checked}/{lenght_languages}]")
                    page.goto(
                        f"https://dgm-beta.ps-gamespace.com/launch?link_title={branch}&gameName={game}_mob&partner="
                        f"{branch}-gs-beta-platform-new&key=test50000&viewid=gameFrame&lang={lang}")
                    time.sleep(15)  #ВРЕМЯ ЗАГРУЗКИ ИГРЫ
                    correct_modes(game, page, lang, mode)
                    languages_checked += 1
                    print(f"[{lang}] CHECKED [{languages_checked}/{lenght_languages}]")
                    print("- - - - - - -")

            print(f'[{game}][{mode}]: CHECKED [{modes_checked}/{lenght_modes}]')
            print("===============================")

        else:
            modes_checked += 1
            print(f'[{game}][{mode}]: in work [{modes_checked}/{lenght_modes}]')
            print("===   ===   ===   ===")
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=False, channel="chrome")
                page = browser.new_page()
                languages_checked = 0
                for lang in languages:
                    print(f"[{lang}] in work [{languages_checked}/{lenght_languages}]")
                    page.goto(
                        f"https://dgm-beta.ps-gamespace.com/launch?link_title={branch}&gameName={game}&partner="
                        f"{branch}-gs-beta-platform-new&key=test50000&viewid=gameFrame&lang={lang}")
                    time.sleep(15)  #ВРЕМЯ ЗАГРУЗКИ ИГРЫ
                    correct_modes(game, page, lang, mode)
                    languages_checked += 1
                    print(f"[{lang}] CHECKED [{languages_checked}/{lenght_languages}]")
                    print("- - - - - - -")
            print(f'[{game}][{mode}]: CHECKED [{modes_checked}/{lenght_modes}]')
            print("===============================")


def screen_pop_up(game_name, page, lang, mode):
    if chk_screenshot_all_time.get() == 1:

        page.click('//*[@id="game_canvas"]')
        page.screenshot(path=f"{game_name}/{lang}/{mode}/screen_pop_up_{lang}.png")
        print("Screen [Feature Preview Pop Up] - done")
        page.keyboard.press("Enter")
    elif chk_screenshot_manual.get() == 1:
        page.click('//*[@id="game_canvas"]')
        screen_value = input("Make screenshot? : ")
        if screen_value == "y":
            page.screenshot(path=f"{game_name}/{lang}/{mode}/screen_pop_up_{lang}.png")
            print("Screen [Feature Preview Pop Up] - done")
            page.keyboard.press("Enter")
        else:
            page.keyboard.press("Enter")
    elif chk_without_screenshot.get() == 1:
        page.click('//*[@id="game_canvas"]')
        page.keyboard.press("Enter")


def screen_main(game_name, page, lang, mode):
    if chk_screenshot_all_time.get() == 1:
        page.click('//*[@id="game_canvas"]')
        page.screenshot(path=f"{game_name}/{lang}/{mode}/main_{lang}.png")
        print("Screen [Main Game] - done")
    elif chk_screenshot_manual.get() == 1:
        page.click('//*[@id="game_canvas"]')
        screen_value = input("Make screenshot? : ")
        if screen_value == "y":
            page.screenshot(path=f"{game_name}/{lang}/{mode}/main_{lang}.png")
            print("Screen [Main Game] - done")
        else:
            page.click('//*[@id="game_canvas"]')
    elif chk_without_screenshot.get() == 1:
        page.click('//*[@id="game_canvas"]')


def screen_big_mega_super_win(game_name, page, lang, mode):
    with open("config.json") as file:
        config = json.load(file)
        shifts = "".join(config['shifts'].get("big_super_mega_win"))

    page.wait_for_selector('//*[text()="Open Controls"]').click()
    page.wait_for_selector('//*[text()="shifter"]').click()

    new_tab_open(page, shifts)

    if chk_screenshot_all_time.get() == 1:
        page.wait_for_selector('//*[text()="Close Controls"]').click()
        page.click('//*[@id="game_canvas"]')
        page.keyboard.press("Space")
        time.sleep(7) #Время через которое делается скип
        page.click('//*[@id="game_canvas"]')
        time.sleep(1) #Время через которое делается скрин после скипа
        page.screenshot(path=f"{game_name}/{lang}/{mode}/screen_big_win_{lang}.png")
        print("Screen [Big Win Pop Up] - done")
        time.sleep(2)
        page.click('//*[text()="Open Controls"]')
        time.sleep(1)
        page.click('//*[text()="Close Controls"]')
        page.keyboard.press("Space")
        time.sleep(7) #Время через которое делается скип
        page.click('//*[@id="game_canvas"]')
        time.sleep(1) #Время через которое делается скрин после скипа
        page.screenshot(path=f"{game_name}/{lang}/{mode}/screen_mega_win_{lang}.png")
        print("Screen [Mega Win Pop Up] - done")
        page.click('//*[@id="game_canvas"]')
        time.sleep(2)
        page.click('//*[text()="Open Controls"]')
        time.sleep(1)
        page.click('//*[text()="Close Controls"]')
        page.keyboard.press("Space")
        time.sleep(7)
        page.click('//*[@id="game_canvas"]')
        time.sleep(1)
        page.screenshot(path=f"{game_name}/{lang}/{mode}/screen_super_win_{lang}.png")
        print("Screen [Super Win Pop Up] - done")
        time.sleep(1)
    elif chk_screenshot_manual.get() == 1:
        page.wait_for_selector('//*[text()="Close Controls"]').click()
        page.click('//*[@id="game_canvas"]')
        page.keyboard.press("Space")   #SPIN START
        time.sleep(7) #Время через которое делается скип
        page.click('//*[@id="game_canvas"]')  #Click on game field
        time.sleep(1) #Время через которое делается скрин после скипа
        page.click('//*[text()="Open Controls"]') #Open Control
        page.wait_for_selector('//*[text()="pause"]').click() #Pause the game
        page.wait_for_selector('//*[text()="Close Controls"]').click() #Close the console

        screen_value = input("Make screenshot? : ")
        if screen_value == "y":
            page.screenshot(path=f"{game_name}/{lang}/{mode}/screen_big_win_{lang}.png")
            print("Screen [Big Win Pop Up] - done")
            time.sleep(1)
            page.wait_for_selector('//*[text()="Open Controls"]').click()
            page.wait_for_selector('//*[text()="resume"]').click()
            page.wait_for_selector('//*[text()="Close Controls"]').click()
            time.sleep(2)
            page.click('//*[@id="game_canvas"]')
            time.sleep(2)
            page.keyboard.press("Enter")

        else:
            page.wait_for_selector('//*[text()="Open Controls"]').click()
            page.wait_for_selector('//*[text()="resume"]').click()
            page.wait_for_selector('//*[text()="Close Controls"]').click()
            time.sleep(2)
            page.click('//*[@id="game_canvas"]')
            time.sleep(2)
            page.keyboard.press("Enter")

        time.sleep(7)
        page.click('//*[@id="game_canvas"]')
        time.sleep(1)
        page.click('//*[text()="Open Controls"]')
        page.wait_for_selector('//*[text()="pause"]').click()
        page.wait_for_selector('//*[text()="Close Controls"]').click()

        screen_value2 = input("Make screenshot? : ")
        if screen_value2 == "y":
            page.screenshot(path=f"{game_name}/{lang}/{mode}/screen_super_win_{lang}.png")
            print("Screen [Super Win Pop Up] - done")
            time.sleep(1)
            page.wait_for_selector('//*[text()="Open Controls"]').click()
            page.wait_for_selector('//*[text()="resume"]').click()
            page.wait_for_selector('//*[text()="Close Controls"]').click()
            time.sleep(2)
            page.click('//*[@id="game_canvas"]')
            time.sleep(2)
            page.keyboard.press("Enter")
        else:
            page.wait_for_selector('//*[text()="Open Controls"]').click()
            page.wait_for_selector('//*[text()="resume"]').click()
            page.wait_for_selector('//*[text()="Close Controls"]').click()
            time.sleep(2)
            page.click('//*[@id="game_canvas"]')
            time.sleep(2)
            page.keyboard.press("Enter")

        page.click('//*[@id="game_canvas"]')
        page.keyboard.press("Space")
        time.sleep(7)
        page.click('//*[@id="game_canvas"]')
        time.sleep(1)
        page.click('//*[text()="Open Controls"]')
        page.wait_for_selector('//*[text()="pause"]').click()
        page.wait_for_selector('//*[text()="Close Controls"]').click()

        screen_value3 = input("Make screenshot? : ")
        if screen_value3 == "y":
            page.screenshot(path=f"{game_name}/{lang}/{mode}/screen_mega_win_{lang}.png")
            print("Screen [Mega Win Pop Up] - done")
            time.sleep(1)
            page.wait_for_selector('//*[text()="Open Controls"]').click()
            page.wait_for_selector('//*[text()="resume"]').click()
            page.wait_for_selector('//*[text()="Close Controls"]').click()
            time.sleep(2)
            page.click('//*[@id="game_canvas"]')
            time.sleep(2)
            page.keyboard.press("Enter")
        else:
            page.wait_for_selector('//*[text()="Open Controls"]').click()
            page.wait_for_selector('//*[text()="resume"]').click()
            page.wait_for_selector('//*[text()="Close Controls"]').click()
            time.sleep(2)
            page.click('//*[@id="game_canvas"]')
            time.sleep(2)
            page.keyboard.press("Enter")
    elif chk_without_screenshot.get() == 1:
        page.wait_for_selector('//*[text()="Close Controls"]').click()
        page.click('//*[@id="game_canvas"]')
        page.keyboard.press("Space")
        time.sleep(7)
        page.click('//*[@id="game_canvas"]')
        time.sleep(2)
        page.click('//*[text()="Open Controls"]')
        time.sleep(1)
        page.click('//*[text()="Close Controls"]')
        page.keyboard.press("Space")
        time.sleep(7)
        page.click('//*[@id="game_canvas"]')
        time.sleep(2)
        page.click('//*[text()="Open Controls"]')
        time.sleep(1)
        page.click('//*[text()="Close Controls"]')
        page.keyboard.press("Space")
        time.sleep(7)
        page.click('//*[@id="game_canvas"]')
        time.sleep(2)


def screen_freespin_pop_up(game_name, page, lang, mode):
    with open("config.json") as file:
        config = json.load(file)
        shifts = "".join(config['shifts'].get("free_spin_shift"))

    page.wait_for_selector('//*[text()="Open Controls"]').click()
    page.wait_for_selector('//*[text()="shifter"]').click()

    new_tab_open(page, shifts)

    if chk_screenshot_all_time.get() == 1:
        page.wait_for_selector('//*[text()="Close Controls"]').click()
        page.click('//*[@id="game_canvas"]')
        page.keyboard.press("Enter")
        time.sleep(15) # Время ожидания транзишина перехода из мейн гейма в фри спины
        page.screenshot(path=f"{game_name}/{lang}/{mode}/free_spin_pop_up_{lang}.png")
        print("Screen [Free Spin Pop Up] - done")
    elif chk_screenshot_manual.get() == 1:
        page.wait_for_selector('//*[text()="Close Controls"]').click()
        page.click('//*[@id="game_canvas"]')
        page.keyboard.press("Enter")
        time.sleep(15) # Время ожидания транзишина перехода из мейн гейма в фри спины
        screen_value = input("Make screenshot? : ")
        if screen_value == "y":
            page.screenshot(path=f"{game_name}/{lang}/{mode}/free_spin_pop_up_{lang}.png")
            print("Screen [Free Spin Pop Up] - done")
    elif chk_without_screenshot.get() == 1:
        page.wait_for_selector('//*[text()="Close Controls"]').click()
        page.click('//*[@id="game_canvas"]')
        page.keyboard.press("Enter")
        time.sleep(15)


def screen_freespin_and_additional_pop_up(game_name, page, lang, mode):
    with open("config.json") as file:
        config = json.load(file)
        shifts = "".join(config['shifts'].get("free_spin_shift_and_add_spins"))

    page.wait_for_selector('//*[text()="Open Controls"]').click()
    page.wait_for_selector('//*[text()="shifter"]').click()

    new_tab_open(page, shifts)

    if chk_screenshot_all_time.get() == 1:
        page.wait_for_selector('//*[text()="Close Controls"]').click()
        page.click('//*[@id="game_canvas"]')
        page.keyboard.press("Enter")
        time.sleep(15) # Время ожидания транзишина перехода из мейн гейма в фри спины
        page.keyboard.press("Enter")
        time.sleep(10) # Время ожидания србатывания дополнительных фриспинов
        page.click('//*[@id="game_canvas"]')
        time.sleep(1) # Время через которое делается скриншот
        page.screenshot(path=f"{game_name}/{lang}/{mode}/free_spin_add_{lang}.png")
        print("Screen [Add Free Spin Pop Up] - done")
    elif chk_screenshot_manual.get() == 1:

        page.wait_for_selector('//*[text()="Close Controls"]').click()
        page.click('//*[@id="game_canvas"]')
        page.keyboard.press("Enter")
        time.sleep(15) # Время ожидания транзишина перехода из мейн гейма в фри спины
        page.keyboard.press("Enter")
        time.sleep(10) # Время ожидания србатывания дополнительных фриспинов
        page.click('//*[@id="game_canvas"]')
        page.wait_for_selector('//*[text()="Open Controls"]').click()
        page.wait_for_selector('//*[text()="pause"]').click()
        page.wait_for_selector('//*[text()="Close Controls"]').click()
        screen_value = input("Make screenshot?: ")
        if screen_value == "y":
            page.screenshot(path=f"{game_name}/{lang}/{mode}/free_spin_add_{lang}.png")
            print("Screen [Add Free Spin Pop Up] - done")
    elif chk_without_screenshot.get() == 1:
        page.wait_for_selector('//*[text()="Close Controls"]').click()
        page.click('//*[@id="game_canvas"]')
        page.keyboard.press("Enter")
        time.sleep(15)
        page.keyboard.press("Enter")
        time.sleep(10)
        page.click('//*[@id="game_canvas"]')
        time.sleep(1)


def screen_bonus_game(game_name, page, lang, mode):
    with open("config.json") as file:
        config = json.load(file)
        shifts = "".join(config['shifts'].get("bonus_game_shift"))

    page.wait_for_selector('//*[text()="Open Controls"]').click()
    page.wait_for_selector('//*[text()="shifter"]').click()

    new_tab_open(page, shifts)

    if chk_screenshot_all_time.get() == 1:
        page.wait_for_selector('//*[text()="Close Controls"]').click()
        page.click('//*[@id="game_canvas"]')
        page.keyboard.press("Enter")
        time.sleep(15)  # Время ожидания транзишина перехода из мейн гейма в бонус игру
        page.screenshot(path=f"{game_name}/{lang}/{mode}/bonus_game_pop_up_{lang}.png")
        print("Screen [Bonus Game Pop Up] - done")
    elif chk_screenshot_manual.get() == 1:
        page.wait_for_selector('//*[text()="Close Controls"]').click()
        page.click('//*[@id="game_canvas"]')
        page.keyboard.press("Enter")
        time.sleep(15) # Время ожидания транзишина перехода из мейн гейма в бонус игру
        screen_value = input("Make screenshot?: ")
        if screen_value == "y":
            page.screenshot(path=f"{game_name}/{lang}/{mode}/bonus_game_pop_up_{lang}.png")
            print("Screen [Bonus Game Pop Up] - done")
    elif chk_without_screenshot.get() == 1:
        page.wait_for_selector('//*[text()="Close Controls"]').click()
        page.click('//*[@id="game_canvas"]')
        page.keyboard.press("Enter")
        time.sleep(15)


def screen_paytable(game_name, page, lang, mode):
    time.sleep(2)
    page.click('//*[text()="Open Controls"]')
    time.sleep(1)
    page.click('//*[text()="Close Controls"]')

    page.click('//*[@id="game_canvas"]')
    page.keyboard.press("i")
    page.click('//*[@id="game_canvas"]')
    time.sleep(2)

    if chk_screenshot_all_time.get() == 1:
        for i in range(10):
            page.screenshot(path=f"{game_name}/{lang}/{mode}/paytable_{lang}_{i}.png")
            page.mouse.wheel(0, 125)

        print("Screen [All Paytable] - done")
        page.click('//*[@id="game_canvas"]')
        page.keyboard.press("Escape")
    elif chk_screenshot_manual.get() == 1:
        number_screen = 1
        for i in range(12):
            screen_value = input("Make screenshot?: ")
            if screen_value == "y":
                page.screenshot(path=f"{game_name}/{lang}/{mode}/paytable_{lang}_{i}.png")
                print(f"Screen [Paytable_{number_screen}] - done")
                page.mouse.wheel(0, 125)

                number_screen += 1

            else:
                page.mouse.wheel(0, 125)

        print("Checking [All Paytable] - done")
        page.click('//*[@id="game_canvas"]')
        page.keyboard.press("Escape")
    elif chk_without_screenshot.get() == 1:
        for i in range(10):
            time.sleep(1)
            page.mouse.wheel(0, 125)

        page.click('//*[@id="game_canvas"]')
        page.keyboard.press("Escape")


def new_tab_open(page, shift):
    with page.context.expect_page() as tab:
        new_tab = tab.value
        time.sleep(2)
        new_tab.wait_for_selector('//select[@class="game-list-select"]').click()
        time.sleep(1)
        new_tab.wait_for_selector('//input[@class="combination-edit-input"]').click()
        time.sleep(1)
        new_tab.wait_for_selector('//input[@class="combination-edit-input"]').fill(shift)
        time.sleep(1)
        new_tab.wait_for_selector('//input[@class="combination-edit-input"]').click()
        time.sleep(2)
        new_tab.keyboard.press("Tab")
        new_tab.keyboard.press("Enter")
        new_tab.wait_for_selector('//*[contains(text(), "Clear & Send")]').click()

        time.sleep(2)
        new_tab.close()


def correct_modes(game, page, lang, mode):
    if chk_pop_up_state.get() == 1 and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 0):
        screen_pop_up(game, page, lang, mode)
    elif chk_pop_up_state.get() == 0 and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 0):
        page.keyboard.press("Enter")
        screen_main(game, page, lang, mode)
    elif chk_pop_up_state.get() == 0 and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 0):
        page.keyboard.press("Enter")
        screen_big_mega_super_win(game, page, lang, mode)
    elif chk_pop_up_state.get() == 0 and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 0):
        page.keyboard.press("Enter")
        screen_freespin_pop_up(game, page, lang, mode)
    elif chk_pop_up_state.get() == 0 and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 0):
        page.keyboard.press("Enter")
        screen_freespin_and_additional_pop_up(game, page, lang, mode)
    elif chk_pop_up_state.get() == 0 and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 1):
        page.keyboard.press("Enter")
        screen_bonus_game(game, page, lang, mode)
    elif chk_pop_up_state.get() == 0 and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 1) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 0):
        page.keyboard.press("Enter")
        screen_paytable(game, page, lang, mode)
    elif chk_pop_up_state.get() == 1 and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 0):
        screen_pop_up(game, page, lang, mode)
        screen_main(game, page, lang, mode)
    elif chk_pop_up_state.get() == 1 and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 0):
        screen_pop_up(game, page, lang, mode)
        screen_big_mega_super_win(game, page, lang, mode)
    elif chk_pop_up_state.get() == 1 and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 0):
        screen_pop_up(game, page, lang, mode)
        screen_freespin_pop_up(game, page, lang, mode)
    elif chk_pop_up_state.get() == 1 and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 0):
        screen_pop_up(game, page, lang, mode)
        screen_freespin_and_additional_pop_up(game, page, lang, mode)
    elif chk_pop_up_state.get() == 1 and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 1):
        screen_pop_up(game, page, lang, mode)
        screen_bonus_game(game, page, lang, mode)
    elif chk_pop_up_state.get() == 1 and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 1) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 0):
        screen_pop_up(game, page, lang, mode)
        screen_paytable(game, page, lang, mode)
    elif (chk_pop_up_state.get() == 0) and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 0):
        page.keyboard.press("Enter")
        screen_main(game, page, lang, mode)
        screen_big_mega_super_win(game, page, lang, mode)
    elif (chk_pop_up_state.get() == 0) and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 0):
        page.keyboard.press("Enter")
        screen_main(game, page, lang, mode)
        screen_freespin_pop_up(game, page, lang, mode)
    elif (chk_pop_up_state.get() == 0) and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 0):
        page.keyboard.press("Enter")
        screen_main(game, page, lang, mode)
        screen_freespin_and_additional_pop_up(game, page, lang, mode)
    elif (chk_pop_up_state.get() == 0) and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 1):
        page.keyboard.press("Enter")
        screen_main(game, page, lang, mode)
        screen_bonus_game(game, page, lang, mode)
    elif (chk_pop_up_state.get() == 0) and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 1) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 0):
        page.keyboard.press("Enter")
        screen_main(game, page, lang, mode)
        screen_paytable(game, page, lang, mode)
    #
    elif (chk_pop_up_state.get() == 0) and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 0):
        page.keyboard.press("Enter")
        screen_big_mega_super_win(game, page, lang, mode)
        page.reload()
        time.sleep(15)
        page.keyboard.press("Enter")
        screen_freespin_pop_up(game, page, lang, mode)

    elif (chk_pop_up_state.get() == 0) and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 0):
        page.keyboard.press("Enter")
        screen_big_mega_super_win(game, page, lang, mode)
        page.reload()
        time.sleep(15)
        page.keyboard.press("Enter")
        screen_freespin_and_additional_pop_up(game, page, lang, mode)

    elif (chk_pop_up_state.get() == 0) and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 1):
        page.keyboard.press("Enter")
        screen_big_mega_super_win(game, page, lang, mode)
        page.reload()
        time.sleep(15)
        page.keyboard.press("Enter")
        screen_bonus_game(game, page, lang, mode)

    elif (chk_pop_up_state.get() == 0) and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 1) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 0):
        page.keyboard.press("Enter")
        screen_big_mega_super_win(game, page, lang, mode)
        screen_paytable(game, page, lang, mode)
    #
    elif (chk_pop_up_state.get() == 0) and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 0):
        page.keyboard.press("Enter")
        screen_freespin_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(15)
        page.keyboard.press("Enter")
        screen_freespin_and_additional_pop_up(game, page, lang, mode)
    elif (chk_pop_up_state.get() == 0) and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 1):
        page.keyboard.press("Enter")
        screen_freespin_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(15)
        page.keyboard.press("Enter")
        screen_bonus_game(game, page, lang, mode)

    elif (chk_pop_up_state.get() == 0) and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 1) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 0):
        page.keyboard.press("Enter")
        screen_paytable(game, page, lang, mode)
        screen_freespin_pop_up(game, page, lang, mode)

    #
    elif (chk_pop_up_state.get() == 0) and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 1):
        page.keyboard.press("Enter")
        screen_freespin_and_additional_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(15)
        page.keyboard.press("Enter")
        screen_bonus_game(game, page, lang, mode)

    elif (chk_pop_up_state.get() == 0) and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 1) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 0):
        page.keyboard.press("Enter")
        screen_paytable(game, page, lang, mode)
        screen_freespin_and_additional_pop_up(game, page, lang, mode)

    #
    elif (chk_pop_up_state.get() == 0) and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 1) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 1):
        page.keyboard.press("Enter")
        screen_paytable(game, page, lang, mode)
        screen_bonus_game(game, page, lang, mode)

    #
    elif (chk_pop_up_state.get() == 1) and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 0):
        screen_pop_up(game, page, lang, mode)
        screen_main(game, page, lang, mode)
        screen_bonus_game(game, page, lang, mode)

    elif (chk_pop_up_state.get() == 1) and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 0):
        screen_pop_up(game, page, lang, mode)
        screen_main(game, page, lang, mode)
        screen_freespin_pop_up(game, page, lang, mode)

    elif (chk_pop_up_state.get() == 1) and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 0):
        screen_pop_up(game, page, lang, mode)
        screen_main(game, page, lang, mode)
        screen_freespin_and_additional_pop_up(game, page, lang, mode)

    elif (chk_pop_up_state.get() == 1) and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 1):
        screen_pop_up(game, page, lang, mode)
        screen_main(game, page, lang, mode)
        screen_bonus_game(game, page, lang, mode)

    elif (chk_pop_up_state.get() == 1) and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 1) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 0):
        screen_pop_up(game, page, lang, mode)
        screen_main(game, page, lang, mode)
        screen_paytable(game, page, lang, mode)
    #
    elif (chk_pop_up_state.get() == 1) and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 0):
        screen_pop_up(game, page, lang, mode)
        screen_big_mega_super_win(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_pop_up(game, page, lang, mode)

    elif (chk_pop_up_state.get() == 1) and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 0):
        screen_pop_up(game, page, lang, mode)
        screen_big_mega_super_win(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_and_additional_pop_up(game, page, lang, mode)

    elif (chk_pop_up_state.get() == 1) and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 1):
        screen_pop_up(game, page, lang, mode)
        screen_big_mega_super_win(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_bonus_game(game, page, lang, mode)

    elif (chk_pop_up_state.get() == 1) and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 1) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 0):
        screen_pop_up(game, page, lang, mode)
        screen_big_mega_super_win(game, page, lang, mode)
        screen_paytable(game, page, lang, mode)

    #
    elif (chk_pop_up_state.get() == 1) and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 0):
        screen_pop_up(game, page, lang, mode)
        screen_freespin_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_and_additional_pop_up(game, page, lang, mode)

    elif (chk_pop_up_state.get() == 1) and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 1):
        screen_pop_up(game, page, lang, mode)
        screen_freespin_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_bonus_game(game, page, lang, mode)

    elif (chk_pop_up_state.get() == 1) and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 1) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 0):
        screen_pop_up(game, page, lang, mode)
        screen_paytable(game, page, lang, mode)
        screen_freespin_pop_up(game, page, lang, mode)

    #
    elif (chk_pop_up_state.get() == 1) and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 1):
        screen_pop_up(game, page, lang, mode)
        screen_freespin_and_additional_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_bonus_game(game, page, lang, mode)

    elif (chk_pop_up_state.get() == 1) and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 1):
        screen_pop_up(game, page, lang, mode)
        screen_paytable(game, page, lang, mode)
        screen_freespin_and_additional_pop_up(game, page, lang, mode)

    #
    elif (chk_pop_up_state.get() == 1) and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 1) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 1):
        screen_pop_up(game, page, lang, mode)
        screen_paytable(game, page, lang, mode)
        screen_bonus_game(game, page, lang, mode)

    #
    elif (chk_pop_up_state.get() == 0) and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 0):
        page.keyboard.press("Enter")
        screen_main(game, page, lang, mode)
        screen_big_mega_super_win(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_pop_up(game, page, lang, mode)

    elif (chk_pop_up_state.get() == 0) and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 0):
        page.keyboard.press("Enter")
        screen_main(game, page, lang, mode)
        screen_big_mega_super_win(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_and_additional_pop_up(game, page, lang, mode)

    elif (chk_pop_up_state.get() == 0) and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 1):
        page.keyboard.press("Enter")
        screen_main(game, page, lang, mode)
        screen_big_mega_super_win(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_bonus_game(game, page, lang, mode)

    elif (chk_pop_up_state.get() == 0) and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 1) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 0):
        page.keyboard.press("Enter")
        screen_main(game, page, lang, mode)
        screen_paytable(game, page, lang, mode)
        screen_big_mega_super_win(game, page, lang, mode)

    #
    elif (chk_pop_up_state.get() == 0) and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 0):
        page.keyboard.press("Enter")
        screen_main(game, page, lang, mode)
        screen_freespin_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_and_additional_pop_up(game, page, lang, mode)

    elif (chk_pop_up_state.get() == 0) and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 1):
        page.keyboard.press("Enter")
        screen_main(game, page, lang, mode)
        screen_freespin_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_bonus_game(game, page, lang, mode)

    elif (chk_pop_up_state.get() == 0) and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 1) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 0):
        page.keyboard.press("Enter")
        screen_main(game, page, lang, mode)
        screen_paytable(game, page, lang, mode)
        screen_freespin_pop_up(game, page, lang, mode)

    #
    elif (chk_pop_up_state.get() == 0) and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 1):
        page.keyboard.press("Enter")
        screen_main(game, page, lang, mode)
        screen_freespin_and_additional_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_bonus_game(game, page, lang, mode)

    elif (chk_pop_up_state.get() == 0) and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 1) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 0):
        page.keyboard.press("Enter")
        screen_main(game, page, lang, mode)
        screen_paytable(game, page, lang, mode)
        screen_freespin_and_additional_pop_up(game, page, lang, mode)
    #
    elif (chk_pop_up_state.get() == 0) and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 1) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 1):
        page.keyboard.press("Enter")
        screen_main(game, page, lang, mode)
        screen_paytable(game, page, lang, mode)
        screen_bonus_game(game, page, lang, mode)

    #
    elif (chk_pop_up_state.get() == 0) and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 1):
        page.keyboard.press("Enter")
        screen_big_mega_super_win(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_and_additional_pop_up(game, page, lang, mode)

    elif (chk_pop_up_state.get() == 0) and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 1):
        page.keyboard.press("Enter")
        screen_big_mega_super_win(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_bonus_game(game, page, lang, mode)

    elif (chk_pop_up_state.get() == 0) and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 1) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 0):
        page.keyboard.press("Enter")
        screen_paytable(game, page, lang, mode)
        screen_big_mega_super_win(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_pop_up(game, page, lang, mode)

    #
    elif (chk_pop_up_state.get() == 0) and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 1):
        page.keyboard.press("Enter")
        screen_big_mega_super_win(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_and_additional_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_bonus_game(game, page, lang, mode)

    elif (chk_pop_up_state.get() == 0) and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 1) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 0):
        page.keyboard.press("Enter")
        screen_paytable(game, page, lang, mode)
        screen_big_mega_super_win(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_and_additional_pop_up(game, page, lang, mode)

    elif (chk_pop_up_state.get() == 0) and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 1) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 1):
        page.keyboard.press("Enter")
        screen_paytable(game, page, lang, mode)
        screen_big_mega_super_win(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_bonus_game(game, page, lang, mode)
    #
    elif (chk_pop_up_state.get() == 0) and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 1):
        page.keyboard.press("Enter")
        screen_freespin_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_and_additional_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_bonus_game(game, page, lang, mode)

    elif (chk_pop_up_state.get() == 0) and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 1) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 0):
        page.keyboard.press("Enter")
        screen_paytable(game, page, lang, mode)
        screen_freespin_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_and_additional_pop_up(game, page, lang, mode)

    #
    elif (chk_pop_up_state.get() == 0) and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 1) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 1):
        page.keyboard.press("Enter")
        screen_paytable(game, page, lang, mode)
        screen_freespin_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_bonus_game(game, page, lang, mode)

    #
    elif (chk_pop_up_state.get() == 0) and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 1) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 1):
        page.keyboard.press("Enter")
        screen_paytable(game, page, lang, mode)
        screen_freespin_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_bonus_game(game, page, lang, mode)
    #
    elif (chk_pop_up_state.get() == 1) and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 0):
        screen_pop_up(game, page, lang, mode)
        screen_main(game, page, lang, mode)
        screen_big_mega_super_win(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_pop_up(game, page, lang, mode)

    elif (chk_pop_up_state.get() == 1) and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 0):
        screen_pop_up(game, page, lang, mode)
        screen_main(game, page, lang, mode)
        screen_big_mega_super_win(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_and_additional_pop_up(game, page, lang, mode)

    elif (chk_pop_up_state.get() == 1) and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 1):
        screen_pop_up(game, page, lang, mode)
        screen_main(game, page, lang, mode)
        screen_big_mega_super_win(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_bonus_game(game, page, lang, mode)

    elif (chk_pop_up_state.get() == 1) and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 1) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 0):
        screen_pop_up(game, page, lang, mode)
        screen_main(game, page, lang, mode)
        screen_paytable(game, page, lang, mode)
        screen_big_mega_super_win(game, page, lang, mode)

    #
    elif (chk_pop_up_state.get() == 1) and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 0):
        screen_pop_up(game, page, lang, mode)
        screen_main(game, page, lang, mode)
        screen_freespin_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_and_additional_pop_up(game, page, lang, mode)

    elif (chk_pop_up_state.get() == 1) and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 1):
        screen_pop_up(game, page, lang, mode)
        screen_main(game, page, lang, mode)
        screen_freespin_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_bonus_game(game, page, lang, mode)

    elif (chk_pop_up_state.get() == 1) and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 1) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 0):
        screen_pop_up(game, page, lang, mode)
        screen_main(game, page, lang, mode)
        screen_paytable(game, page, lang, mode)
        screen_freespin_pop_up(game, page, lang, mode)

    #
    elif (chk_pop_up_state.get() == 1) and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 1):
        screen_pop_up(game, page, lang, mode)
        screen_main(game, page, lang, mode)
        screen_freespin_and_additional_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_bonus_game(game, page, lang, mode)

    elif (chk_pop_up_state.get() == 1) and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 1) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 0):
        screen_pop_up(game, page, lang, mode)
        screen_main(game, page, lang, mode)
        screen_paytable(game, page, lang, mode)
        screen_freespin_and_additional_pop_up(game, page, lang, mode)

    #
    elif (chk_pop_up_state.get() == 1) and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 0):
        screen_pop_up(game, page, lang, mode)
        screen_big_mega_super_win(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_and_additional_pop_up(game, page, lang, mode)

    elif (chk_pop_up_state.get() == 1) and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 1):
        screen_pop_up(game, page, lang, mode)
        screen_big_mega_super_win(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_bonus_game(game, page, lang, mode)

    elif (chk_pop_up_state.get() == 1) and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 1) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 0):
        screen_pop_up(game, page, lang, mode)
        screen_paytable(game, page, lang, mode)
        screen_big_mega_super_win(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_pop_up(game, page, lang, mode)

    #
    elif (chk_pop_up_state.get() == 1) and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 1):
        screen_pop_up(game, page, lang, mode)
        screen_big_mega_super_win(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_and_additional_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_bonus_game(game, page, lang, mode)

    elif (chk_pop_up_state.get() == 1) and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 1) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 0):
        screen_pop_up(game, page, lang, mode)
        screen_paytable(game, page, lang, mode)
        screen_big_mega_super_win(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_and_additional_pop_up(game, page, lang, mode)

    #
    elif (chk_pop_up_state.get() == 1) and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 1) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 1):
        screen_pop_up(game, page, lang, mode)
        screen_paytable(game, page, lang, mode)
        screen_big_mega_super_win(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_bonus_game(game, page, lang, mode)

    #
    elif (chk_pop_up_state.get() == 1) and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 1):
        screen_pop_up(game, page, lang, mode)
        screen_freespin_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_and_additional_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_bonus_game(game, page, lang, mode)

    elif (chk_pop_up_state.get() == 1) and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 1) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 0):
        screen_pop_up(game, page, lang, mode)
        screen_paytable(game, page, lang, mode)
        screen_freespin_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_and_additional_pop_up(game, page, lang, mode)

    #
    elif (chk_pop_up_state.get() == 1) and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 1) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 1):
        screen_pop_up(game, page, lang, mode)
        screen_paytable(game, page, lang, mode)
        screen_freespin_and_additional_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_bonus_game(game, page, lang, mode)

    #
    elif (chk_pop_up_state.get() == 0) and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 0):
        page.keyboard.press("Enter")
        screen_main(game, page, lang, mode)
        screen_big_mega_super_win(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_and_additional_pop_up(game, page, lang, mode)

    elif (chk_pop_up_state.get() == 0) and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 1):
        page.keyboard.press("Enter")
        screen_main(game, page, lang, mode)
        screen_big_mega_super_win(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_bonus_game(game, page, lang, mode)

    elif (chk_pop_up_state.get() == 0) and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 1) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 0):
        page.keyboard.press("Enter")
        screen_main(game, page, lang, mode)
        screen_paytable(game, page, lang, mode)
        screen_big_mega_super_win(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_pop_up(game, page, lang, mode)
    #
    elif (chk_pop_up_state.get() == 0) and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 1):
        page.keyboard.press("Enter")
        screen_main(game, page, lang, mode)
        screen_big_mega_super_win(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_and_additional_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_bonus_game(game, page, lang, mode)

    #
    elif (chk_pop_up_state.get() == 0) and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 1):
        page.keyboard.press("Enter")
        screen_main(game, page, lang, mode)
        screen_freespin_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_and_additional_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_bonus_game(game, page, lang, mode)

    elif (chk_pop_up_state.get() == 0) and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 1) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 0):
        page.keyboard.press("Enter")
        screen_main(game, page, lang, mode)
        screen_paytable(game, page, lang, mode)
        screen_freespin_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_and_additional_pop_up(game, page, lang, mode)

    #
    elif (chk_pop_up_state.get() == 0) and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 1) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 1):
        page.keyboard.press("Enter")
        screen_main(game, page, lang, mode)
        screen_paytable(game, page, lang, mode)
        screen_freespin_and_additional_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_bonus_game(game, page, lang, mode)

    #
    elif (chk_pop_up_state.get() == 0) and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 1):
        page.keyboard.press("Enter")
        screen_big_mega_super_win(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_and_additional_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_bonus_game(game, page, lang, mode)

    elif (chk_pop_up_state.get() == 0) and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 1) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 0):
        page.keyboard.press("Enter")
        screen_paytable(game, page, lang, mode)
        screen_big_mega_super_win(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_and_additional_pop_up(game, page, lang, mode)

    #
    elif (chk_pop_up_state.get() == 0) and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 1) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 1):
        page.keyboard.press("Enter")
        screen_paytable(game, page, lang, mode)
        screen_freespin_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_and_additional_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_bonus_game(game, page, lang, mode)

    # 5
    elif (chk_pop_up_state.get() == 1) and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 0):
        screen_pop_up(game, page, lang, mode)
        screen_main(game, page, lang, mode)
        screen_big_mega_super_win(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_and_additional_pop_up(game, page, lang, mode)

    elif (chk_pop_up_state.get() == 1) and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 1):
        screen_pop_up(game, page, lang, mode)
        screen_main(game, page, lang, mode)
        screen_big_mega_super_win(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_bonus_game(game, page, lang, mode)

    elif (chk_pop_up_state.get() == 1) and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 1) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 0):
        screen_pop_up(game, page, lang, mode)
        screen_main(game, page, lang, mode)
        screen_paytable(game, page, lang, mode)
        screen_big_mega_super_win(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_pop_up(game, page, lang, mode)
    #
    elif (chk_pop_up_state.get() == 1) and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 1) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 0):
        screen_pop_up(game, page, lang, mode)
        screen_main(game, page, lang, mode)
        screen_big_mega_super_win(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_and_additional_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_bonus_game(game, page, lang, mode)

    elif (chk_pop_up_state.get() == 1) and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 1) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 0):
        screen_pop_up(game, page, lang, mode)
        screen_main(game, page, lang, mode)
        screen_paytable(game, page, lang, mode)
        screen_big_mega_super_win(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_and_additional_pop_up(game, page, lang, mode)

    #
    elif (chk_pop_up_state.get() == 1) and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 1):
        screen_pop_up(game, page, lang, mode)
        screen_main(game, page, lang, mode)
        screen_freespin_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_and_additional_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_bonus_game(game, page, lang, mode)

    elif (chk_pop_up_state.get() == 1) and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 1) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 0):
        screen_pop_up(game, page, lang, mode)
        screen_main(game, page, lang, mode)
        screen_paytable(game, page, lang, mode)
        screen_freespin_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_and_additional_pop_up(game, page, lang, mode)

    #
    elif (chk_pop_up_state.get() == 1) and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 1):
        screen_pop_up(game, page, lang, mode)
        screen_big_mega_super_win(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_and_additional_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_bonus_game(game, page, lang, mode)

    elif (chk_pop_up_state.get() == 1) and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 1) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 0):
        screen_pop_up(game, page, lang, mode)
        screen_paytable(game, page, lang, mode)
        screen_big_mega_super_win(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_and_additional_pop_up(game, page, lang, mode)

    #
    elif (chk_pop_up_state.get() == 1) and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 1) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 1):
        screen_pop_up(game, page, lang, mode)
        screen_paytable(game, page, lang, mode)
        screen_big_mega_super_win(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_bonus_game(game, page, lang, mode)

    #
    elif (chk_pop_up_state.get() == 1) and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 1) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 1):
        screen_pop_up(game, page, lang, mode)
        screen_paytable(game, page, lang, mode)
        screen_big_mega_super_win(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_and_additional_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_bonus_game(game, page, lang, mode)

    #
    elif (chk_pop_up_state.get() == 1) and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 1) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 1):
        screen_pop_up(game, page, lang, mode)
        screen_main(game, page, lang, mode)
        screen_paytable(game, page, lang, mode)
        screen_freespin_and_additional_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_bonus_game(game, page, lang, mode)

    elif (chk_pop_up_state.get() == 1) and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 1) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 1):
        screen_pop_up(game, page, lang, mode)
        screen_main(game, page, lang, mode)
        screen_paytable(game, page, lang, mode)
        screen_freespin_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_bonus_game(game, page, lang, mode)

    #
    elif (chk_pop_up_state.get() == 1) and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 1) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 1):
        screen_pop_up(game, page, lang, mode)
        screen_paytable(game, page, lang, mode)
        screen_freespin_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_and_additional_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_bonus_game(game, page, lang, mode)

    #
    elif (chk_pop_up_state.get() == 0) and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 1):
        page.keyboard.press("Enter")
        screen_main(game, page, lang, mode)
        screen_big_mega_super_win(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_and_additional_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_bonus_game(game, page, lang, mode)

    elif (chk_pop_up_state.get() == 0) and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 1) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 0):
        page.keyboard.press("Enter")
        screen_main(game, page, lang, mode)
        screen_paytable(game, page, lang, mode)
        screen_big_mega_super_win(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_and_additional_pop_up(game, page, lang, mode)

    #
    elif (chk_pop_up_state.get() == 0) and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 1) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 0) and (chk_bg_state.get() == 1):
        page.keyboard.press("Enter")
        screen_main(game, page, lang, mode)
        screen_paytable(game, page, lang, mode)
        screen_big_mega_super_win(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_bonus_game(game, page, lang, mode)

    #
    elif (chk_pop_up_state.get() == 0) and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 1):
        page.keyboard.press("Enter")
        screen_main(game, page, lang, mode)
        screen_paytable(game, page, lang, mode)
        screen_big_mega_super_win(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_and_additional_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_bonus_game(game, page, lang, mode)

    #
    elif (chk_pop_up_state.get() == 0) and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 1) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 1):
        page.keyboard.press("Enter")
        screen_main(game, page, lang, mode)
        screen_paytable(game, page, lang, mode)
        screen_freespin_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_and_additional_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_bonus_game(game, page, lang, mode)

    #
    elif (chk_pop_up_state.get() == 0) and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 1) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 1):
        page.keyboard.press("Enter")
        screen_paytable(game, page, lang, mode)
        screen_big_mega_super_win(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_and_additional_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_bonus_game(game, page, lang, mode)

    # 6
    elif (chk_pop_up_state.get() == 1) and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 0) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 1):
        screen_pop_up(game, page, lang, mode)
        screen_main(game, page, lang, mode)
        screen_big_mega_super_win(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_and_additional_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_bonus_game(game, page, lang, mode)

    elif (chk_pop_up_state.get() == 1) and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 1) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 0):
        screen_pop_up(game, page, lang, mode)
        screen_main(game, page, lang, mode)
        screen_paytable(game, page, lang, mode)
        screen_big_mega_super_win(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_and_additional_pop_up(game, page, lang, mode)

    #
    elif (chk_pop_up_state.get() == 1) and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 1) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 1):
        screen_pop_up(game, page, lang, mode)
        screen_main(game, page, lang, mode)
        screen_paytable(game, page, lang, mode)
        screen_big_mega_super_win(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_and_additional_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_bonus_game(game, page, lang, mode)

    #
    elif (chk_pop_up_state.get() == 1) and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 0) \
            and (chk_paytable_state.get() == 1) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 1):
        screen_pop_up(game, page, lang, mode)
        screen_main(game, page, lang, mode)
        screen_paytable(game, page, lang, mode)
        screen_freespin_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_and_additional_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_bonus_game(game, page, lang, mode)

    #
    elif (chk_pop_up_state.get() == 1) and (chk_main_state.get() == 0) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 1) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 1):
        screen_pop_up(game, page, lang, mode)
        screen_paytable(game, page, lang, mode)
        screen_big_mega_super_win(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_and_additional_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_bonus_game(game, page, lang, mode)

    #
    elif (chk_pop_up_state.get() == 1) and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 1) and (chk_fs_pop_up_state.get() == 0) \
            and (chk_fs_add_state.get() == 1) and (chk_bg_state.get() == 1):
        screen_pop_up(game, page, lang, mode)
        screen_main(game, page, lang, mode)
        screen_paytable(game, page, lang, mode)
        screen_big_mega_super_win(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_and_additional_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_bonus_game(game, page, lang, mode)

    #
    if chk_pop_up_state.get() == 1 and (chk_main_state.get() == 1) and (
            chk_big_super_mega_state.get() == 1) \
            and (chk_paytable_state.get() == 1) and (chk_fs_pop_up_state.get() == 1) \
            and (chk_fs_pop_up_state.get() == 1) and (chk_bg_state.get() == 1):
        screen_pop_up(game, page, lang, mode)
        screen_main(game, page, lang, mode)
        screen_paytable(game, page, lang, mode)
        screen_big_mega_super_win(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_freespin_and_additional_pop_up(game, page, lang, mode)
        page.reload()
        time.sleep(20)
        page.keyboard.press("Enter")
        screen_bonus_game(game, page, lang, mode)


window = Tk()
window.geometry('290x425')
window.title("Locals screenshots")

fake_lbl = Label(window, text="")
fake_lbl.grid(column=3, row=0)

screenshot_select = Label(window, text="Screen: ")
screenshot_select.grid(column=0, row=1)

fake_lbl1 = Label(window, text="")
fake_lbl1.grid(column=1, row=4)

page_size = Label(window, text="Page size: ")
page_size.grid(column=0, row=5)

fake_lbl3 = Label(window, text="")
fake_lbl3.grid(column=1, row=8)

modes_choose = Label(window, text="Modes: ")
modes_choose.grid(column=0, row=9)

chk_mobile_landscape_state = IntVar()
chk_mobile_portrait_state = IntVar()
chk_desktop_state = IntVar()
chk_pop_up_state = IntVar()
chk_main_state = IntVar()
chk_big_super_mega_state = IntVar()
chk_fs_pop_up_state = IntVar()
chk_fs_add_state = IntVar()
chk_bg_state = IntVar()
chk_paytable_state = IntVar()
chk_screenshot_all_time = IntVar()
chk_screenshot_manual = IntVar()
chk_without_screenshot = IntVar()

chkbtn_screenshot_all_time = Checkbutton(window, text="Auto screenshots", variable=chk_screenshot_all_time, onvalue=1,
                                         offvalue=0)
chkbtn_screenshot_all_time.grid(column=1, row=1)

chkbtn_screenshot_manual = Checkbutton(window, text="Manual screenshots", variable=chk_screenshot_manual, onvalue=1,
                                       offvalue=0)
chkbtn_screenshot_manual.grid(column=1, row=2)

chkbtn_without_screenshot = Checkbutton(window, text="Without screenshots", variable=chk_without_screenshot, onvalue=1,
                                        offvalue=0)
chkbtn_without_screenshot.grid(column=1, row=3)

chkbtn_mobile_landscape = Checkbutton(window, text="Mobile Portrait", variable=chk_mobile_landscape_state, onvalue=1,
                                      offvalue=0)
chkbtn_mobile_landscape.grid(column=1, row=5)

chkbtn_mobile_portrait = Checkbutton(window, text="Mobile Landscape", variable=chk_mobile_portrait_state, onvalue=1,
                                     offvalue=0)
chkbtn_mobile_portrait.grid(column=1, row=6)

chkbtn_desktop = Checkbutton(window, text="Desktop", variable=chk_desktop_state, onvalue=1, offvalue=0)
chkbtn_desktop.grid(column=1, row=7)

feature_preview_chkbtn = Checkbutton(window, text="Feature Preview", variable=chk_pop_up_state, onvalue=1,
                                     offvalue=0)
feature_preview_chkbtn.grid(column=1, row=9)

main_chkbtn = Checkbutton(window, text="Main", variable=chk_main_state, onvalue=1, offvalue=0)
main_chkbtn.grid(column=1, row=10)

big_mega_super_chkbtn = Checkbutton(window, text=" Big/Super/Mega Win ", variable=chk_big_super_mega_state, onvalue=1,
                                    offvalue=0)
big_mega_super_chkbtn.grid(column=1, row=11)

fs_chkbtn = Checkbutton(window, text="FS Pop Up", variable=chk_fs_pop_up_state, onvalue=1, offvalue=0)
fs_chkbtn.grid(column=1, row=12)

fs_add_chkbtn = Checkbutton(window, text="Additional FS", variable=chk_fs_add_state, onvalue=1, offvalue=0)
fs_add_chkbtn.grid(column=1, row=13)

bg_chkbtn = Checkbutton(window, text="BG Pop Up", variable=chk_bg_state, onvalue=1, offvalue=0)
bg_chkbtn.grid(column=1, row=14)

paytable_chkbtn = Checkbutton(window, text="Paytable", variable=chk_paytable_state, onvalue=1, offvalue=0)
paytable_chkbtn.grid(column=1, row=15)

fake_lbl4 = Label(window, text="")
fake_lbl4.grid(column=0, row=16)

start_testing_btn = Button(window, text="Start locals testing", command=start_testing)
start_testing_btn.grid(column=1, row=18)

window.mainloop()
