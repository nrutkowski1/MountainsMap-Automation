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

print('Open files')
# only opens the file if 'open' in dialog is pressed otherwise if 'cancel' in dialog is pressed closes dialog
if result == wx.ID_OK:
    # gets the file path
    filepaths = openFileDialog.GetPaths()

    for path in filepaths:

        files.append(path)

# -------- Launch MountainsMap ------------
app = Application().start(cmd_line=u'"C:\\Program Files\\Digital Surf\\MountainsMap Premium 7.4\\Bin\\Mountains.exe" ')
# app = Application().connect(title=u'MountainsMap\xae Imaging Topography - Untitled document*', class_name='#32770')
time.sleep(20)
window = app.Dialog
# ---- Check that mmaps is loaded wait until to click events ------
time.sleep(5)
if app.active():
    print('active')
# check if main window is visible
if window.is_visible():
    print('visible')
time.sleep(5)
window.maximize()
time.sleep(3)
# ---- process all files ----
for file in files:
    time.sleep(5)
    # ------ load a studiable *only 2D image of surface* --------
    window.type_keys('{F4}')

    # print([wnd.window_text() for wnd in app.windows()])
    file_path = file.replace('\\\\', '\\')
    print(file_path)
    time.sleep(1)
    file_name = window['File &name:Edit']
    # file_name.print_control_identifiers()
    file_name.set_edit_text(file_path)
    time.sleep(1)
    open_btn = window['&OpenButton']
    open_btn.click_input()

    time.sleep(150)

    # ------ Multiscale Analysis with default 200 scales ------
    xtptoolbar = window['The Ribbon']
    time.sleep(5)
    xtptoolbar.set_focus()
    xtptoolbar.click(button='left', pressed='', coords=(300, 45), double=False, absolute=False)
    # for interpolated surfaces
    xtptoolbar.click(button='left', pressed='', coords=(550, 90), double=False, absolute=False)
    # for no interpolations .plux files
    # xtptoolbar.click(button='left', pressed='', coords=(350, 90), double=False, absolute=False)
    time.sleep(1)
    # xtpstatusbar = window['ReadyXTPStatusBar']
    # xtpstatusbar = window['...']
    # time.sleep(1)
    # xtpstatusbar.set_focus()
    # xtpstatusbar.wait('ready', 300, 0.1)
    time.sleep(400)

    # ----- export file make sure that you select folder to save to ahead of time do not run with data that will save
    #       with same name due to Mmaps auto naming system----------
    xtptoolbar.set_focus()
    xtptoolbar.click(button='left', pressed='', coords=(1050, 90), double=False, absolute=False)

    # ----- saving ----------------
    window.set_focus()
    time.sleep(1)
    save_btn = window['&Save:Button']
    time.sleep(1)
    save_btn.click_input()
    # save_btn.print_control_identifiers()

    # ---- Connect to notepad that opens -----
    time.sleep(2)
    appN = Application().connect(title_re='.*Notepad*.')
    notepad = appN.Notepad
    notepad.close()
    # ----- Connect back to mmaps create new doc --------
    time.sleep(2)
    window.type_keys('^N')
    time.sleep(2)
    test = window
    time.sleep(2)
    test.type_keys('{TAB}')
    time.sleep(2)
    test.type_keys('{ENTER}')
    # test = window['Open a studiable']
    # test.print_control_identifiers()

    # need to figure out how to not execute the next command until the previous has occurred prevent code from
    # throwing errors
    # and breaking in the middle of the night during a big data process.

