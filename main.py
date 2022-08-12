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
                        f"https://dgm-beta.ps-gamespace.com/launch?link_title={branch}&gameName={game}_mob&partner={branch}-gs-beta-platform-new&key=test50000&viewid=gameFrame&lang={lang}")
                    time.sleep(15)
                    if chk_pop_up_state.get() == 1:
                        screen_pop_up(game, page, lang, mode)
                    if chk_main_state.get() == 1:
                        screen_main(game, page, lang, mode)
                    if chk_big_super_mega_state.get() == 1:
                        screen_big_mega_super_win(game, page, lang, mode)
                    if chk_paytable_state.get() == 1:
                        screen_paytable(game, page, lang, mode)
                    if chk_fs_pop_up_state.get() == 1:
                        screen_freespin_pop_up(game, page, lang, mode)
                    if chk_fs_add_state.get() == 1:
                        screen_freespin_and_additional_pop_up(game, page, lang, mode)
                    if chk_bg_state.get() == 1:
                        screen_bonus_game(game, page, lang, mode)
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
                        f"https://dgm-beta.ps-gamespace.com/launch?link_title={branch}&gameName={game}_mob&partner={branch}-gs-beta-platform-new&key=test50000&viewid=gameFrame&lang={lang}")
                    time.sleep(15)
                    if chk_pop_up_state.get() == 1:
                        screen_pop_up(game, page, lang, mode)
                    if chk_main_state.get() == 1:
                        screen_main(game, page, lang, mode)
                    if chk_big_super_mega_state.get() == 1:
                        screen_big_mega_super_win(game, page, lang, mode)
                    if chk_paytable_state.get() == 1:
                        screen_paytable(game, page, lang, mode)
                    if chk_fs_pop_up_state.get() == 1:
                        screen_freespin_pop_up(game, page, lang, mode)
                    if chk_fs_add_state.get() == 1:
                        screen_freespin_and_additional_pop_up(game, page, lang, mode)
                    if chk_bg_state.get() == 1:
                        screen_bonus_game(game, page, lang, mode)
                    languages_checked += 1
                    print(f"[{lang}] CHECKED [{languages_checked}/{lenght_languages}]")
                    print("- - - - - - -")

            print(f'[{game}][{mode}]: CHECKED [{modes_checked}/{lenght_modes}]')
            print("===============================")

        else:
            modes_checked = + 1
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=False, channel="chrome")
                page = browser.new_page()
                languages_checked = 0
                for lang in languages:
                    print(f"[{lang}] in work [{languages_checked}/{lenght_languages}]")
                    page.goto(
                        f"https://dgm-beta.ps-gamespace.com/launch?link_title={branch}&gameName={game}&partner={branch}-gs-beta-platform-new&key=test50000&viewid=gameFrame&lang={lang}")
                    time.sleep(15)
                    if chk_pop_up_state.get() == 1:
                        screen_pop_up(game, page, lang, mode)
                    if chk_main_state.get() == 1:
                        screen_main(game, page, lang, mode)
                    if chk_big_super_mega_state.get() == 1:
                        screen_big_mega_super_win(game, page, lang, mode)
                    if chk_paytable_state.get() == 1:
                        screen_paytable(game, page, lang, mode)
                    if chk_fs_pop_up_state.get() == 1:
                        screen_freespin_pop_up(game, page, lang, mode)
                    if chk_fs_add_state.get() == 1:
                        screen_freespin_and_additional_pop_up(game, page, lang, mode)
                    if chk_bg_state.get() == 1:
                        screen_bonus_game(game, page, lang, mode)
                    languages_checked += 1
                    print(f"[{lang}] CHECKED [{languages_checked}/{lenght_languages}]")
                    print("- - - - - - -")
            print(f'[{game}][{mode}]: CHECKED [{modes_checked}/{lenght_modes}]')
            print("===============================")


def screen_pop_up(game_name, page, lang, mode):
    page.click('//*[@id="game_canvas"]')
    page.screenshot(path=f"{game_name}/{lang}/{mode}/screen_pop_up_{lang}.png")
    page.keyboard.press("Enter")
    print("Screen [Pop Up] - done")


def screen_main(game_name, page, lang, mode):
    page.click('//*[@id="game_canvas"]')
    page.screenshot(path=f"{game_name}/{lang}/{mode}/main_{lang}.png")
    print("Screen [Main Game] - done")


