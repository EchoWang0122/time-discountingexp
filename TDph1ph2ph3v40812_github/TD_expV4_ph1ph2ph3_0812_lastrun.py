#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on 六  8/13 00:01:08 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'test'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/wangshuning/Desktop/RA/time_discounting/timediscountingexpV4(0805)v2/TDph1ph2ph3v40812/TD_expV4_ph1ph2ph3_0812_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color='white', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "intro"
introClock = core.Clock()
introduction = visual.TextStim(win=win, name='introduction',
    text='欢迎您参加此社会认知与决策相关的实验。\n\n本实验为您随机生成了一个头像，\n请您填写您的昵称，填写完成后，请点击“下一页”。',
    font='STSong',
    pos=(0, 0.05), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
input_name = visual.TextBox2(
     win, text=None, font='Songti SC',
     pos=(0, -0.3),     letterHeight=0.05,
     size=(None, None), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0,
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=True,
     name='input_name',
     autoLog=True,
)
image_myself = visual.ImageStim(
    win=win,
    name='image_myself', 
    image='img/img_person/myself.png', mask=None,
    ori=0.0, pos=(0, -0.15), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
image_nextbutton = visual.ImageStim(
    win=win,
    name='image_nextbutton', 
    image='img/img_button/3button.jpg', mask=None,
    ori=0.0, pos=(0.5, -0.4), size=(0.2, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
mouse_3 = event.Mouse(win=win)
x, y = [None, None]
mouse_3.mouseClock = core.Clock()

# Initialize components for Routine "waiting_phase"
waiting_phaseClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='其他实验参与者在进入中，请稍候…',
    font='STSong',
    pos=(0.05, 0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_1 = visual.TextStim(win=win, name='text_1',
    text='',
    font='Open Sans',
    pos=(-0.06, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
text_2 = visual.TextStim(win=win, name='text_2',
    text='',
    font='Open Sans',
    pos=(-0.06, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
text_3 = visual.TextStim(win=win, name='text_3',
    text='',
    font='Open Sans',
    pos=(-0.06, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
text_4 = visual.TextStim(win=win, name='text_4',
    text='',
    font='Open Sans',
    pos=(-0.06, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
text_5 = visual.TextStim(win=win, name='text_5',
    text='           已经有              名实验参与者进入',
    font='STSong',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "phase1intro_2"
phase1intro_2Clock = core.Clock()
image_phase1intro = visual.ImageStim(
    win=win,
    name='image_phase1intro', 
    image='img/img_instruction/ph1intro.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.2,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp = keyboard.Keyboard()

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
text_fixation = visual.TextStim(win=win, name='text_fixation',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "phase1"
phase1Clock = core.Clock()
image_horrible = visual.ImageStim(
    win=win,
    name='image_horrible', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.6, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
image_evl1 = visual.ImageStim(
    win=win,
    name='image_evl1', 
    image='img/img_horriblethreat/hopic_evl0.png', mask=None,
    ori=0.0, pos=(0, 0.1), size=(1.2,0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
image_3button = visual.ImageStim(
    win=win,
    name='image_3button', 
    image='img/img_button/3button.jpg', mask=None,
    ori=0.0, pos=(0.5, -0.4), size=(0.2, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_2.mouseClock = core.Clock()
slider_2 = visual.Slider(win=win, name='slider_2',
    startValue=None, size=(1, 0.05), pos=(0, -0.1), units=None,
    labels=None, ticks=(1,10), granularity=0.1,
    style='rating', styleTweaks=(), opacity=None,
    color='LightGray', fillColor='Red', borderColor='black', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, depth=-4, readOnly=False)
text_6 = visual.TextStim(win=win, name='text_6',
    text='非常消极',
    font='STSong',
    pos=(-0.5, -0.2), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
text_7 = visual.TextStim(win=win, name='text_7',
    text='一点都不消极',
    font='STSong',
    pos=(0.46, -0.2), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);

# Initialize components for Routine "phase2intro"
phase2introClock = core.Clock()
image_phase2intro = visual.ImageStim(
    win=win,
    name='image_phase2intro', 
    image='img/img_instruction/ph2intro.png', mask=None,
    ori=0.0, pos=(0, 0.15), size=(1.2, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_5 = keyboard.Keyboard()
image_12 = visual.ImageStim(
    win=win,
    name='image_12', 
    image='img/img_axis/ax1.png', mask=None,
    ori=0.0, pos=(0, -0.1), size=(0.2, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# Initialize components for Routine "Phase2"
Phase2Clock = core.Clock()
list_1 = [1,2,3,4,5,6,7,8,9]
list_2 = [1,2,3,4,5,6,7,8,9]
list_3 = [1,2,3,4,5,6,7,8,9]
list_4 = [1,2,3,4,5,6,7,8,9]
pic_1 = ''
pic_2 = ''
pic_3 = ''
pic_4 = ''
loc_x_1 = 0
loc_x_2 = 0
loc_x_3 = 0
loc_x_4 = 0
list_1_remove = []
list_2_remove = []
list_3_remove = []
list_4_remove = []
image_ax1 = visual.ImageStim(
    win=win,
    name='image_ax1', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.2, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
image_ax2 = visual.ImageStim(
    win=win,
    name='image_ax2', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.2, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
image_ax3 = visual.ImageStim(
    win=win,
    name='image_ax3', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.2, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
image_ax4 = visual.ImageStim(
    win=win,
    name='image_ax4', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.2, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
image_buttonA = visual.ImageStim(
    win=win,
    name='image_buttonA', 
    image='sin', mask=None,
    ori=0.0, pos=(-0.35, -0.4), size=(0.18, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
image_buttonB = visual.ImageStim(
    win=win,
    name='image_buttonB', 
    image='sin', mask=None,
    ori=0.0, pos=(-0.05, -0.4), size=(0.18, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
image_buttonC = visual.ImageStim(
    win=win,
    name='image_buttonC', 
    image='sin', mask=None,
    ori=0.0, pos=(0.25, -0.4), size=(0.18, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
image_buttonD = visual.ImageStim(
    win=win,
    name='image_buttonD', 
    image='sin', mask=None,
    ori=0.0, pos=(0.55, -0.4), size=(0.18, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
image_personpic = visual.ImageStim(
    win=win,
    name='image_personpic', 
    image='sin', mask=None,
    ori=0.0, pos=(-0.6, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
mouse_A = event.Mouse(win=win)
x, y = [None, None]
mouse_A.mouseClock = core.Clock()
mouse_B = event.Mouse(win=win)
x, y = [None, None]
mouse_B.mouseClock = core.Clock()
mouse_C = event.Mouse(win=win)
x, y = [None, None]
mouse_C.mouseClock = core.Clock()
mouse_D = event.Mouse(win=win)
x, y = [None, None]
mouse_D.mouseClock = core.Clock()
text_personname = visual.TextStim(win=win, name='text_personname',
    text='',
    font='Open Sans',
    pos=(-0.6, -0.1), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-14.0);
image_ph2axisnow1 = visual.ImageStim(
    win=win,
    name='image_ph2axisnow1', 
    image='img/img_button/4axis_now.jpg', mask=None,
    ori=0.0, pos=(-0.338, -0.31), size=(0.09, 0.055),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-15.0)
image_ph2axisnow2 = visual.ImageStim(
    win=win,
    name='image_ph2axisnow2', 
    image='img/img_button/4axis_now.jpg', mask=None,
    ori=0.0, pos=(-0.038, -0.31), size=(0.09, 0.055),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-16.0)
image_ph2axisnow3 = visual.ImageStim(
    win=win,
    name='image_ph2axisnow3', 
    image='img/img_button/4axis_now.jpg', mask=None,
    ori=0.0, pos=(0.262, -0.31), size=(0.09, 0.055),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-17.0)
image_ph2axisnow4 = visual.ImageStim(
    win=win,
    name='image_ph2axisnow4', 
    image='img/img_button/4axis_now.jpg', mask=None,
    ori=0.0, pos=(0.562, -0.31), size=(0.09, 0.055),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-18.0)

# Initialize components for Routine "phase3intro"
phase3introClock = core.Clock()
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='img/img_instruction/ph3intro.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.2, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "phase3_practicechoice"
phase3_practicechoiceClock = core.Clock()
imagepracticeAbutton = visual.ImageStim(
    win=win,
    name='imagepracticeAbutton', 
    image='img/img_button/1button.jpg', mask=None,
    ori=0.0, pos=(-0.2, -0.4), size=(0.18, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
imagepracticeBbutton = visual.ImageStim(
    win=win,
    name='imagepracticeBbutton', 
    image='img/img_button/2button.jpg', mask=None,
    ori=0.0, pos=(0.2, -0.4), size=(0.18, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
mouse_5 = event.Mouse(win=win)
x, y = [None, None]
mouse_5.mouseClock = core.Clock()
time_show=0
image_practiceaxis1 = visual.ImageStim(
    win=win,
    name='image_practiceaxis1', 
    image='img/img_axis/ax27.png', mask=None,
    ori=0.0, pos=(-0.2, 0), size=(0.2, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
image_practiceaxis2 = visual.ImageStim(
    win=win,
    name='image_practiceaxis2', 
    image='img/img_axis/ax36.png', mask=None,
    ori=0.0, pos=(0.2, 0), size=(0.2, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
image_11 = visual.ImageStim(
    win=win,
    name='image_11', 
    image='img/img_instruction/ph3_practiceinstr.png', mask=None,
    ori=0.0, pos=(0, 0.3), size=(1, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)

# Initialize components for Routine "phase3_practicecountdown"
phase3_practicecountdownClock = core.Clock()
text_word = ''
text_8 = visual.TextStim(win=win, name='text_8',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "phase3_practicepic"
phase3_practicepicClock = core.Clock()
image_10 = visual.ImageStim(
    win=win,
    name='image_10', 
    image='img/img_horriblethreat/horriblethreatpractice.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "phase3_formalinstr"
phase3_formalinstrClock = core.Clock()
key_resp_7 = keyboard.Keyboard()
image_9 = visual.ImageStim(
    win=win,
    name='image_9', 
    image='img/img_instruction/ph3_formalinstr.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# Initialize components for Routine "fixation2"
fixation2Clock = core.Clock()
text_fixation2 = visual.TextStim(win=win, name='text_fixation2',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "phase3"
phase3Clock = core.Clock()
count_num=0
image_ph3Q = visual.ImageStim(
    win=win,
    name='image_ph3Q', 
    image='img/img_instruction/ph3.png', mask=None,
    ori=0.0, pos=(0, 0.2), size=(1, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
image_1axis = visual.ImageStim(
    win=win,
    name='image_1axis', 
    image='sin', mask=None,
    ori=0.0, pos=(-0.2, 0), size=(0.2, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
image_2axis = visual.ImageStim(
    win=win,
    name='image_2axis', 
    image='sin', mask=None,
    ori=0.0, pos=(0.2, 0), size=(0.2, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
image_leftbutton = visual.ImageStim(
    win=win,
    name='image_leftbutton', 
    image='img/img_button/1button.jpg', mask=None,
    ori=0.0, pos=(-0.2, -0.4), size=(0.18, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
image_rightbutton = visual.ImageStim(
    win=win,
    name='image_rightbutton', 
    image='img/img_button/2button.jpg', mask=None,
    ori=0.0, pos=(0.2, -0.4), size=(0.18, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
image_ph3axisnow2 = visual.ImageStim(
    win=win,
    name='image_ph3axisnow2', 
    image='img/img_button/5axis_now.jpg', mask=None,
    ori=0.0, pos=(0.2, -0.31), size=(0.1, 0.06),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
image_ph3axisnow1 = visual.ImageStim(
    win=win,
    name='image_ph3axisnow1', 
    image='img/img_button/5axis_now.jpg', mask=None,
    ori=0.0, pos=(-0.2, -0.31), size=(0.1, 0.06),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)

# Initialize components for Routine "phase4intro"
phase4introClock = core.Clock()
image_4 = visual.ImageStim(
    win=win,
    name='image_4', 
    image='img/img_instruction/ph4intro.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.2, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "countdownsec"
countdownsecClock = core.Clock()
countdown_time= 6
text_11 = visual.TextStim(win=win, name='text_11',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "ph4threat_image"
ph4threat_imageClock = core.Clock()
image_5 = visual.ImageStim(
    win=win,
    name='image_5', 
    image='img/img_horriblethreat/horriblethreatfinal.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "stop"
stopClock = core.Clock()
text_stop = visual.TextStim(win=win, name='text_stop',
    text='thanks',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "intro"-------
continueRoutine = True
# update component parameters for each repeat
input_name.reset()
# setup some python lists for storing info about the mouse_3
mouse_3.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
introComponents = [introduction, input_name, image_myself, image_nextbutton, mouse_3]
for thisComponent in introComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "intro"-------
while continueRoutine:
    # get current time
    t = introClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *introduction* updates
    if introduction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        introduction.frameNStart = frameN  # exact frame index
        introduction.tStart = t  # local t and not account for scr refresh
        introduction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(introduction, 'tStartRefresh')  # time at next scr refresh
        introduction.setAutoDraw(True)
    
    # *input_name* updates
    if input_name.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        input_name.frameNStart = frameN  # exact frame index
        input_name.tStart = t  # local t and not account for scr refresh
        input_name.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(input_name, 'tStartRefresh')  # time at next scr refresh
        input_name.setAutoDraw(True)
    
    # *image_myself* updates
    if image_myself.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_myself.frameNStart = frameN  # exact frame index
        image_myself.tStart = t  # local t and not account for scr refresh
        image_myself.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_myself, 'tStartRefresh')  # time at next scr refresh
        image_myself.setAutoDraw(True)
    
    # *image_nextbutton* updates
    if image_nextbutton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_nextbutton.frameNStart = frameN  # exact frame index
        image_nextbutton.tStart = t  # local t and not account for scr refresh
        image_nextbutton.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_nextbutton, 'tStartRefresh')  # time at next scr refresh
        image_nextbutton.setAutoDraw(True)
    # *mouse_3* updates
    if mouse_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_3.frameNStart = frameN  # exact frame index
        mouse_3.tStart = t  # local t and not account for scr refresh
        mouse_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_3, 'tStartRefresh')  # time at next scr refresh
        mouse_3.status = STARTED
        mouse_3.mouseClock.reset()
        prevButtonState = mouse_3.getPressed()  # if button is down already this ISN'T a new click
    if mouse_3.status == STARTED:  # only update if started and not finished!
        buttons = mouse_3.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(image_nextbutton)
                    clickableList = image_nextbutton
                except:
                    clickableList = [image_nextbutton]
                for obj in clickableList:
                    if obj.contains(mouse_3):
                        gotValidClick = True
                        mouse_3.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "intro"-------
for thisComponent in introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('introduction.started', introduction.tStartRefresh)
thisExp.addData('introduction.stopped', introduction.tStopRefresh)
thisExp.addData('input_name.text',input_name.text)
thisExp.addData('input_name.started', input_name.tStartRefresh)
thisExp.addData('input_name.stopped', input_name.tStopRefresh)
thisExp.addData('image_myself.started', image_myself.tStartRefresh)
thisExp.addData('image_myself.stopped', image_myself.tStopRefresh)
thisExp.addData('image_nextbutton.started', image_nextbutton.tStartRefresh)
thisExp.addData('image_nextbutton.stopped', image_nextbutton.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = mouse_3.getPos()
buttons = mouse_3.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    try:
        iter(image_nextbutton)
        clickableList = image_nextbutton
    except:
        clickableList = [image_nextbutton]
    for obj in clickableList:
        if obj.contains(mouse_3):
            gotValidClick = True
            mouse_3.clicked_name.append(obj.name)
thisExp.addData('mouse_3.x', x)
thisExp.addData('mouse_3.y', y)
thisExp.addData('mouse_3.leftButton', buttons[0])
thisExp.addData('mouse_3.midButton', buttons[1])
thisExp.addData('mouse_3.rightButton', buttons[2])
if len(mouse_3.clicked_name):
    thisExp.addData('mouse_3.clicked_name', mouse_3.clicked_name[0])
thisExp.addData('mouse_3.started', mouse_3.tStart)
thisExp.addData('mouse_3.stopped', mouse_3.tStop)
thisExp.nextEntry()
# the Routine "intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('cond/waiting_period.xlsx'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "waiting_phase"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    text_1.setText(a)
    text_2.setText(b)
    text_3.setText(c)
    text_4.setText(d)
    # keep track of which components have finished
    waiting_phaseComponents = [text, text_1, text_2, text_3, text_4, text_5]
    for thisComponent in waiting_phaseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    waiting_phaseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "waiting_phase"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = waiting_phaseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=waiting_phaseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
        # *text_1* updates
        if text_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_1.frameNStart = frameN  # exact frame index
            text_1.tStart = t  # local t and not account for scr refresh
            text_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_1, 'tStartRefresh')  # time at next scr refresh
            text_1.setAutoDraw(True)
        if text_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_1.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_1.tStop = t  # not accounting for scr refresh
                text_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_1, 'tStopRefresh')  # time at next scr refresh
                text_1.setAutoDraw(False)
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                text_2.setAutoDraw(False)
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
                text_3.setAutoDraw(False)
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_4.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                text_4.setAutoDraw(False)
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        if text_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_5.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                text_5.tStop = t  # not accounting for scr refresh
                text_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_5, 'tStopRefresh')  # time at next scr refresh
                text_5.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in waiting_phaseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "waiting_phase"-------
    for thisComponent in waiting_phaseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('text.started', text.tStartRefresh)
    trials_2.addData('text.stopped', text.tStopRefresh)
    trials_2.addData('text_1.started', text_1.tStartRefresh)
    trials_2.addData('text_1.stopped', text_1.tStopRefresh)
    trials_2.addData('text_2.started', text_2.tStartRefresh)
    trials_2.addData('text_2.stopped', text_2.tStopRefresh)
    trials_2.addData('text_3.started', text_3.tStartRefresh)
    trials_2.addData('text_3.stopped', text_3.tStopRefresh)
    trials_2.addData('text_4.started', text_4.tStartRefresh)
    trials_2.addData('text_4.stopped', text_4.tStopRefresh)
    trials_2.addData('text_5.started', text_5.tStartRefresh)
    trials_2.addData('text_5.stopped', text_5.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_2'


# ------Prepare to start Routine "phase1intro_2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
phase1intro_2Components = [image_phase1intro, key_resp]
for thisComponent in phase1intro_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
phase1intro_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "phase1intro_2"-------
while continueRoutine:
    # get current time
    t = phase1intro_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=phase1intro_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_phase1intro* updates
    if image_phase1intro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_phase1intro.frameNStart = frameN  # exact frame index
        image_phase1intro.tStart = t  # local t and not account for scr refresh
        image_phase1intro.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_phase1intro, 'tStartRefresh')  # time at next scr refresh
        image_phase1intro.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in phase1intro_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "phase1intro_2"-------
for thisComponent in phase1intro_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_phase1intro.started', image_phase1intro.tStartRefresh)
thisExp.addData('image_phase1intro.stopped', image_phase1intro.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "phase1intro_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_horribleimg = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('cond/horriblepicture.xlsx'),
    seed=None, name='trials_horribleimg')
thisExp.addLoop(trials_horribleimg)  # add the loop to the experiment
thisTrials_horribleimg = trials_horribleimg.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_horribleimg.rgb)
if thisTrials_horribleimg != None:
    for paramName in thisTrials_horribleimg:
        exec('{} = thisTrials_horribleimg[paramName]'.format(paramName))

for thisTrials_horribleimg in trials_horribleimg:
    currentLoop = trials_horribleimg
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_horribleimg.rgb)
    if thisTrials_horribleimg != None:
        for paramName in thisTrials_horribleimg:
            exec('{} = thisTrials_horribleimg[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "fixation"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixationComponents = [text_fixation]
    for thisComponent in fixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fixation"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_fixation* updates
        if text_fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_fixation.frameNStart = frameN  # exact frame index
            text_fixation.tStart = t  # local t and not account for scr refresh
            text_fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_fixation, 'tStartRefresh')  # time at next scr refresh
            text_fixation.setAutoDraw(True)
        if text_fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_fixation.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                text_fixation.tStop = t  # not accounting for scr refresh
                text_fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_fixation, 'tStopRefresh')  # time at next scr refresh
                text_fixation.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixation"-------
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_horribleimg.addData('text_fixation.started', text_fixation.tStartRefresh)
    trials_horribleimg.addData('text_fixation.stopped', text_fixation.tStopRefresh)
    
    # ------Prepare to start Routine "phase1"-------
    continueRoutine = True
    # update component parameters for each repeat
    image_horrible.setImage(horriblepic)
    # setup some python lists for storing info about the mouse_2
    mouse_2.clicked_name = []
    gotValidClick = False  # until a click is received
    slider_2.reset()
    # keep track of which components have finished
    phase1Components = [image_horrible, image_evl1, image_3button, mouse_2, slider_2, text_6, text_7]
    for thisComponent in phase1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    phase1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "phase1"-------
    while continueRoutine:
        # get current time
        t = phase1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=phase1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_horrible* updates
        if image_horrible.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_horrible.frameNStart = frameN  # exact frame index
            image_horrible.tStart = t  # local t and not account for scr refresh
            image_horrible.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_horrible, 'tStartRefresh')  # time at next scr refresh
            image_horrible.setAutoDraw(True)
        if image_horrible.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_horrible.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                image_horrible.tStop = t  # not accounting for scr refresh
                image_horrible.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_horrible, 'tStopRefresh')  # time at next scr refresh
                image_horrible.setAutoDraw(False)
        
        # *image_evl1* updates
        if image_evl1.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
            # keep track of start time/frame for later
            image_evl1.frameNStart = frameN  # exact frame index
            image_evl1.tStart = t  # local t and not account for scr refresh
            image_evl1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_evl1, 'tStartRefresh')  # time at next scr refresh
            image_evl1.setAutoDraw(True)
        
        # *image_3button* updates
        if image_3button.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
            # keep track of start time/frame for later
            image_3button.frameNStart = frameN  # exact frame index
            image_3button.tStart = t  # local t and not account for scr refresh
            image_3button.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_3button, 'tStartRefresh')  # time at next scr refresh
            image_3button.setAutoDraw(True)
        # *mouse_2* updates
        if mouse_2.status == NOT_STARTED and t >= 5-frameTolerance:
            # keep track of start time/frame for later
            mouse_2.frameNStart = frameN  # exact frame index
            mouse_2.tStart = t  # local t and not account for scr refresh
            mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
            mouse_2.status = STARTED
            mouse_2.mouseClock.reset()
            prevButtonState = mouse_2.getPressed()  # if button is down already this ISN'T a new click
        if mouse_2.status == STARTED:  # only update if started and not finished!
            buttons = mouse_2.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(image_3button)
                        clickableList = image_3button
                    except:
                        clickableList = [image_3button]
                    for obj in clickableList:
                        if obj.contains(mouse_2):
                            gotValidClick = True
                            mouse_2.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # *slider_2* updates
        if slider_2.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
            # keep track of start time/frame for later
            slider_2.frameNStart = frameN  # exact frame index
            slider_2.tStart = t  # local t and not account for scr refresh
            slider_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_2, 'tStartRefresh')  # time at next scr refresh
            slider_2.setAutoDraw(True)
        
        # *text_6* updates
        if text_6.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
            # keep track of start time/frame for later
            text_6.frameNStart = frameN  # exact frame index
            text_6.tStart = t  # local t and not account for scr refresh
            text_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
            text_6.setAutoDraw(True)
        
        # *text_7* updates
        if text_7.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
            # keep track of start time/frame for later
            text_7.frameNStart = frameN  # exact frame index
            text_7.tStart = t  # local t and not account for scr refresh
            text_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
            text_7.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in phase1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "phase1"-------
    for thisComponent in phase1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_horribleimg.addData('image_horrible.started', image_horrible.tStartRefresh)
    trials_horribleimg.addData('image_horrible.stopped', image_horrible.tStopRefresh)
    trials_horribleimg.addData('image_evl1.started', image_evl1.tStartRefresh)
    trials_horribleimg.addData('image_evl1.stopped', image_evl1.tStopRefresh)
    trials_horribleimg.addData('image_3button.started', image_3button.tStartRefresh)
    trials_horribleimg.addData('image_3button.stopped', image_3button.tStopRefresh)
    # store data for trials_horribleimg (TrialHandler)
    x, y = mouse_2.getPos()
    buttons = mouse_2.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        try:
            iter(image_3button)
            clickableList = image_3button
        except:
            clickableList = [image_3button]
        for obj in clickableList:
            if obj.contains(mouse_2):
                gotValidClick = True
                mouse_2.clicked_name.append(obj.name)
    trials_horribleimg.addData('mouse_2.x', x)
    trials_horribleimg.addData('mouse_2.y', y)
    trials_horribleimg.addData('mouse_2.leftButton', buttons[0])
    trials_horribleimg.addData('mouse_2.midButton', buttons[1])
    trials_horribleimg.addData('mouse_2.rightButton', buttons[2])
    if len(mouse_2.clicked_name):
        trials_horribleimg.addData('mouse_2.clicked_name', mouse_2.clicked_name[0])
    trials_horribleimg.addData('mouse_2.started', mouse_2.tStart)
    trials_horribleimg.addData('mouse_2.stopped', mouse_2.tStop)
    trials_horribleimg.addData('slider_2.response', slider_2.getRating())
    trials_horribleimg.addData('slider_2.rt', slider_2.getRT())
    trials_horribleimg.addData('slider_2.started', slider_2.tStartRefresh)
    trials_horribleimg.addData('slider_2.stopped', slider_2.tStopRefresh)
    trials_horribleimg.addData('text_6.started', text_6.tStartRefresh)
    trials_horribleimg.addData('text_6.stopped', text_6.tStopRefresh)
    trials_horribleimg.addData('text_7.started', text_7.tStartRefresh)
    trials_horribleimg.addData('text_7.stopped', text_7.tStopRefresh)
    # the Routine "phase1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_horribleimg'


# ------Prepare to start Routine "phase2intro"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
phase2introComponents = [image_phase2intro, key_resp_5, image_12]
for thisComponent in phase2introComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
phase2introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "phase2intro"-------
while continueRoutine:
    # get current time
    t = phase2introClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=phase2introClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_phase2intro* updates
    if image_phase2intro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_phase2intro.frameNStart = frameN  # exact frame index
        image_phase2intro.tStart = t  # local t and not account for scr refresh
        image_phase2intro.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_phase2intro, 'tStartRefresh')  # time at next scr refresh
        image_phase2intro.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *image_12* updates
    if image_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_12.frameNStart = frameN  # exact frame index
        image_12.tStart = t  # local t and not account for scr refresh
        image_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_12, 'tStartRefresh')  # time at next scr refresh
        image_12.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in phase2introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "phase2intro"-------
for thisComponent in phase2introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_phase2intro.started', image_phase2intro.tStartRefresh)
thisExp.addData('image_phase2intro.stopped', image_phase2intro.tStopRefresh)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.addData('key_resp_5.started', key_resp_5.tStartRefresh)
thisExp.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('image_12.started', image_12.tStartRefresh)
thisExp.addData('image_12.stopped', image_12.tStopRefresh)
# the Routine "phase2intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('cond/ph2_cond.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Phase2"-------
    continueRoutine = True
    # update component parameters for each repeat
    list_loc_1 = [-0.35,-0.05,0.25,0.55]
    shuffle(list_1)
    shuffle(list_2)
    shuffle(list_3)
    shuffle(list_4)
    shuffle(list_loc_1)
    loc_x_1 = list_loc_1[0]
    loc_x_2 = list_loc_1[1]
    loc_x_3 = list_loc_1[2]
    loc_x_4 = list_loc_1[3]
    
    if list_1[0] == 1:
        pic_1 = ph2_pic60_1
        list_1_remove.append(1)
    
    if list_1[0] == 2:
        pic_1 = ph2_pic60_2
        list_1_remove.append(2)
    if list_1[0] == 3:
        pic_1 = ph2_pic60_3
        list_1_remove.append(3)
    
    if list_1[0] == 4:
        pic_1 = ph2_pic60_4
        list_1_remove.append(4)
        
    if list_1[0] == 5:
        pic_1 = ph2_pic60_5
        list_1_remove.append(5)
        
    if list_1[0] == 6:
        pic_1 = ph2_pic60_6
        list_1_remove.append(6)
        
    if list_1[0] == 7:
        pic_1 = ph2_pic60_7
        list_1_remove.append(7)
    
    if list_1[0] == 8:
        pic_1 = ph2_pic60_8
        list_1_remove.append(8)
    if list_1[0] == 9:
        pic_1 = ph2_pic60_9
        list_1_remove.append(9)
    
    temp_1 = list_1[0]
    temp_2 = list_2[0]
    temp_3 = list_3[0]
    temp_4 = list_4[0]
    if list_2[0] == 1:
        pic_2 = ph2_pic70_1
        list_2_remove.append(1)
    
    if list_2[0] == 2:
        pic_2 = ph2_pic70_2
        list_2_remove.append(2)
    
    if list_2[0] == 3:
        pic_2 = ph2_pic70_3
        list_2_remove.append(3)
    
    if list_2[0] == 4:
        pic_2 = ph2_pic70_4
        list_2_remove.append(4)
        
    if list_2[0] == 5:
        pic_2 = ph2_pic70_5
        list_2_remove.append(5)
        
    if list_2[0] == 6:
        pic_2= ph2_pic70_6
        list_2_remove.append(6)
        
    if list_2[0] == 7:
        pic_2 = ph2_pic70_7
        list_2_remove.append(7)
    
    if list_2[0] == 8:
        pic_2 = ph2_pic70_8
        list_2_remove.append(8)
    
    if list_2[0] == 9:
        pic_2 = ph2_pic70_9
        list_2_remove.append(9)
    
    if list_3[0] == 1:
        pic_3 = ph2_pic80_1
        list_3_remove.append(1)
    
    if list_3[0] == 2:
        pic_3 = ph2_pic80_2
        list_3_remove.append(2)
    
    if list_3[0] == 3:
        pic_3 = ph2_pic80_3
        list_3_remove.append(3)
    
    if list_3[0] == 4:
        pic_3 = ph2_pic80_4
        list_3_remove.append(4)
        
    if list_3[0] == 5:
        pic_3 = ph2_pic80_5
        list_3_remove.append(5)
        
    if list_3[0] == 6:
        pic_3 = ph2_pic80_6
        list_3_remove.append(6)
        
    if list_3[0] == 7:
        pic_3 = ph2_pic80_7
        list_3_remove.append(7)
    
    if list_3[0] == 8:
        pic_3 = ph2_pic80_8
        list_3_remove.append(8)
    
    if list_3[0] == 9:
        pic_3 = ph2_pic80_9
        list_3_remove.append(9)
    
    if list_4[0] == 1:
        pic_4 = ph2_pic90_1
        list_4_remove.append(1)
    
    if list_4[0] == 2:
        pic_4 = ph2_pic90_2
        list_4_remove.append(2)
    
    if list_4[0] == 3:
        pic_4 = ph2_pic90_3
        list_4_remove.append(3)
    
    if list_4[0] == 4:
        pic_4 = ph2_pic90_4
        list_4_remove.append(4)
        
    if list_4[0] == 5:
        pic_4 = ph2_pic90_5
        list_4_remove.append(5)
        
    if list_4[0] == 6:
        pic_4 = ph2_pic90_6
        list_4_remove.append(6)
        
    if list_4[0] == 7:
        pic_4 = ph2_pic90_7
        list_4_remove.append(7)
    
    if list_4[0] == 8:
        pic_4 = ph2_pic90_8
        list_4_remove.append(8)
    
    if list_4[0] == 9:
        pic_4 = ph2_pic90_9
        list_4_remove.append(9)
    image_ax1.setPos((loc_x_1,0))
    image_ax1.setImage(pic_1)
    image_ax2.setPos((loc_x_2,0))
    image_ax2.setImage(pic_2)
    image_ax3.setPos((loc_x_3,0))
    image_ax3.setImage(pic_3)
    image_ax4.setPos((loc_x_4,0))
    image_ax4.setImage(pic_4)
    image_buttonA.setImage('img/img_button_ph2/button_A.jpg')
    image_buttonB.setImage('img/img_button_ph2/button_B.jpg')
    image_buttonC.setImage('img/img_button_ph2/button_C.jpg')
    image_buttonD.setImage('img/img_button_ph2/button_D.jpg')
    image_personpic.setImage(person_img)
    # setup some python lists for storing info about the mouse_A
    mouse_A.clicked_name = []
    gotValidClick = False  # until a click is received
    # setup some python lists for storing info about the mouse_B
    mouse_B.clicked_name = []
    gotValidClick = False  # until a click is received
    # setup some python lists for storing info about the mouse_C
    mouse_C.clicked_name = []
    gotValidClick = False  # until a click is received
    # setup some python lists for storing info about the mouse_D
    mouse_D.clicked_name = []
    gotValidClick = False  # until a click is received
    text_personname.setText(person_name)
    # keep track of which components have finished
    Phase2Components = [image_ax1, image_ax2, image_ax3, image_ax4, image_buttonA, image_buttonB, image_buttonC, image_buttonD, image_personpic, mouse_A, mouse_B, mouse_C, mouse_D, text_personname, image_ph2axisnow1, image_ph2axisnow2, image_ph2axisnow3, image_ph2axisnow4]
    for thisComponent in Phase2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Phase2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Phase2"-------
    while continueRoutine:
        # get current time
        t = Phase2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Phase2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_ax1* updates
        if image_ax1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_ax1.frameNStart = frameN  # exact frame index
            image_ax1.tStart = t  # local t and not account for scr refresh
            image_ax1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_ax1, 'tStartRefresh')  # time at next scr refresh
            image_ax1.setAutoDraw(True)
        
        # *image_ax2* updates
        if image_ax2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_ax2.frameNStart = frameN  # exact frame index
            image_ax2.tStart = t  # local t and not account for scr refresh
            image_ax2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_ax2, 'tStartRefresh')  # time at next scr refresh
            image_ax2.setAutoDraw(True)
        
        # *image_ax3* updates
        if image_ax3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_ax3.frameNStart = frameN  # exact frame index
            image_ax3.tStart = t  # local t and not account for scr refresh
            image_ax3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_ax3, 'tStartRefresh')  # time at next scr refresh
            image_ax3.setAutoDraw(True)
        
        # *image_ax4* updates
        if image_ax4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_ax4.frameNStart = frameN  # exact frame index
            image_ax4.tStart = t  # local t and not account for scr refresh
            image_ax4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_ax4, 'tStartRefresh')  # time at next scr refresh
            image_ax4.setAutoDraw(True)
        
        # *image_buttonA* updates
        if image_buttonA.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_buttonA.frameNStart = frameN  # exact frame index
            image_buttonA.tStart = t  # local t and not account for scr refresh
            image_buttonA.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_buttonA, 'tStartRefresh')  # time at next scr refresh
            image_buttonA.setAutoDraw(True)
        
        # *image_buttonB* updates
        if image_buttonB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_buttonB.frameNStart = frameN  # exact frame index
            image_buttonB.tStart = t  # local t and not account for scr refresh
            image_buttonB.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_buttonB, 'tStartRefresh')  # time at next scr refresh
            image_buttonB.setAutoDraw(True)
        
        # *image_buttonC* updates
        if image_buttonC.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_buttonC.frameNStart = frameN  # exact frame index
            image_buttonC.tStart = t  # local t and not account for scr refresh
            image_buttonC.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_buttonC, 'tStartRefresh')  # time at next scr refresh
            image_buttonC.setAutoDraw(True)
        
        # *image_buttonD* updates
        if image_buttonD.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_buttonD.frameNStart = frameN  # exact frame index
            image_buttonD.tStart = t  # local t and not account for scr refresh
            image_buttonD.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_buttonD, 'tStartRefresh')  # time at next scr refresh
            image_buttonD.setAutoDraw(True)
        
        # *image_personpic* updates
        if image_personpic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_personpic.frameNStart = frameN  # exact frame index
            image_personpic.tStart = t  # local t and not account for scr refresh
            image_personpic.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_personpic, 'tStartRefresh')  # time at next scr refresh
            image_personpic.setAutoDraw(True)
        # *mouse_A* updates
        if mouse_A.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_A.frameNStart = frameN  # exact frame index
            mouse_A.tStart = t  # local t and not account for scr refresh
            mouse_A.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_A, 'tStartRefresh')  # time at next scr refresh
            mouse_A.status = STARTED
            mouse_A.mouseClock.reset()
            prevButtonState = mouse_A.getPressed()  # if button is down already this ISN'T a new click
        if mouse_A.status == STARTED:  # only update if started and not finished!
            buttons = mouse_A.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter([image_buttonA,image_buttonB,image_buttonC,image_buttonD])
                        clickableList = [image_buttonA,image_buttonB,image_buttonC,image_buttonD]
                    except:
                        clickableList = [[image_buttonA,image_buttonB,image_buttonC,image_buttonD]]
                    for obj in clickableList:
                        if obj.contains(mouse_A):
                            gotValidClick = True
                            mouse_A.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        # *mouse_B* updates
        if mouse_B.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_B.frameNStart = frameN  # exact frame index
            mouse_B.tStart = t  # local t and not account for scr refresh
            mouse_B.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_B, 'tStartRefresh')  # time at next scr refresh
            mouse_B.status = STARTED
            mouse_B.mouseClock.reset()
            prevButtonState = mouse_B.getPressed()  # if button is down already this ISN'T a new click
        if mouse_B.status == STARTED:  # only update if started and not finished!
            buttons = mouse_B.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter([image_buttonA,image_buttonB,image_buttonC,image_buttonD])
                        clickableList = [image_buttonA,image_buttonB,image_buttonC,image_buttonD]
                    except:
                        clickableList = [[image_buttonA,image_buttonB,image_buttonC,image_buttonD]]
                    for obj in clickableList:
                        if obj.contains(mouse_B):
                            gotValidClick = True
                            mouse_B.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        # *mouse_C* updates
        if mouse_C.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_C.frameNStart = frameN  # exact frame index
            mouse_C.tStart = t  # local t and not account for scr refresh
            mouse_C.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_C, 'tStartRefresh')  # time at next scr refresh
            mouse_C.status = STARTED
            mouse_C.mouseClock.reset()
            prevButtonState = mouse_C.getPressed()  # if button is down already this ISN'T a new click
        if mouse_C.status == STARTED:  # only update if started and not finished!
            buttons = mouse_C.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter([image_buttonA,image_buttonB,image_buttonC,image_buttonD])
                        clickableList = [image_buttonA,image_buttonB,image_buttonC,image_buttonD]
                    except:
                        clickableList = [[image_buttonA,image_buttonB,image_buttonC,image_buttonD]]
                    for obj in clickableList:
                        if obj.contains(mouse_C):
                            gotValidClick = True
                            mouse_C.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        # *mouse_D* updates
        if mouse_D.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_D.frameNStart = frameN  # exact frame index
            mouse_D.tStart = t  # local t and not account for scr refresh
            mouse_D.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_D, 'tStartRefresh')  # time at next scr refresh
            mouse_D.status = STARTED
            mouse_D.mouseClock.reset()
            prevButtonState = mouse_D.getPressed()  # if button is down already this ISN'T a new click
        if mouse_D.status == STARTED:  # only update if started and not finished!
            buttons = mouse_D.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter([image_buttonA,image_buttonB,image_buttonC,image_buttonD])
                        clickableList = [image_buttonA,image_buttonB,image_buttonC,image_buttonD]
                    except:
                        clickableList = [[image_buttonA,image_buttonB,image_buttonC,image_buttonD]]
                    for obj in clickableList:
                        if obj.contains(mouse_D):
                            gotValidClick = True
                            mouse_D.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # *text_personname* updates
        if text_personname.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_personname.frameNStart = frameN  # exact frame index
            text_personname.tStart = t  # local t and not account for scr refresh
            text_personname.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_personname, 'tStartRefresh')  # time at next scr refresh
            text_personname.setAutoDraw(True)
        
        # *image_ph2axisnow1* updates
        if image_ph2axisnow1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_ph2axisnow1.frameNStart = frameN  # exact frame index
            image_ph2axisnow1.tStart = t  # local t and not account for scr refresh
            image_ph2axisnow1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_ph2axisnow1, 'tStartRefresh')  # time at next scr refresh
            image_ph2axisnow1.setAutoDraw(True)
        
        # *image_ph2axisnow2* updates
        if image_ph2axisnow2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_ph2axisnow2.frameNStart = frameN  # exact frame index
            image_ph2axisnow2.tStart = t  # local t and not account for scr refresh
            image_ph2axisnow2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_ph2axisnow2, 'tStartRefresh')  # time at next scr refresh
            image_ph2axisnow2.setAutoDraw(True)
        
        # *image_ph2axisnow3* updates
        if image_ph2axisnow3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_ph2axisnow3.frameNStart = frameN  # exact frame index
            image_ph2axisnow3.tStart = t  # local t and not account for scr refresh
            image_ph2axisnow3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_ph2axisnow3, 'tStartRefresh')  # time at next scr refresh
            image_ph2axisnow3.setAutoDraw(True)
        
        # *image_ph2axisnow4* updates
        if image_ph2axisnow4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_ph2axisnow4.frameNStart = frameN  # exact frame index
            image_ph2axisnow4.tStart = t  # local t and not account for scr refresh
            image_ph2axisnow4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_ph2axisnow4, 'tStartRefresh')  # time at next scr refresh
            image_ph2axisnow4.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Phase2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Phase2"-------
    for thisComponent in Phase2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    list_temp1=[]
    list_temp2=[]
    list_temp3=[]
    list_temp4=[]
    if len(list_1)>1:
        for i in list_1:
            if i not in list_1_remove:
                list_temp1.append(i)
        list_1 = list_temp1
    if len(list_2)>1:
        for i in list_2:
            if i not in list_2_remove:
                list_temp2.append(i)
        list_2 = list_temp2
    if len(list_3)>1:
        for i in list_3:
            if i not in list_3_remove:
                list_temp3.append(i)
        list_3 = list_temp3
    if len(list_4)>1:
        for i in list_4:
            if i not in list_4_remove:
                list_temp4.append(i)
        list_4 = list_temp4
    
    thisExp.addData("loc_x_1",loc_x_1)
    thisExp.addData("loc_x_2",loc_x_2)
    thisExp.addData("loc_x_3",loc_x_3)
    thisExp.addData("loc_x_4",loc_x_4)
    thisExp.addData("list_1_remove",list_1_remove)
    thisExp.addData("list_2_remove",list_2_remove)
    thisExp.addData("list_3_remove",list_3_remove)
    thisExp.addData("list_4_remove",list_4_remove) 
    
    print(list_1_remove)
    print(list_2_remove)
    print(list_3_remove)
    print(list_4_remove)
    print(loc_x_1)
    print(loc_x_2)
    print(loc_x_3)
    print(loc_x_4)
    
    
    trials.addData('image_ax1.started', image_ax1.tStartRefresh)
    trials.addData('image_ax1.stopped', image_ax1.tStopRefresh)
    trials.addData('image_ax2.started', image_ax2.tStartRefresh)
    trials.addData('image_ax2.stopped', image_ax2.tStopRefresh)
    trials.addData('image_ax3.started', image_ax3.tStartRefresh)
    trials.addData('image_ax3.stopped', image_ax3.tStopRefresh)
    trials.addData('image_ax4.started', image_ax4.tStartRefresh)
    trials.addData('image_ax4.stopped', image_ax4.tStopRefresh)
    trials.addData('image_buttonA.started', image_buttonA.tStartRefresh)
    trials.addData('image_buttonA.stopped', image_buttonA.tStopRefresh)
    trials.addData('image_buttonB.started', image_buttonB.tStartRefresh)
    trials.addData('image_buttonB.stopped', image_buttonB.tStopRefresh)
    trials.addData('image_buttonC.started', image_buttonC.tStartRefresh)
    trials.addData('image_buttonC.stopped', image_buttonC.tStopRefresh)
    trials.addData('image_buttonD.started', image_buttonD.tStartRefresh)
    trials.addData('image_buttonD.stopped', image_buttonD.tStopRefresh)
    trials.addData('image_personpic.started', image_personpic.tStartRefresh)
    trials.addData('image_personpic.stopped', image_personpic.tStopRefresh)
    # store data for trials (TrialHandler)
    x, y = mouse_A.getPos()
    buttons = mouse_A.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        try:
            iter([image_buttonA,image_buttonB,image_buttonC,image_buttonD])
            clickableList = [image_buttonA,image_buttonB,image_buttonC,image_buttonD]
        except:
            clickableList = [[image_buttonA,image_buttonB,image_buttonC,image_buttonD]]
        for obj in clickableList:
            if obj.contains(mouse_A):
                gotValidClick = True
                mouse_A.clicked_name.append(obj.name)
    trials.addData('mouse_A.x', x)
    trials.addData('mouse_A.y', y)
    trials.addData('mouse_A.leftButton', buttons[0])
    trials.addData('mouse_A.midButton', buttons[1])
    trials.addData('mouse_A.rightButton', buttons[2])
    if len(mouse_A.clicked_name):
        trials.addData('mouse_A.clicked_name', mouse_A.clicked_name[0])
    trials.addData('mouse_A.started', mouse_A.tStart)
    trials.addData('mouse_A.stopped', mouse_A.tStop)
    # store data for trials (TrialHandler)
    x, y = mouse_B.getPos()
    buttons = mouse_B.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        try:
            iter([image_buttonA,image_buttonB,image_buttonC,image_buttonD])
            clickableList = [image_buttonA,image_buttonB,image_buttonC,image_buttonD]
        except:
            clickableList = [[image_buttonA,image_buttonB,image_buttonC,image_buttonD]]
        for obj in clickableList:
            if obj.contains(mouse_B):
                gotValidClick = True
                mouse_B.clicked_name.append(obj.name)
    trials.addData('mouse_B.x', x)
    trials.addData('mouse_B.y', y)
    trials.addData('mouse_B.leftButton', buttons[0])
    trials.addData('mouse_B.midButton', buttons[1])
    trials.addData('mouse_B.rightButton', buttons[2])
    if len(mouse_B.clicked_name):
        trials.addData('mouse_B.clicked_name', mouse_B.clicked_name[0])
    trials.addData('mouse_B.started', mouse_B.tStart)
    trials.addData('mouse_B.stopped', mouse_B.tStop)
    # store data for trials (TrialHandler)
    x, y = mouse_C.getPos()
    buttons = mouse_C.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        try:
            iter([image_buttonA,image_buttonB,image_buttonC,image_buttonD])
            clickableList = [image_buttonA,image_buttonB,image_buttonC,image_buttonD]
        except:
            clickableList = [[image_buttonA,image_buttonB,image_buttonC,image_buttonD]]
        for obj in clickableList:
            if obj.contains(mouse_C):
                gotValidClick = True
                mouse_C.clicked_name.append(obj.name)
    trials.addData('mouse_C.x', x)
    trials.addData('mouse_C.y', y)
    trials.addData('mouse_C.leftButton', buttons[0])
    trials.addData('mouse_C.midButton', buttons[1])
    trials.addData('mouse_C.rightButton', buttons[2])
    if len(mouse_C.clicked_name):
        trials.addData('mouse_C.clicked_name', mouse_C.clicked_name[0])
    trials.addData('mouse_C.started', mouse_C.tStart)
    trials.addData('mouse_C.stopped', mouse_C.tStop)
    # store data for trials (TrialHandler)
    x, y = mouse_D.getPos()
    buttons = mouse_D.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        try:
            iter([image_buttonA,image_buttonB,image_buttonC,image_buttonD])
            clickableList = [image_buttonA,image_buttonB,image_buttonC,image_buttonD]
        except:
            clickableList = [[image_buttonA,image_buttonB,image_buttonC,image_buttonD]]
        for obj in clickableList:
            if obj.contains(mouse_D):
                gotValidClick = True
                mouse_D.clicked_name.append(obj.name)
    trials.addData('mouse_D.x', x)
    trials.addData('mouse_D.y', y)
    trials.addData('mouse_D.leftButton', buttons[0])
    trials.addData('mouse_D.midButton', buttons[1])
    trials.addData('mouse_D.rightButton', buttons[2])
    if len(mouse_D.clicked_name):
        trials.addData('mouse_D.clicked_name', mouse_D.clicked_name[0])
    trials.addData('mouse_D.started', mouse_D.tStart)
    trials.addData('mouse_D.stopped', mouse_D.tStop)
    trials.addData('text_personname.started', text_personname.tStartRefresh)
    trials.addData('text_personname.stopped', text_personname.tStopRefresh)
    trials.addData('image_ph2axisnow1.started', image_ph2axisnow1.tStartRefresh)
    trials.addData('image_ph2axisnow1.stopped', image_ph2axisnow1.tStopRefresh)
    trials.addData('image_ph2axisnow2.started', image_ph2axisnow2.tStartRefresh)
    trials.addData('image_ph2axisnow2.stopped', image_ph2axisnow2.tStopRefresh)
    trials.addData('image_ph2axisnow3.started', image_ph2axisnow3.tStartRefresh)
    trials.addData('image_ph2axisnow3.stopped', image_ph2axisnow3.tStopRefresh)
    trials.addData('image_ph2axisnow4.started', image_ph2axisnow4.tStartRefresh)
    trials.addData('image_ph2axisnow4.stopped', image_ph2axisnow4.tStopRefresh)
    # the Routine "Phase2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# ------Prepare to start Routine "phase3intro"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
phase3introComponents = [image_2, key_resp_4]
for thisComponent in phase3introComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
phase3introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "phase3intro"-------
while continueRoutine:
    # get current time
    t = phase3introClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=phase3introClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_2* updates
    if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_2.frameNStart = frameN  # exact frame index
        image_2.tStart = t  # local t and not account for scr refresh
        image_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
        image_2.setAutoDraw(True)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in phase3introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "phase3intro"-------
for thisComponent in phase3introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_2.started', image_2.tStartRefresh)
thisExp.addData('image_2.stopped', image_2.tStopRefresh)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys = None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.addData('key_resp_4.started', key_resp_4.tStartRefresh)
thisExp.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
thisExp.nextEntry()
# the Routine "phase3intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "phase3_practicechoice"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_5
mouse_5.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
phase3_practicechoiceComponents = [imagepracticeAbutton, imagepracticeBbutton, mouse_5, image_practiceaxis1, image_practiceaxis2, image_11]
for thisComponent in phase3_practicechoiceComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
phase3_practicechoiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "phase3_practicechoice"-------
while continueRoutine:
    # get current time
    t = phase3_practicechoiceClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=phase3_practicechoiceClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *imagepracticeAbutton* updates
    if imagepracticeAbutton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        imagepracticeAbutton.frameNStart = frameN  # exact frame index
        imagepracticeAbutton.tStart = t  # local t and not account for scr refresh
        imagepracticeAbutton.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(imagepracticeAbutton, 'tStartRefresh')  # time at next scr refresh
        imagepracticeAbutton.setAutoDraw(True)
    
    # *imagepracticeBbutton* updates
    if imagepracticeBbutton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        imagepracticeBbutton.frameNStart = frameN  # exact frame index
        imagepracticeBbutton.tStart = t  # local t and not account for scr refresh
        imagepracticeBbutton.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(imagepracticeBbutton, 'tStartRefresh')  # time at next scr refresh
        imagepracticeBbutton.setAutoDraw(True)
    # *mouse_5* updates
    if mouse_5.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_5.frameNStart = frameN  # exact frame index
        mouse_5.tStart = t  # local t and not account for scr refresh
        mouse_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_5, 'tStartRefresh')  # time at next scr refresh
        mouse_5.status = STARTED
        mouse_5.mouseClock.reset()
        prevButtonState = mouse_5.getPressed()  # if button is down already this ISN'T a new click
    if mouse_5.status == STARTED:  # only update if started and not finished!
        buttons = mouse_5.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter([imagepracticeAbutton,imagepracticeBbutton])
                    clickableList = [imagepracticeAbutton,imagepracticeBbutton]
                except:
                    clickableList = [[imagepracticeAbutton,imagepracticeBbutton]]
                for obj in clickableList:
                    if obj.contains(mouse_5):
                        gotValidClick = True
                        mouse_5.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # *image_practiceaxis1* updates
    if image_practiceaxis1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_practiceaxis1.frameNStart = frameN  # exact frame index
        image_practiceaxis1.tStart = t  # local t and not account for scr refresh
        image_practiceaxis1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_practiceaxis1, 'tStartRefresh')  # time at next scr refresh
        image_practiceaxis1.setAutoDraw(True)
    
    # *image_practiceaxis2* updates
    if image_practiceaxis2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_practiceaxis2.frameNStart = frameN  # exact frame index
        image_practiceaxis2.tStart = t  # local t and not account for scr refresh
        image_practiceaxis2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_practiceaxis2, 'tStartRefresh')  # time at next scr refresh
        image_practiceaxis2.setAutoDraw(True)
    
    # *image_11* updates
    if image_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_11.frameNStart = frameN  # exact frame index
        image_11.tStart = t  # local t and not account for scr refresh
        image_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_11, 'tStartRefresh')  # time at next scr refresh
        image_11.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in phase3_practicechoiceComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "phase3_practicechoice"-------
for thisComponent in phase3_practicechoiceComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('imagepracticeAbutton.started', imagepracticeAbutton.tStartRefresh)
thisExp.addData('imagepracticeAbutton.stopped', imagepracticeAbutton.tStopRefresh)
thisExp.addData('imagepracticeBbutton.started', imagepracticeBbutton.tStartRefresh)
thisExp.addData('imagepracticeBbutton.stopped', imagepracticeBbutton.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = mouse_5.getPos()
buttons = mouse_5.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    try:
        iter([imagepracticeAbutton,imagepracticeBbutton])
        clickableList = [imagepracticeAbutton,imagepracticeBbutton]
    except:
        clickableList = [[imagepracticeAbutton,imagepracticeBbutton]]
    for obj in clickableList:
        if obj.contains(mouse_5):
            gotValidClick = True
            mouse_5.clicked_name.append(obj.name)
thisExp.addData('mouse_5.x', x)
thisExp.addData('mouse_5.y', y)
thisExp.addData('mouse_5.leftButton', buttons[0])
thisExp.addData('mouse_5.midButton', buttons[1])
thisExp.addData('mouse_5.rightButton', buttons[2])
if len(mouse_5.clicked_name):
    thisExp.addData('mouse_5.clicked_name', mouse_5.clicked_name[0])
thisExp.addData('mouse_5.started', mouse_5.tStart)
thisExp.addData('mouse_5.stopped', mouse_5.tStop)
thisExp.nextEntry()
if mouse.isPressedIn(imagepracticeAbutton):
    time_show=7
else:
    time_show=9
thisExp.addData('image_practiceaxis1.started', image_practiceaxis1.tStartRefresh)
thisExp.addData('image_practiceaxis1.stopped', image_practiceaxis1.tStopRefresh)
thisExp.addData('image_practiceaxis2.started', image_practiceaxis2.tStartRefresh)
thisExp.addData('image_practiceaxis2.stopped', image_practiceaxis2.tStopRefresh)
thisExp.addData('image_11.started', image_11.tStartRefresh)
thisExp.addData('image_11.stopped', image_11.tStopRefresh)
# the Routine "phase3_practicechoice" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=time_show, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "phase3_practicecountdown"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    text_word = str(time_show) + 's'
    text_8.setText(text_word)
    # keep track of which components have finished
    phase3_practicecountdownComponents = [text_8]
    for thisComponent in phase3_practicecountdownComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    phase3_practicecountdownClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "phase3_practicecountdown"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = phase3_practicecountdownClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=phase3_practicecountdownClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_8* updates
        if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_8.frameNStart = frameN  # exact frame index
            text_8.tStart = t  # local t and not account for scr refresh
            text_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
            text_8.setAutoDraw(True)
        if text_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_8.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_8.tStop = t  # not accounting for scr refresh
                text_8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_8, 'tStopRefresh')  # time at next scr refresh
                text_8.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in phase3_practicecountdownComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "phase3_practicecountdown"-------
    for thisComponent in phase3_practicecountdownComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    time_show -= 1
    trials_3.addData('text_8.started', text_8.tStartRefresh)
    trials_3.addData('text_8.stopped', text_8.tStopRefresh)
    thisExp.nextEntry()
    
# completed time_show repeats of 'trials_3'


# ------Prepare to start Routine "phase3_practicepic"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
phase3_practicepicComponents = [image_10]
for thisComponent in phase3_practicepicComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
phase3_practicepicClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "phase3_practicepic"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = phase3_practicepicClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=phase3_practicepicClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_10* updates
    if image_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_10.frameNStart = frameN  # exact frame index
        image_10.tStart = t  # local t and not account for scr refresh
        image_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_10, 'tStartRefresh')  # time at next scr refresh
        image_10.setAutoDraw(True)
    if image_10.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_10.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            image_10.tStop = t  # not accounting for scr refresh
            image_10.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_10, 'tStopRefresh')  # time at next scr refresh
            image_10.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in phase3_practicepicComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "phase3_practicepic"-------
for thisComponent in phase3_practicepicComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_10.started', image_10.tStartRefresh)
thisExp.addData('image_10.stopped', image_10.tStopRefresh)

# ------Prepare to start Routine "phase3_formalinstr"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_7.keys = []
key_resp_7.rt = []
_key_resp_7_allKeys = []
# keep track of which components have finished
phase3_formalinstrComponents = [key_resp_7, image_9]
for thisComponent in phase3_formalinstrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
phase3_formalinstrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "phase3_formalinstr"-------
while continueRoutine:
    # get current time
    t = phase3_formalinstrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=phase3_formalinstrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_7* updates
    waitOnFlip = False
    if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.tStart = t  # local t and not account for scr refresh
        key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_7.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_7.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_7_allKeys.extend(theseKeys)
        if len(_key_resp_7_allKeys):
            key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
            key_resp_7.rt = _key_resp_7_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *image_9* updates
    if image_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_9.frameNStart = frameN  # exact frame index
        image_9.tStart = t  # local t and not account for scr refresh
        image_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_9, 'tStartRefresh')  # time at next scr refresh
        image_9.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in phase3_formalinstrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "phase3_formalinstr"-------
for thisComponent in phase3_formalinstrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_7.keys in ['', [], None]:  # No response was made
    key_resp_7.keys = None
thisExp.addData('key_resp_7.keys',key_resp_7.keys)
if key_resp_7.keys != None:  # we had a response
    thisExp.addData('key_resp_7.rt', key_resp_7.rt)
thisExp.addData('key_resp_7.started', key_resp_7.tStartRefresh)
thisExp.addData('key_resp_7.stopped', key_resp_7.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('image_9.started', image_9.tStartRefresh)
thisExp.addData('image_9.stopped', image_9.tStopRefresh)
# the Routine "phase3_formalinstr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_ph3_2 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('cond/tabletotal.xlsx'),
    seed=None, name='trials_ph3_2')
thisExp.addLoop(trials_ph3_2)  # add the loop to the experiment
thisTrials_ph3_2 = trials_ph3_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_ph3_2.rgb)
if thisTrials_ph3_2 != None:
    for paramName in thisTrials_ph3_2:
        exec('{} = thisTrials_ph3_2[paramName]'.format(paramName))

for thisTrials_ph3_2 in trials_ph3_2:
    currentLoop = trials_ph3_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_ph3_2.rgb)
    if thisTrials_ph3_2 != None:
        for paramName in thisTrials_ph3_2:
            exec('{} = thisTrials_ph3_2[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials_ph3_1 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(excel),
        seed=None, name='trials_ph3_1')
    thisExp.addLoop(trials_ph3_1)  # add the loop to the experiment
    thisTrials_ph3_1 = trials_ph3_1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_ph3_1.rgb)
    if thisTrials_ph3_1 != None:
        for paramName in thisTrials_ph3_1:
            exec('{} = thisTrials_ph3_1[paramName]'.format(paramName))
    
    for thisTrials_ph3_1 in trials_ph3_1:
        currentLoop = trials_ph3_1
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_ph3_1.rgb)
        if thisTrials_ph3_1 != None:
            for paramName in thisTrials_ph3_1:
                exec('{} = thisTrials_ph3_1[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "fixation2"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        # keep track of which components have finished
        fixation2Components = [text_fixation2]
        for thisComponent in fixation2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        fixation2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "fixation2"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = fixation2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=fixation2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_fixation2* updates
            if text_fixation2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_fixation2.frameNStart = frameN  # exact frame index
                text_fixation2.tStart = t  # local t and not account for scr refresh
                text_fixation2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_fixation2, 'tStartRefresh')  # time at next scr refresh
                text_fixation2.setAutoDraw(True)
            if text_fixation2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_fixation2.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_fixation2.tStop = t  # not accounting for scr refresh
                    text_fixation2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_fixation2, 'tStopRefresh')  # time at next scr refresh
                    text_fixation2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixation2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "fixation2"-------
        for thisComponent in fixation2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_ph3_1.addData('text_fixation2.started', text_fixation2.tStartRefresh)
        trials_ph3_1.addData('text_fixation2.stopped', text_fixation2.tStopRefresh)
        
        # ------Prepare to start Routine "phase3"-------
        continueRoutine = True
        # update component parameters for each repeat
        count_num += 1
        list_1 = [1,2]
        shuffle(list_1)
        if list_1[0] ==2 :
           img_2_loc = pic_left
           img_1_loc = pic_right
        else:
           img_2_loc = pic_right
           img_1_loc = pic_left
        image_1axis.setImage(img_1_loc)
        image_2axis.setImage(img_2_loc)
        # setup some python lists for storing info about the mouse
        mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        phase3Components = [image_ph3Q, image_1axis, image_2axis, image_leftbutton, image_rightbutton, mouse, image_ph3axisnow2, image_ph3axisnow1]
        for thisComponent in phase3Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        phase3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "phase3"-------
        while continueRoutine:
            # get current time
            t = phase3Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=phase3Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_ph3Q* updates
            if image_ph3Q.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_ph3Q.frameNStart = frameN  # exact frame index
                image_ph3Q.tStart = t  # local t and not account for scr refresh
                image_ph3Q.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_ph3Q, 'tStartRefresh')  # time at next scr refresh
                image_ph3Q.setAutoDraw(True)
            
            # *image_1axis* updates
            if image_1axis.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_1axis.frameNStart = frameN  # exact frame index
                image_1axis.tStart = t  # local t and not account for scr refresh
                image_1axis.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_1axis, 'tStartRefresh')  # time at next scr refresh
                image_1axis.setAutoDraw(True)
            
            # *image_2axis* updates
            if image_2axis.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_2axis.frameNStart = frameN  # exact frame index
                image_2axis.tStart = t  # local t and not account for scr refresh
                image_2axis.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_2axis, 'tStartRefresh')  # time at next scr refresh
                image_2axis.setAutoDraw(True)
            
            # *image_leftbutton* updates
            if image_leftbutton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_leftbutton.frameNStart = frameN  # exact frame index
                image_leftbutton.tStart = t  # local t and not account for scr refresh
                image_leftbutton.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_leftbutton, 'tStartRefresh')  # time at next scr refresh
                image_leftbutton.setAutoDraw(True)
            
            # *image_rightbutton* updates
            if image_rightbutton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_rightbutton.frameNStart = frameN  # exact frame index
                image_rightbutton.tStart = t  # local t and not account for scr refresh
                image_rightbutton.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_rightbutton, 'tStartRefresh')  # time at next scr refresh
                image_rightbutton.setAutoDraw(True)
            # *mouse* updates
            if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse.frameNStart = frameN  # exact frame index
                mouse.tStart = t  # local t and not account for scr refresh
                mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
                mouse.status = STARTED
                mouse.mouseClock.reset()
                prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
            if mouse.status == STARTED:  # only update if started and not finished!
                buttons = mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter([image_leftbutton,image_rightbutton])
                            clickableList = [image_leftbutton,image_rightbutton]
                        except:
                            clickableList = [[image_leftbutton,image_rightbutton]]
                        for obj in clickableList:
                            if obj.contains(mouse):
                                gotValidClick = True
                                mouse.clicked_name.append(obj.name)
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # *image_ph3axisnow2* updates
            if image_ph3axisnow2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_ph3axisnow2.frameNStart = frameN  # exact frame index
                image_ph3axisnow2.tStart = t  # local t and not account for scr refresh
                image_ph3axisnow2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_ph3axisnow2, 'tStartRefresh')  # time at next scr refresh
                image_ph3axisnow2.setAutoDraw(True)
            
            # *image_ph3axisnow1* updates
            if image_ph3axisnow1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_ph3axisnow1.frameNStart = frameN  # exact frame index
                image_ph3axisnow1.tStart = t  # local t and not account for scr refresh
                image_ph3axisnow1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_ph3axisnow1, 'tStartRefresh')  # time at next scr refresh
                image_ph3axisnow1.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in phase3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "phase3"-------
        for thisComponent in phase3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        if count_num >=1 :
            trials_ph3_1.finished = True
            
        trials_ph3_1.addData('image_ph3Q.started', image_ph3Q.tStartRefresh)
        trials_ph3_1.addData('image_ph3Q.stopped', image_ph3Q.tStopRefresh)
        trials_ph3_1.addData('image_1axis.started', image_1axis.tStartRefresh)
        trials_ph3_1.addData('image_1axis.stopped', image_1axis.tStopRefresh)
        trials_ph3_1.addData('image_2axis.started', image_2axis.tStartRefresh)
        trials_ph3_1.addData('image_2axis.stopped', image_2axis.tStopRefresh)
        trials_ph3_1.addData('image_leftbutton.started', image_leftbutton.tStartRefresh)
        trials_ph3_1.addData('image_leftbutton.stopped', image_leftbutton.tStopRefresh)
        trials_ph3_1.addData('image_rightbutton.started', image_rightbutton.tStartRefresh)
        trials_ph3_1.addData('image_rightbutton.stopped', image_rightbutton.tStopRefresh)
        # store data for trials_ph3_1 (TrialHandler)
        x, y = mouse.getPos()
        buttons = mouse.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            try:
                iter([image_leftbutton,image_rightbutton])
                clickableList = [image_leftbutton,image_rightbutton]
            except:
                clickableList = [[image_leftbutton,image_rightbutton]]
            for obj in clickableList:
                if obj.contains(mouse):
                    gotValidClick = True
                    mouse.clicked_name.append(obj.name)
        trials_ph3_1.addData('mouse.x', x)
        trials_ph3_1.addData('mouse.y', y)
        trials_ph3_1.addData('mouse.leftButton', buttons[0])
        trials_ph3_1.addData('mouse.midButton', buttons[1])
        trials_ph3_1.addData('mouse.rightButton', buttons[2])
        if len(mouse.clicked_name):
            trials_ph3_1.addData('mouse.clicked_name', mouse.clicked_name[0])
        trials_ph3_1.addData('mouse.started', mouse.tStart)
        trials_ph3_1.addData('mouse.stopped', mouse.tStop)
        trials_ph3_1.addData('image_ph3axisnow2.started', image_ph3axisnow2.tStartRefresh)
        trials_ph3_1.addData('image_ph3axisnow2.stopped', image_ph3axisnow2.tStopRefresh)
        trials_ph3_1.addData('image_ph3axisnow1.started', image_ph3axisnow1.tStartRefresh)
        trials_ph3_1.addData('image_ph3axisnow1.stopped', image_ph3axisnow1.tStopRefresh)
        # the Routine "phase3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_ph3_1'
    
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_ph3_2'


# ------Prepare to start Routine "phase4intro"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
# keep track of which components have finished
phase4introComponents = [image_4, key_resp_6]
for thisComponent in phase4introComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
phase4introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "phase4intro"-------
while continueRoutine:
    # get current time
    t = phase4introClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=phase4introClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_4* updates
    if image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_4.frameNStart = frameN  # exact frame index
        image_4.tStart = t  # local t and not account for scr refresh
        image_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
        image_4.setAutoDraw(True)
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
            key_resp_6.rt = _key_resp_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in phase4introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "phase4intro"-------
for thisComponent in phase4introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_4.started', image_4.tStartRefresh)
thisExp.addData('image_4.stopped', image_4.tStopRefresh)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.addData('key_resp_6.started', key_resp_6.tStartRefresh)
thisExp.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
thisExp.nextEntry()
# the Routine "phase4intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_4 = data.TrialHandler(nReps=countdown_time, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_4')
thisExp.addLoop(trials_4)  # add the loop to the experiment
thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
if thisTrial_4 != None:
    for paramName in thisTrial_4:
        exec('{} = thisTrial_4[paramName]'.format(paramName))

for thisTrial_4 in trials_4:
    currentLoop = trials_4
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
    if thisTrial_4 != None:
        for paramName in thisTrial_4:
            exec('{} = thisTrial_4[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "countdownsec"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    text_word = str(countdown_time) + 's'
    text_11.setText(countdown_time)
    # keep track of which components have finished
    countdownsecComponents = [text_11]
    for thisComponent in countdownsecComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    countdownsecClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "countdownsec"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = countdownsecClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=countdownsecClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_11* updates
        if text_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_11.frameNStart = frameN  # exact frame index
            text_11.tStart = t  # local t and not account for scr refresh
            text_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
            text_11.setAutoDraw(True)
        if text_11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_11.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_11.tStop = t  # not accounting for scr refresh
                text_11.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_11, 'tStopRefresh')  # time at next scr refresh
                text_11.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in countdownsecComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "countdownsec"-------
    for thisComponent in countdownsecComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    countdown_time -= 1
    trials_4.addData('text_11.started', text_11.tStartRefresh)
    trials_4.addData('text_11.stopped', text_11.tStopRefresh)
    thisExp.nextEntry()
    
# completed countdown_time repeats of 'trials_4'


# ------Prepare to start Routine "ph4threat_image"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
ph4threat_imageComponents = [image_5]
for thisComponent in ph4threat_imageComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ph4threat_imageClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ph4threat_image"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ph4threat_imageClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ph4threat_imageClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_5* updates
    if image_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_5.frameNStart = frameN  # exact frame index
        image_5.tStart = t  # local t and not account for scr refresh
        image_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_5, 'tStartRefresh')  # time at next scr refresh
        image_5.setAutoDraw(True)
    if image_5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_5.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            image_5.tStop = t  # not accounting for scr refresh
            image_5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_5, 'tStopRefresh')  # time at next scr refresh
            image_5.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ph4threat_imageComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ph4threat_image"-------
for thisComponent in ph4threat_imageComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_5.started', image_5.tStartRefresh)
thisExp.addData('image_5.stopped', image_5.tStopRefresh)

# ------Prepare to start Routine "stop"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
stopComponents = [text_stop]
for thisComponent in stopComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
stopClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "stop"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = stopClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=stopClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_stop* updates
    if text_stop.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_stop.frameNStart = frameN  # exact frame index
        text_stop.tStart = t  # local t and not account for scr refresh
        text_stop.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_stop, 'tStartRefresh')  # time at next scr refresh
        text_stop.setAutoDraw(True)
    if text_stop.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_stop.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            text_stop.tStop = t  # not accounting for scr refresh
            text_stop.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_stop, 'tStopRefresh')  # time at next scr refresh
            text_stop.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in stopComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "stop"-------
for thisComponent in stopComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_stop.started', text_stop.tStartRefresh)
thisExp.addData('text_stop.stopped', text_stop.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
