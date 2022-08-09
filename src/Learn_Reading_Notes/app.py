# TODO
# add missing notes (0-3)
# change b* files to bass key

"""
Learn Reading Notes!
"""
import random
import toga
from toga import App, Box, MainWindow
from toga import ImageView, Image
from toga.style import Pack
from toga.style.pack import ROW, COLUMN
from toga.constants import CENTER


class learnreadingnotes(toga.App):

    def startup(self):
        self.box_main = toga.Box(style=Pack(direction=COLUMN))

        self.key = "v"

        box_header = toga.Box()
        # box_header = toga.Box(style=Pack(direction=ROW))
        self.lbl_status = toga.Label(
            '0/0',
            style=Pack(padding=3, text_align=CENTER)
        )
        spacer = toga.Label(
            " ",
            style=Pack(flex=1)
        )
        self.btn_change_key = toga.Button(
            self.key.upper(),
            on_press=self.__btn_change_key,
            style=Pack(padding=3, text_align=CENTER)
        )
        box_header.add(self.lbl_status, spacer, self.btn_change_key)

        self.img = toga.ImageView(style=Pack(flex=1))
        self.__new_img()

        self.txt_input = toga.TextInput(style=Pack(flex=1))

        self.lbl_res = toga.Label(
            '',
            style=Pack(padding=5, text_align=CENTER)
        )

        self.btn_see_res = toga.Button(
            "check",
            on_press=self.btn_next,
            style=Pack(padding=5)
        )

        self.box_main.add(
            box_header,
            self.img,
            self.btn_see_res,
            self.lbl_res,
            self.txt_input
        )

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.box_main
        self.main_window.show()

    def __btn_change_key(self, btn):
        if self.key == "b":
            self.key = "v"
        else:
            self.key = "b"
        self.btn_change_key.label = self.key.upper()
        self.__update_img()

    def __update_img(self):
        try:
            self.img.image = toga.Image(f"./img/{self.key}{self.result[1]}.png")
            self.img.refresh
        except:
            self.img.image = toga.Image(f"./img/{self.key}{self.result[1][:len(self.result[1]) - 1]}.png")
            self.img.refresh

    def __new_img(self):
        self.result = random.choice(ARR_IMG)
        self.__update_img()

    def btn_next(self, widget):
        if self.btn_see_res.label == "next":
            self.btn_see_res.label = "check Result"
            self.__new_img()
            self.lbl_res.text = ""
            self.txt_input.value = ""
        elif self.txt_input.value.lower() == self.result[0].lower():
            self.__new_img()
            self.lbl_res.text = "RIGHT"
            self.txt_input.value = ""
            status = self.lbl_status.text.split("/")
            self.lbl_status.text = f"{int(status[0]) + 1}/{int(status[1]) + 1}"
        else:
            self.lbl_res.text = f"WRONG: it would have been: {self.result[0]}"
            self.btn_see_res.label = "next"
            status = self.lbl_status.text.split("/")
            self.lbl_status.text = f"{status[0]}/{int(status[1]) + 1}"


def main():
    return learnreadingnotes()


ARR_IMG = [
    ["a", "a"],
    ["a", "a0"],
    ["ais", "ais"],
    ["ais", "ais0"],
    ["as", "as"],
    ["as", "as0"],
    # ["bes", "b"], # HERE english version
    # ["bes", "b0"], # HERE english version
    # ["bes", "b2"], # HERE english version
    ["b", "b"], # HERE german version
    ["b", "b0"], # HERE german version
    ["b", "b2"], # HERE german version
    ["c", "c"],
    ["c", "c2"],
    ["c", "c3"],
    ["ces", "ces"],
    ["ces", "ces2"],
    ["ces", "ces3"],
    ["cis", "cis"],
    ["cis", "cis2"],
    ["d", "d"],
    ["d", "d2"],
    ["d", "d3"],
    ["des", "des"],
    ["des", "des"],
    ["des", "des2"],
    ["des", "des3"],
    ["dis", "dis"],
    ["dis", "dis2"],
    ["dis", "dis3"],
    ["e", "e"],
    ["e", "e2"],
    ["eis", "eis"],
    ["eis", "eis2"],
    ["es", "es"],
    ["es", "es2"],
    ["f", "f"],
    ["f", "f2"],
    ["fes", "fes"],
    ["fes", "fes2"],
    ["fis", "fis"],
    ["fis", "fis2"],
    ["g", "g"],
    ["g", "g0"],
    ["g", "g2"],
    ["ges", "ges"],
    ["ges", "ges0"],
    ["ges", "ges2"],
    ["gis", "gis"],
    ["gis", "gis0"],
    ["gis", "gis2"],
    # ["b", "h"], # HERE english version
    # ["b", "h0"], # HERE english version
    # ["b", "h2"], # HERE english version
    ["h", "h"], # HERE german version
    ["h", "h0"], # HERE german version
    ["h", "h2"], # HERE german version
    ["his", "his"],
    ["his", "his0"],
    ["his", "his2"]
]