def screen_big_mega_super_win(game_name, page, lang, mode):
    shifts = ""
    with open("config.json") as file:
        config = json.load(file)
        shifts = "".join(config['shifts'].get("big_super_mega_win"))

    page.wait_for_selector('//*[text()="Open Controls"]').click()
    page.wait_for_selector('//*[text()="shifter"]').click()
    with page.context.expect_page() as tab:
        new_tab = tab.value

        time.sleep(2)
        new_tab.wait_for_selector('//select[@class="game-list-select"]').click()
        time.sleep(1)
        new_tab.wait_for_selector('//input[@class="combination-edit-input"]').click()
        time.sleep(1)
        new_tab.wait_for_selector('//input[@class="combination-edit-input"]').fill(shifts)
        time.sleep(1)
        new_tab.wait_for_selector('//input[@class="combination-edit-input"]').click()
        time.sleep(2)
        new_tab.keyboard.press("Tab")
        new_tab.keyboard.press("Enter")
        new_tab.wait_for_selector('//*[contains(text(), "Clear & Send")]').click()

        time.sleep(2)
        new_tab.close()

    page.wait_for_selector('//*[text()="Close Controls"]').click()
    page.click('//*[@id="game_canvas"]')
    page.keyboard.press("Space")
    time.sleep(7)
    page.click('//*[@id="game_canvas"]')
    time.sleep(1)
    page.screenshot(path=f"{game_name}/{lang}/{mode}/screen_big_win_{lang}.png")
    print("Screen [Big Win Pop Up] - done")
    time.sleep(2)
    page.click('//*[text()="Open Controls"]')
    time.sleep(1)
    page.click('//*[text()="Close Controls"]')
    page.keyboard.press("Space")
    time.sleep(7)
    page.click('//*[@id="game_canvas"]')
    time.sleep(1)
    page.screenshot(path=f"{game_name}/{lang}/{mode}/screen_mega_win_{lang}.png")
    print("Screen [Super Win Pop Up] - done")
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
    print("Screen [Mega Win Pop Up] - done")
    time.sleep(2)
    page.click('//*[text()="Open Controls"]')
    time.sleep(1)
    page.click('//*[text()="Close Controls"]')
    page.keyboard.press("Space")


def screen_freespin_pop_up(game_name, page, lang, mode):
    # time.sleep(2)
    # page.click('//*[text()="Open Controls"]')
    # time.sleep(1)
    # page.click('//*[text()="Close Controls"]')

    shifts = ""
    with open("config.json") as file:
        config = json.load(file)
        shifts = "".join(config['shifts'].get("free_spin_shift"))

    page.wait_for_selector('//*[text()="Open Controls"]').click()
    page.wait_for_selector('//*[text()="shifter"]').click()
    with page.context.expect_page() as t:
        new_tab = t.value
        time.sleep(2)
        new_tab.wait_for_selector('//select[@class="game-list-select"]').click()
        time.sleep(1)
        time.sleep(2)
        new_tab.wait_for_selector('//input[@class="combination-edit-input"]').click()
        time.sleep(1)
        new_tab.wait_for_selector('//input[@class="combination-edit-input"]').fill(shifts)
        time.sleep(1)
        new_tab.wait_for_selector('//input[@class="combination-edit-input"]').click()
        time.sleep(2)
        new_tab.keyboard.press("Tab")
        new_tab.keyboard.press("Enter")
        new_tab.wait_for_selector('//*[contains(text(), "Clear & Send")]').click()

        time.sleep(2)
        new_tab.close()

    page.wait_for_selector('//*[text()="Close Controls"]').click()
    page.click('//*[@id="game_canvas"]')
    page.keyboard.press("Enter")
    time.sleep(15)
    page.screenshot(path=f"{game_name}/{lang}/{mode}/free_spin_pop_up_{lang}.png")
    print("Screen [Free Spin Pop Up] - done")


def screen_freespin_and_additional_pop_up(game_name, page, lang, mode):
    shifts = ""
    with open("config.json") as file:
        config = json.load(file)
        shifts_fs_add = "".join(config['shifts'].get("free_spin_shift_and_add_spins"))

    page.wait_for_selector('//*[text()="Open Controls"]').click()
    page.wait_for_selector('//*[text()="shifter"]').click()
    with page.context.expect_page() as tab2:
        new_tab2 = tab2.value
        time.sleep(2)
        new_tab2.wait_for_selector('//input[@class="combination-edit-input"]').click()
        time.sleep(1)
        new_tab2.wait_for_selector('//input[@class="combination-edit-input"]').fill(shifts_fs_add)
        time.sleep(1)
        new_tab2.wait_for_selector('//input[@class="combination-edit-input"]').click()
        time.sleep(2)
        new_tab2.keyboard.press("Tab")
        new_tab2.keyboard.press("Enter")
        new_tab2.wait_for_selector('//*[contains(text(), "Clear & Send")]').click()

        time.sleep(2)
        new_tab2.close()

    page.wait_for_selector('//*[text()="Close Controls"]').click()
    page.click('//*[@id="game_canvas"]')
    page.keyboard.press("Enter")
    time.sleep(15)
    page.screenshot(path=f"{game_name}/{lang}/{mode}/free_spin_pop_up_{lang}.png")
    print("Screen [Free Spin Pop Up] - done")
    page.keyboard.press("Enter")
    time.sleep(10)
    page.click('//*[@id="game_canvas"]')
    time.sleep(1)
    page.screenshot(path=f"{game_name}/{lang}/{mode}/free_spin_add_{lang}.png")
    print("Screen [Add Free Spin Pop Up] - done")


