from pywinauto import *
import wx
from pyautogui import *


files = []

app1 = wx.App(redirect=False)
frame = wx.Frame(None, title='')
# wxPython open dialog select studiable files.
openFileDialog = wx.FileDialog(frame, "Open", style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST | wx.FD_MULTIPLE)
openFileDialog.CenterOnScreen()
# shows the dialog on screen
result = openFileDialog.ShowModal()
# only opens the file if 'open' in dialog is pressed otherwise if 'cancel' in dialog is pressed closes dialog
if result == wx.ID_OK:
    # gets the file path
    filepaths = openFileDialog.GetPaths()

    for path in filepaths:

        files.append(path)

# -------- Launch MountainsMap ------------
app = Application().start(cmd_line=u'"C:\\Program Files\\Digital Surf\\MountainsMap Premium 7.4\\Bin\\Mountains.exe" ')
window = app.Dialog
# ---- Check that mmaps is loaded wait until to click events ------
if app.active():
    print('active')
# check if main window is visible
if window.is_visible():
    print('visible')
time.sleep(2)
window.maximize()
time.sleep(3)
# ---- process all files ----
for file in files:
    time.sleep(3)
    # ------ load a studiable *only 2D image of surface* --------
    window.type_keys('{F4}')
    # print([wnd.window_text() for wnd in app.windows()])
    file_path = file.replace('\\\\', '\\')
    print(file_path)
    time.sleep(2)
    file_name = window['File &name:Edit']
    # file_name.print_control_identifiers()
    file_name.set_edit_text(file_path)
    time.sleep(2)
    open_btn = window['&OpenButton']
    open_btn.click_input()
    time.sleep(4)

    click(540, 110)
    time.sleep(1)
    # moveTo(540, 150, 0.2)
    click(540, 150)
    save_as = window['Save As']
    time.sleep(2)
    file_name_save = window['Edit']
    file_ = file_path.split('\\')[5]
    file_name_save.set_edit_text(file_)
    time.sleep(0.5)
    save_btn = window['&SaveAs']
    save_btn.click_input()

    time.sleep(2)

    ppN = Application().connect(title=u'Photos')
    c = ppN.Photos
    c.close()

    time.sleep(1)
    window.type_keys('^N')
    time.sleep(1)
    test = window
    time.sleep(1)
    test.type_keys('{TAB}')
    time.sleep(1)
    test.type_keys('{ENTER}')

    # print([wnd.window_text() for wnd in app.windows()])
    # xtptoolbar = window['The Ribbon']
    # time.sleep(2)
    # xtptoolbar.set_focus()
    # # xtptoolbar.click(button='left', pressed='', coords=(300, 45), double=False, absolute=False)
    # xtptoolbar.click(button='left', pressed='', coords=(540, 110), double=False, absolute=False)
    # time.sleep(1)
    # xtptoolbar.click(button='left', pressed='', coords=(540, 115), double=False, absolute=False)