def screen_bonus_game(game_name, page, lang, mode):
    shifts = ""
    with open("config.json") as file:
        config = json.load(file)
        shifts = "".join(config['shifts'].get("bonus_game_shift"))

    page.wait_for_selector('//*[text()="Open Controls"]').click()
    page.wait_for_selector('//*[text()="shifter"]').click()
    with page.context.expect_page() as t:
        new_tab = t.value
        time.sleep(2)

        new_tab.wait_for_selector('//select[@class="game-list-select"]').click()
        time.sleep(2)
        new_tab.wait_for_selector('//input[@class="combination-edit-input"]').click()
        time.sleep(1)
        new_tab.wait_for_selector('//input[@class="combination-edit-input"]').fill(shifts)
        time.sleep(1)
        new_tab.wait_for_selector('//input[@class="combination-edit-input"]').click()
        time.sleep(2)
        new_tab.keyboard.press("Tab")
        new_tab.keyboard.press("Enter")
        new_tab.wait_for_selector('//*[contains(text(), "Clear & Send")]').click()

        time.sleep(2)
        new_tab.close()

    page.wait_for_selector('//*[text()="Close Controls"]').click()
    page.click('//*[@id="game_canvas"]')
    page.keyboard.press("Enter")
    time.sleep(15)
    page.screenshot(path=f"{game_name}/{lang}/{mode}/bonus_game_pop_up_{lang}.png")
    print("Screen [Bonus Game Pop Up] - done")


def screen_paytable(game_name, page, lang, mode):
    time.sleep(2)
    page.click('//*[text()="Open Controls"]')
    time.sleep(1)
    page.click('//*[text()="Close Controls"]')
    page.click('//*[@id="game_canvas"]')
    page.keyboard.press("i")
    page.click('//*[@id="game_canvas"]')
    time.sleep(2)

    for i in range(12):
        page.screenshot(path=f"{game_name}/{lang}/{mode}/paytable_{lang}_{i}.png")
        page.mouse.wheel(0, 125)

    print("Screen [Paytable] - done")
    page.click('//*[@id="game_canvas"]')
    page.keyboard.press("Escape")


window = Tk()
window.geometry('325x325')
window.title("Locals screenshots")

fake_lbl = Label(window, text="")
fake_lbl.grid(column=3, row=0)

page_size = Label(window, text="Page size: ")
page_size.grid(column=0, row=1)

fale_lbl1 = Label(window, text="")
fale_lbl1.grid(column=1, row=4)

modes_choose = Label(window, text="Choose modes: ")
modes_choose.grid(column=0, row=5)

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

chkbtn_mobile_landscape = Checkbutton(window, text="Mobile Portrait", variable=chk_mobile_landscape_state, onvalue=1,
                                      offvalue=0)
chkbtn_mobile_landscape.grid(column=1, row=1)

chkbtn_mobile_portrait = Checkbutton(window, text="Mobile Landscape", variable=chk_mobile_portrait_state, onvalue=1,
                                     offvalue=0)
chkbtn_mobile_portrait.grid(column=1, row=2)

chkbtn_desktop = Checkbutton(window, text="Desktop", variable=chk_desktop_state, onvalue=1, offvalue=0)
chkbtn_desktop.grid(column=1, row=3)

pop_up_chkbtn = Checkbutton(window, text="Pop Up".center(30), variable=chk_pop_up_state, onvalue=1, offvalue=0)
pop_up_chkbtn.grid(column=1, row=5)

main_chkbtn = Checkbutton(window, text="  Main ".center(32), variable=chk_main_state, onvalue=1, offvalue=0)
main_chkbtn.grid(column=1, row=6)

big_mega_super_chkbtn = Checkbutton(window, text=" Big/Super/Mega Win ", variable=chk_big_super_mega_state, onvalue=1,
                                    offvalue=0)
big_mega_super_chkbtn.grid(column=1, row=7)

fs_chkbtn = Checkbutton(window, text="FS Pop Up".center(28), variable=chk_fs_pop_up_state, onvalue=1, offvalue=0)
fs_chkbtn.grid(column=1, row=8)

fs_add_chkbtn = Checkbutton(window, text="FS Pop Up + add".center(23), variable=chk_fs_add_state, onvalue=1, offvalue=0)
fs_add_chkbtn.grid(column=1, row=9)

bg_chkbtn = Checkbutton(window, text="BG Pop Up".center(27), variable=chk_bg_state, onvalue=1, offvalue=0)
bg_chkbtn.grid(column=1, row=10)

paytable_chkbtn = Checkbutton(window, text="Paytable".center(30), variable=chk_paytable_state, onvalue=1, offvalue=0)
paytable_chkbtn.grid(column=1, row=11)

fake_lbl3 = Label(window, text="")
fake_lbl3.grid(column=0, row=12)
fake_lbl4 = Label(window, text="")
fake_lbl4.grid(column=0, row=14)

start_testing_btn = Button(window, text="Start locals testing", command=start_testing)
start_testing_btn.grid(column=1, row=13)

window.mainloop()
