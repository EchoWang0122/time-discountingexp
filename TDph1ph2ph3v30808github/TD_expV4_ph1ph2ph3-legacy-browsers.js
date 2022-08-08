﻿/*************************** 
 * Td_Expv4_Ph1Ph2Ph3 Test *
 ***************************/


// store info about the experiment session:
let expName = 'TD_expV4_ph1ph2ph3';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: false,
  color: new util.Color('white'),
  units: 'height',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(introRoutineBegin());
flowScheduler.add(introRoutineEachFrame());
flowScheduler.add(introRoutineEnd());
flowScheduler.add(phase1intro_2RoutineBegin());
flowScheduler.add(phase1intro_2RoutineEachFrame());
flowScheduler.add(phase1intro_2RoutineEnd());
const trials_horribleimgLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_horribleimgLoopBegin(trials_horribleimgLoopScheduler));
flowScheduler.add(trials_horribleimgLoopScheduler);
flowScheduler.add(trials_horribleimgLoopEnd);
flowScheduler.add(phase2introRoutineBegin());
flowScheduler.add(phase2introRoutineEachFrame());
flowScheduler.add(phase2introRoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(phase3introRoutineBegin());
flowScheduler.add(phase3introRoutineEachFrame());
flowScheduler.add(phase3introRoutineEnd());
const trials_ph3_2LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_ph3_2LoopBegin(trials_ph3_2LoopScheduler));
flowScheduler.add(trials_ph3_2LoopScheduler);
flowScheduler.add(trials_ph3_2LoopEnd);
flowScheduler.add(phase4introRoutineBegin());
flowScheduler.add(phase4introRoutineEachFrame());
flowScheduler.add(phase4introRoutineEnd());
const trials_countdownLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_countdownLoopBegin(trials_countdownLoopScheduler));
flowScheduler.add(trials_countdownLoopScheduler);
flowScheduler.add(trials_countdownLoopEnd);
flowScheduler.add(ph4threat_imageRoutineBegin());
flowScheduler.add(ph4threat_imageRoutineEachFrame());
flowScheduler.add(ph4threat_imageRoutineEnd());
flowScheduler.add(stopRoutineBegin());
flowScheduler.add(stopRoutineEachFrame());
flowScheduler.add(stopRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'img/img_axis/ax31.png', 'path': 'img/img_axis/ax31.png'},
    {'name': 'img/img_person/py3.png', 'path': 'img/img_person/py3.png'},
    {'name': 'cond/ph3_timepoint/t24.xlsx', 'path': 'cond/ph3_timepoint/t24.xlsx'},
    {'name': 'cond/ph3_timepoint/t57.xlsx', 'path': 'cond/ph3_timepoint/t57.xlsx'},
    {'name': 'img/img_axis/ax12.png', 'path': 'img/img_axis/ax12.png'},
    {'name': 'img/img_horriblethreat/hopic_evl1.png', 'path': 'img/img_horriblethreat/hopic_evl1.png'},
    {'name': 'img/img_axis/ax3.png', 'path': 'img/img_axis/ax3.png'},
    {'name': 'cond/ph3_timepoint/t13.xlsx', 'path': 'cond/ph3_timepoint/t13.xlsx'},
    {'name': 'cond/ph3_timepoint/t1011.xlsx', 'path': 'cond/ph3_timepoint/t1011.xlsx'},
    {'name': 'img/img_axis/ax25.png', 'path': 'img/img_axis/ax25.png'},
    {'name': 'cond/ph3_timepoint/t48.xlsx', 'path': 'cond/ph3_timepoint/t48.xlsx'},
    {'name': 'img/img_person/myself.png', 'path': 'img/img_person/myself.png'},
    {'name': 'img/img_axis/ax2.png', 'path': 'img/img_axis/ax2.png'},
    {'name': 'img/img_instruction/ph2intro.png', 'path': 'img/img_instruction/ph2intro.png'},
    {'name': 'cond/tabletotal.xlsx', 'path': 'cond/tabletotal.xlsx'},
    {'name': 'img/img_person/py4.png', 'path': 'img/img_person/py4.png'},
    {'name': 'cond/ph3_timepoint/t510.xlsx', 'path': 'cond/ph3_timepoint/t510.xlsx'},
    {'name': 'img/img_axis/ax36.png', 'path': 'img/img_axis/ax36.png'},
    {'name': 'cond/ph3_timepoint/t27.xlsx', 'path': 'cond/ph3_timepoint/t27.xlsx'},
    {'name': 'cond/ph3_timepoint/t35.xlsx', 'path': 'cond/ph3_timepoint/t35.xlsx'},
    {'name': 'cond/ph3_timepoint/t68.xlsx', 'path': 'cond/ph3_timepoint/t68.xlsx'},
    {'name': 'cond/ph3_timepoint/t511.xlsx', 'path': 'cond/ph3_timepoint/t511.xlsx'},
    {'name': 'cond/ph3_timepoint/t69.xlsx', 'path': 'cond/ph3_timepoint/t69.xlsx'},
    {'name': 'cond/ph3_timepoint/t58.xlsx', 'path': 'cond/ph3_timepoint/t58.xlsx'},
    {'name': 'img/img_axis/ax8.png', 'path': 'img/img_axis/ax8.png'},
    {'name': 'img/img_axis/ax28.png', 'path': 'img/img_axis/ax28.png'},
    {'name': 'cond/ph3_timepoint/t812.xlsx', 'path': 'cond/ph3_timepoint/t812.xlsx'},
    {'name': 'img/img_person/py8.png', 'path': 'img/img_person/py8.png'},
    {'name': 'img/img_person/py9.png', 'path': 'img/img_person/py9.png'},
    {'name': 'cond/countdownsecond.xlsx', 'path': 'cond/countdownsecond.xlsx'},
    {'name': 'img/img_axis/ax13.png', 'path': 'img/img_axis/ax13.png'},
    {'name': 'cond/ph3_timepoint/t410.xlsx', 'path': 'cond/ph3_timepoint/t410.xlsx'},
    {'name': 'img/img_horriblethreat/horriblethreatfinal.png', 'path': 'img/img_horriblethreat/horriblethreatfinal.png'},
    {'name': 'cond/ph3_timepoint/t18.xlsx', 'path': 'cond/ph3_timepoint/t18.xlsx'},
    {'name': 'cond/ph3_timepoint/t36.xlsx', 'path': 'cond/ph3_timepoint/t36.xlsx'},
    {'name': 'img/img_axis/ax6.png', 'path': 'img/img_axis/ax6.png'},
    {'name': 'img/img_axis/ax22.png', 'path': 'img/img_axis/ax22.png'},
    {'name': 'img/img_person/py6.png', 'path': 'img/img_person/py6.png'},
    {'name': 'img/img_button/5axis_now.jpg', 'path': 'img/img_button/5axis_now.jpg'},
    {'name': 'img/img_person/py1.png', 'path': 'img/img_person/py1.png'},
    {'name': 'img/img_axis/ax10.png', 'path': 'img/img_axis/ax10.png'},
    {'name': 'cond/ph3_timepoint/t412.xlsx', 'path': 'cond/ph3_timepoint/t412.xlsx'},
    {'name': 'cond/ph3_timepoint/t712.xlsx', 'path': 'cond/ph3_timepoint/t712.xlsx'},
    {'name': 'cond/ph3_timepoint/t29.xlsx', 'path': 'cond/ph3_timepoint/t29.xlsx'},
    {'name': 'img/img_axis/ax19.png', 'path': 'img/img_axis/ax19.png'},
    {'name': 'img/img_button_ph2/button_C.jpg', 'path': 'img/img_button_ph2/button_C.jpg'},
    {'name': 'cond/ph3_timepoint/t110.xlsx', 'path': 'cond/ph3_timepoint/t110.xlsx'},
    {'name': 'cond/ph3_timepoint/t312.xlsx', 'path': 'cond/ph3_timepoint/t312.xlsx'},
    {'name': 'cond/ph3_timepoint/t311.xlsx', 'path': 'cond/ph3_timepoint/t311.xlsx'},
    {'name': 'img/img_axis/ax34.png', 'path': 'img/img_axis/ax34.png'},
    {'name': 'img/img_axis/ax24.png', 'path': 'img/img_axis/ax24.png'},
    {'name': 'img/img_instruction/ph3.png', 'path': 'img/img_instruction/ph3.png'},
    {'name': 'cond/ph3_timepoint/t37.xlsx', 'path': 'cond/ph3_timepoint/t37.xlsx'},
    {'name': 'img/img_axis/ax9.png', 'path': 'img/img_axis/ax9.png'},
    {'name': 'cond/ph3_timepoint/t45.xlsx', 'path': 'cond/ph3_timepoint/t45.xlsx'},
    {'name': 'img/img_horriblethreat/horrible2.png', 'path': 'img/img_horriblethreat/horrible2.png'},
    {'name': 'img/img_horriblethreat/hopic_evl2.png', 'path': 'img/img_horriblethreat/hopic_evl2.png'},
    {'name': 'cond/ph3_timepoint/t67.xlsx', 'path': 'cond/ph3_timepoint/t67.xlsx'},
    {'name': 'cond/ph3_timepoint/t611.xlsx', 'path': 'cond/ph3_timepoint/t611.xlsx'},
    {'name': 'cond/ph3_timepoint/t811.xlsx', 'path': 'cond/ph3_timepoint/t811.xlsx'},
    {'name': 'cond/ph3_timepoint/t1112.xlsx', 'path': 'cond/ph3_timepoint/t1112.xlsx'},
    {'name': 'cond/ph3_timepoint/t25.xlsx', 'path': 'cond/ph3_timepoint/t25.xlsx'},
    {'name': 'img/img_axis/ax17.png', 'path': 'img/img_axis/ax17.png'},
    {'name': 'img/img_button_ph2/button_B.jpg', 'path': 'img/img_button_ph2/button_B.jpg'},
    {'name': 'cond/ph3_timepoint/t38.xlsx', 'path': 'cond/ph3_timepoint/t38.xlsx'},
    {'name': 'cond/ph3_timepoint/t59.xlsx', 'path': 'cond/ph3_timepoint/t59.xlsx'},
    {'name': 'cond/ph3_timepoint/t612.xlsx', 'path': 'cond/ph3_timepoint/t612.xlsx'},
    {'name': 'cond/ph3_timepoint/t810.xlsx', 'path': 'cond/ph3_timepoint/t810.xlsx'},
    {'name': 'cond/ph3_timepoint/t111.xlsx', 'path': 'cond/ph3_timepoint/t111.xlsx'},
    {'name': 'cond/ph3_timepoint/t910.xlsx', 'path': 'cond/ph3_timepoint/t910.xlsx'},
    {'name': 'img/img_axis/ax32.png', 'path': 'img/img_axis/ax32.png'},
    {'name': 'img/img_axis/ax18.png', 'path': 'img/img_axis/ax18.png'},
    {'name': 'img/img_button/2button.jpg', 'path': 'img/img_button/2button.jpg'},
    {'name': 'img/img_axis/ax21.png', 'path': 'img/img_axis/ax21.png'},
    {'name': 'img/img_axis/ax27.png', 'path': 'img/img_axis/ax27.png'},
    {'name': 'cond/ph3_timepoint/t210.xlsx', 'path': 'cond/ph3_timepoint/t210.xlsx'},
    {'name': 'cond/ph3_timepoint/t211.xlsx', 'path': 'cond/ph3_timepoint/t211.xlsx'},
    {'name': 'img/img_axis/ax5.png', 'path': 'img/img_axis/ax5.png'},
    {'name': 'img/img_button/4axis_now.jpg', 'path': 'img/img_button/4axis_now.jpg'},
    {'name': 'img/img_person/py7.png', 'path': 'img/img_person/py7.png'},
    {'name': 'img/img_person/py2.png', 'path': 'img/img_person/py2.png'},
    {'name': 'img/img_button/3button.jpg', 'path': 'img/img_button/3button.jpg'},
    {'name': 'cond/ph2_cond.xlsx', 'path': 'cond/ph2_cond.xlsx'},
    {'name': 'img/img_button_ph2/button_A.jpg', 'path': 'img/img_button_ph2/button_A.jpg'},
    {'name': 'cond/ph3_timepoint/t34.xlsx', 'path': 'cond/ph3_timepoint/t34.xlsx'},
    {'name': 'img/img_instruction/ph3intro.png', 'path': 'img/img_instruction/ph3intro.png'},
    {'name': 'cond/ph3_timepoint/t911.xlsx', 'path': 'cond/ph3_timepoint/t911.xlsx'},
    {'name': 'cond/ph3_timepoint/t711.xlsx', 'path': 'cond/ph3_timepoint/t711.xlsx'},
    {'name': 'cond/horriblepicture.xlsx', 'path': 'cond/horriblepicture.xlsx'},
    {'name': 'img/img_axis/ax26.png', 'path': 'img/img_axis/ax26.png'},
    {'name': 'cond/ph3_timepoint/t46.xlsx', 'path': 'cond/ph3_timepoint/t46.xlsx'},
    {'name': 'cond/ph3_timepoint/t16.xlsx', 'path': 'cond/ph3_timepoint/t16.xlsx'},
    {'name': 'img/img_axis/ax11.png', 'path': 'img/img_axis/ax11.png'},
    {'name': 'cond/ph3_timepoint/t78.xlsx', 'path': 'cond/ph3_timepoint/t78.xlsx'},
    {'name': 'img/img_person/py5.png', 'path': 'img/img_person/py5.png'},
    {'name': 'cond/ph3_timepoint/t19.xlsx', 'path': 'cond/ph3_timepoint/t19.xlsx'},
    {'name': 'cond/ph3_timepoint/t89.xlsx', 'path': 'cond/ph3_timepoint/t89.xlsx'},
    {'name': 'img/img_axis/ax30.png', 'path': 'img/img_axis/ax30.png'},
    {'name': 'cond/ph3_timepoint/t610.xlsx', 'path': 'cond/ph3_timepoint/t610.xlsx'},
    {'name': 'img/img_axis/ax33.png', 'path': 'img/img_axis/ax33.png'},
    {'name': 'cond/ph3_timepoint/t28.xlsx', 'path': 'cond/ph3_timepoint/t28.xlsx'},
    {'name': 'img/img_axis/ax1.png', 'path': 'img/img_axis/ax1.png'},
    {'name': 'img/img_axis/ax35.png', 'path': 'img/img_axis/ax35.png'},
    {'name': 'img/img_button/1button.jpg', 'path': 'img/img_button/1button.jpg'},
    {'name': 'img/img_axis/ax16.png', 'path': 'img/img_axis/ax16.png'},
    {'name': 'cond/ph3_timepoint/t710.xlsx', 'path': 'cond/ph3_timepoint/t710.xlsx'},
    {'name': 'cond/ph3_timepoint/t1012.xlsx', 'path': 'cond/ph3_timepoint/t1012.xlsx'},
    {'name': 'cond/ph3_timepoint/t14.xlsx', 'path': 'cond/ph3_timepoint/t14.xlsx'},
    {'name': 'img/img_axis/ax14.png', 'path': 'img/img_axis/ax14.png'},
    {'name': 'cond/ph3_timepoint/t23.xlsx', 'path': 'cond/ph3_timepoint/t23.xlsx'},
    {'name': 'cond/ph3_timepoint/t26.xlsx', 'path': 'cond/ph3_timepoint/t26.xlsx'},
    {'name': 'cond/ph3_timepoint/t49.xlsx', 'path': 'cond/ph3_timepoint/t49.xlsx'},
    {'name': 'img/img_axis/ax29.png', 'path': 'img/img_axis/ax29.png'},
    {'name': 'cond/ph3_timepoint/t912.xlsx', 'path': 'cond/ph3_timepoint/t912.xlsx'},
    {'name': 'cond/ph3_timepoint/t112.xlsx', 'path': 'cond/ph3_timepoint/t112.xlsx'},
    {'name': 'cond/ph3_timepoint/t47.xlsx', 'path': 'cond/ph3_timepoint/t47.xlsx'},
    {'name': 'img/img_button_ph2/button_D.jpg', 'path': 'img/img_button_ph2/button_D.jpg'},
    {'name': 'cond/ph3_timepoint/t79.xlsx', 'path': 'cond/ph3_timepoint/t79.xlsx'},
    {'name': 'cond/ph3_timepoint/t12.xlsx', 'path': 'cond/ph3_timepoint/t12.xlsx'},
    {'name': 'cond/ph3_timepoint/t411.xlsx', 'path': 'cond/ph3_timepoint/t411.xlsx'},
    {'name': 'cond/ph3_timepoint/t310.xlsx', 'path': 'cond/ph3_timepoint/t310.xlsx'},
    {'name': 'img/img_horriblethreat/horrible1.png', 'path': 'img/img_horriblethreat/horrible1.png'},
    {'name': 'img/img_axis/ax4.png', 'path': 'img/img_axis/ax4.png'},
    {'name': 'cond/ph3_timepoint/t39.xlsx', 'path': 'cond/ph3_timepoint/t39.xlsx'},
    {'name': 'img/img_axis/ax7.png', 'path': 'img/img_axis/ax7.png'},
    {'name': 'cond/ph3_timepoint/t212.xlsx', 'path': 'cond/ph3_timepoint/t212.xlsx'},
    {'name': 'img/img_axis/ax20.png', 'path': 'img/img_axis/ax20.png'},
    {'name': 'cond/ph3_timepoint/t56.xlsx', 'path': 'cond/ph3_timepoint/t56.xlsx'},
    {'name': 'cond/ph3_timepoint/t512.xlsx', 'path': 'cond/ph3_timepoint/t512.xlsx'},
    {'name': 'img/img_instruction/ph1intro.png', 'path': 'img/img_instruction/ph1intro.png'},
    {'name': 'img/img_axis/ax15.png', 'path': 'img/img_axis/ax15.png'},
    {'name': 'img/img_instruction/ph4intro.png', 'path': 'img/img_instruction/ph4intro.png'},
    {'name': 'cond/ph3_timepoint/t17.xlsx', 'path': 'cond/ph3_timepoint/t17.xlsx'},
    {'name': 'cond/ph3_timepoint/t15.xlsx', 'path': 'cond/ph3_timepoint/t15.xlsx'},
    {'name': 'img/img_axis/ax23.png', 'path': 'img/img_axis/ax23.png'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var frameDur;
async function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2021.2.3';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var introClock;
var introduction;
var input_name;
var image_myself;
var image_nextbutton;
var mouse_3;
var phase1intro_2Clock;
var image_phase1intro;
var key_resp;
var fixationClock;
var text_fixation;
var phase1Clock;
var image_horrible;
var slider_evl1;
var image_evl1;
var image_evl2;
var slider_evl2;
var image_3button;
var mouse_2;
var phase2introClock;
var image_phase2intro;
var key_resp_5;
var Phase2Clock;
var list_1;
var list_2;
var list_3;
var list_4;
var pic_1;
var pic_2;
var pic_3;
var pic_4;
var loc_x_1;
var loc_x_2;
var loc_x_3;
var loc_x_4;
var list_1_remove;
var list_2_remove;
var list_3_remove;
var list_4_remove;
var image_ax1;
var image_ax2;
var image_ax3;
var image_ax4;
var image_buttonA;
var image_buttonB;
var image_buttonC;
var image_buttonD;
var image_personpic;
var mouse_A;
var mouse_B;
var mouse_C;
var mouse_D;
var text_personname;
var image_ph2axisnow1;
var image_ph2axisnow2;
var image_ph2axisnow3;
var image_ph2axisnow4;
var phase3introClock;
var image_2;
var key_resp_4;
var fixation2Clock;
var text_fixation2;
var phase3Clock;
var image_ph3Q;
var image_1axis;
var image_2axis;
var image_leftbutton;
var image_rightbutton;
var mouse;
var count_num;
var image_ph3axisnow2;
var image_ph3axisnow1;
var phase4introClock;
var image_4;
var key_resp_6;
var countdownClock;
var text_countdownsecond;
var ph4threat_imageClock;
var image_5;
var stopClock;
var text_stop;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "intro"
  introClock = new util.Clock();
  introduction = new visual.TextStim({
    win: psychoJS.window,
    name: 'introduction',
    text: '欢迎参加实验，本实验目的是探究威胁的时间折扣问题\n\n本实验为您随机生成了一个头像，\n请您填写您的昵称，\n填写好后，请点击“下一页”。',
    font: 'STSong',
    units: undefined, 
    pos: [0, 0.05], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  input_name = new visual.TextBox({
    win: psychoJS.window,
    name: 'input_name',
    text: '',
    font: 'Songti SC',
    pos: [0, (- 0.3)], letterHeight: 0.05,
    size: [null, null],  units: undefined, 
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    editable: true,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  image_myself = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_myself', units : undefined, 
    image : 'img/img_person/myself.png', mask : undefined,
    ori : 0.0, pos : [0, (- 0.15)], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  image_nextbutton = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_nextbutton', units : undefined, 
    image : 'img/img_button/3button.jpg', mask : undefined,
    ori : 0.0, pos : [0.5, (- 0.4)], size : [0.2, 0.1],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  mouse_3 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_3.mouseClock = new util.Clock();
  // Initialize components for Routine "phase1intro_2"
  phase1intro_2Clock = new util.Clock();
  image_phase1intro = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_phase1intro', units : undefined, 
    image : 'img/img_instruction/ph1intro.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.2, 1],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "fixation"
  fixationClock = new util.Clock();
  text_fixation = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_fixation',
    text: '+',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "phase1"
  phase1Clock = new util.Clock();
  image_horrible = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_horrible', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.6, 0.5],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  slider_evl1 = new visual.Slider({
    win: psychoJS.window, name: 'slider_evl1',
    size: [0.6, 0.05], pos: [(- 0.4), (- 0.15)], units: 'height',
    labels: [1, 2, 3, 4, 5, 6, 7], ticks: [1, 2, 3, 4, 5, 6, 7],
    granularity: 1.0, style: ["RATING"],
    color: new util.Color('LightGray'), markerColor: new util.Color('Red'), lineColor: new util.Color('black'), 
    fontFamily: 'Open Sans', bold: true, italic: false, depth: -1, 
    flip: false,
  });
  
  image_evl1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_evl1', units : undefined, 
    image : 'img/img_horriblethreat/hopic_evl1.png', mask : undefined,
    ori : 0.0, pos : [(- 0.35), 0.06], size : [0.65, 0.3],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  image_evl2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_evl2', units : undefined, 
    image : 'img/img_horriblethreat/hopic_evl2.png', mask : undefined,
    ori : 0.0, pos : [0.35, 0.06], size : [0.65, 0.3],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  slider_evl2 = new visual.Slider({
    win: psychoJS.window, name: 'slider_evl2',
    size: [0.6, 0.05], pos: [0.4, (- 0.15)], units: 'height',
    labels: [1, 2, 3, 4, 5, 6, 7], ticks: [1, 2, 3, 4, 5, 6, 7],
    granularity: 1.0, style: ["RATING"],
    color: new util.Color('LightGray'), markerColor: new util.Color('Red'), lineColor: new util.Color('black'), 
    fontFamily: 'Open Sans', bold: true, italic: false, depth: -4, 
    flip: false,
  });
  
  image_3button = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_3button', units : undefined, 
    image : 'img/img_button/3button.jpg', mask : undefined,
    ori : 0.0, pos : [0.5, (- 0.4)], size : [0.2, 0.1],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  mouse_2 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_2.mouseClock = new util.Clock();
  // Initialize components for Routine "phase2intro"
  phase2introClock = new util.Clock();
  image_phase2intro = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_phase2intro', units : undefined, 
    image : 'img/img_instruction/ph2intro.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.2, 1],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  key_resp_5 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Phase2"
  Phase2Clock = new util.Clock();
  list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9];
  list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9];
  list_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9];
  list_4 = [1, 2, 3, 4, 5, 6, 7, 8, 9];
  pic_1 = "";
  pic_2 = "";
  pic_3 = "";
  pic_4 = "";
  loc_x_1 = 0;
  loc_x_2 = 0;
  loc_x_3 = 0;
  loc_x_4 = 0;
  list_1_remove = [];
  list_2_remove = [];
  list_3_remove = [];
  list_4_remove = [];
  
  image_ax1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_ax1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.2, 0.7],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  image_ax2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_ax2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.2, 0.7],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  image_ax3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_ax3', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.2, 0.7],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  image_ax4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_ax4', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.2, 0.7],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  image_buttonA = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_buttonA', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [(- 0.35), (- 0.4)], size : [0.18, 0.1],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  image_buttonB = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_buttonB', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [(- 0.05), (- 0.4)], size : [0.18, 0.1],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -6.0 
  });
  image_buttonC = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_buttonC', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0.25, (- 0.4)], size : [0.18, 0.1],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -7.0 
  });
  image_buttonD = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_buttonD', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0.55, (- 0.4)], size : [0.18, 0.1],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -8.0 
  });
  image_personpic = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_personpic', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [(- 0.6), 0], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -9.0 
  });
  mouse_A = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_A.mouseClock = new util.Clock();
  mouse_B = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_B.mouseClock = new util.Clock();
  mouse_C = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_C.mouseClock = new util.Clock();
  mouse_D = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_D.mouseClock = new util.Clock();
  text_personname = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_personname',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.6), (- 0.1)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -14.0 
  });
  
  image_ph2axisnow1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_ph2axisnow1', units : undefined, 
    image : 'img/img_button/4axis_now.jpg', mask : undefined,
    ori : 0.0, pos : [(- 0.338), (- 0.31)], size : [0.09, 0.055],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -15.0 
  });
  image_ph2axisnow2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_ph2axisnow2', units : undefined, 
    image : 'img/img_button/4axis_now.jpg', mask : undefined,
    ori : 0.0, pos : [(- 0.038), (- 0.31)], size : [0.09, 0.055],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -16.0 
  });
  image_ph2axisnow3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_ph2axisnow3', units : undefined, 
    image : 'img/img_button/4axis_now.jpg', mask : undefined,
    ori : 0.0, pos : [0.262, (- 0.31)], size : [0.09, 0.055],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -17.0 
  });
  image_ph2axisnow4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_ph2axisnow4', units : undefined, 
    image : 'img/img_button/4axis_now.jpg', mask : undefined,
    ori : 0.0, pos : [0.562, (- 0.31)], size : [0.09, 0.055],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -18.0 
  });
  // Initialize components for Routine "phase3intro"
  phase3introClock = new util.Clock();
  image_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_2', units : undefined, 
    image : 'img/img_instruction/ph3intro.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.2, 0.6],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  key_resp_4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "fixation2"
  fixation2Clock = new util.Clock();
  text_fixation2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_fixation2',
    text: '+',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "phase3"
  phase3Clock = new util.Clock();
  image_ph3Q = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_ph3Q', units : undefined, 
    image : 'img/img_instruction/ph3.png', mask : undefined,
    ori : 0.0, pos : [0, 0.2], size : [1, 0.6],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  image_1axis = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_1axis', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [(- 0.2), 0], size : [0.2, 0.7],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  image_2axis = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_2axis', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0.2, 0], size : [0.2, 0.7],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  image_leftbutton = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_leftbutton', units : undefined, 
    image : 'img/img_button/1button.jpg', mask : undefined,
    ori : 0.0, pos : [(- 0.2), (- 0.4)], size : [0.18, 0.1],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  image_rightbutton = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_rightbutton', units : undefined, 
    image : 'img/img_button/2button.jpg', mask : undefined,
    ori : 0.0, pos : [0.2, (- 0.4)], size : [0.18, 0.1],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  mouse = new core.Mouse({
    win: psychoJS.window,
  });
  mouse.mouseClock = new util.Clock();
  count_num = 0;
  
  image_ph3axisnow2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_ph3axisnow2', units : undefined, 
    image : 'img/img_button/5axis_now.jpg', mask : undefined,
    ori : 0.0, pos : [0.2, (- 0.31)], size : [0.1, 0.06],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -7.0 
  });
  image_ph3axisnow1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_ph3axisnow1', units : undefined, 
    image : 'img/img_button/5axis_now.jpg', mask : undefined,
    ori : 0.0, pos : [(- 0.2), (- 0.31)], size : [0.1, 0.06],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -8.0 
  });
  // Initialize components for Routine "phase4intro"
  phase4introClock = new util.Clock();
  image_4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_4', units : undefined, 
    image : 'img/img_instruction/ph4intro.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.2, 0.6],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  key_resp_6 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "countdown"
  countdownClock = new util.Clock();
  text_countdownsecond = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_countdownsecond',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "ph4threat_image"
  ph4threat_imageClock = new util.Clock();
  image_5 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_5', units : undefined, 
    image : 'img/img_horriblethreat/horriblethreatfinal.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "stop"
  stopClock = new util.Clock();
  text_stop = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_stop',
    text: 'thanks',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var gotValidClick;
var introComponents;
function introRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'intro'-------
    t = 0;
    introClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    input_name.setText('');
    // setup some python lists for storing info about the mouse_3
    mouse_3.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    introComponents = [];
    introComponents.push(introduction);
    introComponents.push(input_name);
    introComponents.push(image_myself);
    introComponents.push(image_nextbutton);
    introComponents.push(mouse_3);
    
    introComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var prevButtonState;
var _mouseButtons;
function introRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'intro'-------
    // get current time
    t = introClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *introduction* updates
    if (t >= 0.0 && introduction.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      introduction.tStart = t;  // (not accounting for frame time here)
      introduction.frameNStart = frameN;  // exact frame index
      
      introduction.setAutoDraw(true);
    }

    
    // *input_name* updates
    if (t >= 0.0 && input_name.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      input_name.tStart = t;  // (not accounting for frame time here)
      input_name.frameNStart = frameN;  // exact frame index
      
      input_name.setAutoDraw(true);
    }

    
    // *image_myself* updates
    if (t >= 0.0 && image_myself.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_myself.tStart = t;  // (not accounting for frame time here)
      image_myself.frameNStart = frameN;  // exact frame index
      
      image_myself.setAutoDraw(true);
    }

    
    // *image_nextbutton* updates
    if (t >= 0.0 && image_nextbutton.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_nextbutton.tStart = t;  // (not accounting for frame time here)
      image_nextbutton.frameNStart = frameN;  // exact frame index
      
      image_nextbutton.setAutoDraw(true);
    }

    // *mouse_3* updates
    if (t >= 0.0 && mouse_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_3.tStart = t;  // (not accounting for frame time here)
      mouse_3.frameNStart = frameN;  // exact frame index
      
      mouse_3.status = PsychoJS.Status.STARTED;
      mouse_3.mouseClock.reset();
      prevButtonState = mouse_3.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_3.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_3.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [image_nextbutton]) {
            if (obj.contains(mouse_3)) {
              gotValidClick = true;
              mouse_3.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    introComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var _mouseXYs;
function introRoutineEnd() {
  return async function () {
    //------Ending Routine 'intro'-------
    introComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('input_name.text',input_name.text)
    // store data for psychoJS.experiment (ExperimentHandler)
    _mouseXYs = mouse_3.getPos();
    _mouseButtons = mouse_3.getPressed();
    psychoJS.experiment.addData('mouse_3.x', _mouseXYs[0]);
    psychoJS.experiment.addData('mouse_3.y', _mouseXYs[1]);
    psychoJS.experiment.addData('mouse_3.leftButton', _mouseButtons[0]);
    psychoJS.experiment.addData('mouse_3.midButton', _mouseButtons[1]);
    psychoJS.experiment.addData('mouse_3.rightButton', _mouseButtons[2]);
    if (mouse_3.clicked_name.length > 0) {
      psychoJS.experiment.addData('mouse_3.clicked_name', mouse_3.clicked_name[0]);}
    // the Routine "intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_allKeys;
var phase1intro_2Components;
function phase1intro_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'phase1intro_2'-------
    t = 0;
    phase1intro_2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    phase1intro_2Components = [];
    phase1intro_2Components.push(image_phase1intro);
    phase1intro_2Components.push(key_resp);
    
    phase1intro_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function phase1intro_2RoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'phase1intro_2'-------
    // get current time
    t = phase1intro_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_phase1intro* updates
    if (t >= 0.0 && image_phase1intro.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_phase1intro.tStart = t;  // (not accounting for frame time here)
      image_phase1intro.frameNStart = frameN;  // exact frame index
      
      image_phase1intro.setAutoDraw(true);
    }

    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    phase1intro_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function phase1intro_2RoutineEnd() {
  return async function () {
    //------Ending Routine 'phase1intro_2'-------
    phase1intro_2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "phase1intro_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var trials_horribleimg;
var currentLoop;
function trials_horribleimgLoopBegin(trials_horribleimgLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_horribleimg = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'cond/horriblepicture.xlsx',
      seed: undefined, name: 'trials_horribleimg'
    });
    psychoJS.experiment.addLoop(trials_horribleimg); // add the loop to the experiment
    currentLoop = trials_horribleimg;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials_horribleimg.forEach(function() {
      const snapshot = trials_horribleimg.getSnapshot();
    
      trials_horribleimgLoopScheduler.add(importConditions(snapshot));
      trials_horribleimgLoopScheduler.add(fixationRoutineBegin(snapshot));
      trials_horribleimgLoopScheduler.add(fixationRoutineEachFrame());
      trials_horribleimgLoopScheduler.add(fixationRoutineEnd());
      trials_horribleimgLoopScheduler.add(phase1RoutineBegin(snapshot));
      trials_horribleimgLoopScheduler.add(phase1RoutineEachFrame());
      trials_horribleimgLoopScheduler.add(phase1RoutineEnd());
      trials_horribleimgLoopScheduler.add(endLoopIteration(trials_horribleimgLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_horribleimgLoopEnd() {
  psychoJS.experiment.removeLoop(trials_horribleimg);

  return Scheduler.Event.NEXT;
}


var trials;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'cond/ph2_cond.xlsx',
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials.forEach(function() {
      const snapshot = trials.getSnapshot();
    
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(Phase2RoutineBegin(snapshot));
      trialsLoopScheduler.add(Phase2RoutineEachFrame());
      trialsLoopScheduler.add(Phase2RoutineEnd());
      trialsLoopScheduler.add(endLoopIteration(trialsLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}


var trials_ph3_2;
function trials_ph3_2LoopBegin(trials_ph3_2LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_ph3_2 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'cond/tabletotal.xlsx',
      seed: undefined, name: 'trials_ph3_2'
    });
    psychoJS.experiment.addLoop(trials_ph3_2); // add the loop to the experiment
    currentLoop = trials_ph3_2;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials_ph3_2.forEach(function() {
      const snapshot = trials_ph3_2.getSnapshot();
    
      trials_ph3_2LoopScheduler.add(importConditions(snapshot));
      const trials_ph3_1LoopScheduler = new Scheduler(psychoJS);
      trials_ph3_2LoopScheduler.add(trials_ph3_1LoopBegin(trials_ph3_1LoopScheduler, snapshot));
      trials_ph3_2LoopScheduler.add(trials_ph3_1LoopScheduler);
      trials_ph3_2LoopScheduler.add(trials_ph3_1LoopEnd);
      trials_ph3_2LoopScheduler.add(endLoopIteration(trials_ph3_2LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


var trials_ph3_1;
function trials_ph3_1LoopBegin(trials_ph3_1LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_ph3_1 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: excel,
      seed: undefined, name: 'trials_ph3_1'
    });
    psychoJS.experiment.addLoop(trials_ph3_1); // add the loop to the experiment
    currentLoop = trials_ph3_1;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials_ph3_1.forEach(function() {
      const snapshot = trials_ph3_1.getSnapshot();
    
      trials_ph3_1LoopScheduler.add(importConditions(snapshot));
      trials_ph3_1LoopScheduler.add(fixation2RoutineBegin(snapshot));
      trials_ph3_1LoopScheduler.add(fixation2RoutineEachFrame());
      trials_ph3_1LoopScheduler.add(fixation2RoutineEnd());
      trials_ph3_1LoopScheduler.add(phase3RoutineBegin(snapshot));
      trials_ph3_1LoopScheduler.add(phase3RoutineEachFrame());
      trials_ph3_1LoopScheduler.add(phase3RoutineEnd());
      trials_ph3_1LoopScheduler.add(endLoopIteration(trials_ph3_1LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_ph3_1LoopEnd() {
  psychoJS.experiment.removeLoop(trials_ph3_1);

  return Scheduler.Event.NEXT;
}


async function trials_ph3_2LoopEnd() {
  psychoJS.experiment.removeLoop(trials_ph3_2);

  return Scheduler.Event.NEXT;
}


var trials_countdown;
function trials_countdownLoopBegin(trials_countdownLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_countdown = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'cond/countdownsecond.xlsx',
      seed: undefined, name: 'trials_countdown'
    });
    psychoJS.experiment.addLoop(trials_countdown); // add the loop to the experiment
    currentLoop = trials_countdown;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials_countdown.forEach(function() {
      const snapshot = trials_countdown.getSnapshot();
    
      trials_countdownLoopScheduler.add(importConditions(snapshot));
      trials_countdownLoopScheduler.add(countdownRoutineBegin(snapshot));
      trials_countdownLoopScheduler.add(countdownRoutineEachFrame());
      trials_countdownLoopScheduler.add(countdownRoutineEnd());
      trials_countdownLoopScheduler.add(endLoopIteration(trials_countdownLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_countdownLoopEnd() {
  psychoJS.experiment.removeLoop(trials_countdown);

  return Scheduler.Event.NEXT;
}


var fixationComponents;
function fixationRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'fixation'-------
    t = 0;
    fixationClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    fixationComponents = [];
    fixationComponents.push(text_fixation);
    
    fixationComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function fixationRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'fixation'-------
    // get current time
    t = fixationClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_fixation* updates
    if (t >= 0.0 && text_fixation.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_fixation.tStart = t;  // (not accounting for frame time here)
      text_fixation.frameNStart = frameN;  // exact frame index
      
      text_fixation.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_fixation.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_fixation.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    fixationComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function fixationRoutineEnd() {
  return async function () {
    //------Ending Routine 'fixation'-------
    fixationComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var phase1Components;
function phase1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'phase1'-------
    t = 0;
    phase1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    image_horrible.setImage(horriblepic);
    slider_evl1.reset()
    slider_evl2.reset()
    // setup some python lists for storing info about the mouse_2
    mouse_2.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    phase1Components = [];
    phase1Components.push(image_horrible);
    phase1Components.push(slider_evl1);
    phase1Components.push(image_evl1);
    phase1Components.push(image_evl2);
    phase1Components.push(slider_evl2);
    phase1Components.push(image_3button);
    phase1Components.push(mouse_2);
    
    phase1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function phase1RoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'phase1'-------
    // get current time
    t = phase1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_horrible* updates
    if (t >= 0.0 && image_horrible.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_horrible.tStart = t;  // (not accounting for frame time here)
      image_horrible.frameNStart = frameN;  // exact frame index
      
      image_horrible.setAutoDraw(true);
    }

    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_horrible.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_horrible.setAutoDraw(false);
    }
    
    // *slider_evl1* updates
    if (t >= 5 && slider_evl1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider_evl1.tStart = t;  // (not accounting for frame time here)
      slider_evl1.frameNStart = frameN;  // exact frame index
      
      slider_evl1.setAutoDraw(true);
    }

    
    // *image_evl1* updates
    if (t >= 5 && image_evl1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_evl1.tStart = t;  // (not accounting for frame time here)
      image_evl1.frameNStart = frameN;  // exact frame index
      
      image_evl1.setAutoDraw(true);
    }

    
    // *image_evl2* updates
    if (t >= 5 && image_evl2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_evl2.tStart = t;  // (not accounting for frame time here)
      image_evl2.frameNStart = frameN;  // exact frame index
      
      image_evl2.setAutoDraw(true);
    }

    
    // *slider_evl2* updates
    if (t >= 5 && slider_evl2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider_evl2.tStart = t;  // (not accounting for frame time here)
      slider_evl2.frameNStart = frameN;  // exact frame index
      
      slider_evl2.setAutoDraw(true);
    }

    
    // *image_3button* updates
    if (t >= 5 && image_3button.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_3button.tStart = t;  // (not accounting for frame time here)
      image_3button.frameNStart = frameN;  // exact frame index
      
      image_3button.setAutoDraw(true);
    }

    // *mouse_2* updates
    if (t >= 5 && mouse_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_2.tStart = t;  // (not accounting for frame time here)
      mouse_2.frameNStart = frameN;  // exact frame index
      
      mouse_2.status = PsychoJS.Status.STARTED;
      mouse_2.mouseClock.reset();
      prevButtonState = mouse_2.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_2.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_2.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [image_3button]) {
            if (obj.contains(mouse_2)) {
              gotValidClick = true;
              mouse_2.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    phase1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function phase1RoutineEnd() {
  return async function () {
    //------Ending Routine 'phase1'-------
    phase1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('slider_evl1.response', slider_evl1.getRating());
    psychoJS.experiment.addData('slider_evl1.rt', slider_evl1.getRT());
    psychoJS.experiment.addData('slider_evl2.response', slider_evl2.getRating());
    psychoJS.experiment.addData('slider_evl2.rt', slider_evl2.getRT());
    // store data for psychoJS.experiment (ExperimentHandler)
    _mouseXYs = mouse_2.getPos();
    _mouseButtons = mouse_2.getPressed();
    psychoJS.experiment.addData('mouse_2.x', _mouseXYs[0]);
    psychoJS.experiment.addData('mouse_2.y', _mouseXYs[1]);
    psychoJS.experiment.addData('mouse_2.leftButton', _mouseButtons[0]);
    psychoJS.experiment.addData('mouse_2.midButton', _mouseButtons[1]);
    psychoJS.experiment.addData('mouse_2.rightButton', _mouseButtons[2]);
    if (mouse_2.clicked_name.length > 0) {
      psychoJS.experiment.addData('mouse_2.clicked_name', mouse_2.clicked_name[0]);}
    // the Routine "phase1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_5_allKeys;
var phase2introComponents;
function phase2introRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'phase2intro'-------
    t = 0;
    phase2introClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_5.keys = undefined;
    key_resp_5.rt = undefined;
    _key_resp_5_allKeys = [];
    // keep track of which components have finished
    phase2introComponents = [];
    phase2introComponents.push(image_phase2intro);
    phase2introComponents.push(key_resp_5);
    
    phase2introComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function phase2introRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'phase2intro'-------
    // get current time
    t = phase2introClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_phase2intro* updates
    if (t >= 0.0 && image_phase2intro.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_phase2intro.tStart = t;  // (not accounting for frame time here)
      image_phase2intro.frameNStart = frameN;  // exact frame index
      
      image_phase2intro.setAutoDraw(true);
    }

    
    // *key_resp_5* updates
    if (t >= 0.0 && key_resp_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_5.tStart = t;  // (not accounting for frame time here)
      key_resp_5.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_5.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.clearEvents(); });
    }

    if (key_resp_5.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_5.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_5_allKeys = _key_resp_5_allKeys.concat(theseKeys);
      if (_key_resp_5_allKeys.length > 0) {
        key_resp_5.keys = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].name;  // just the last key pressed
        key_resp_5.rt = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    phase2introComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function phase2introRoutineEnd() {
  return async function () {
    //------Ending Routine 'phase2intro'-------
    phase2introComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_5.keys', key_resp_5.keys);
    if (typeof key_resp_5.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_5.rt', key_resp_5.rt);
        routineTimer.reset();
        }
    
    key_resp_5.stop();
    // the Routine "phase2intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var list_loc_1;
var temp_1;
var temp_2;
var temp_3;
var temp_4;
var Phase2Components;
function Phase2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Phase2'-------
    t = 0;
    Phase2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    list_loc_1 = [(- 0.35), (- 0.05), 0.25, 0.55];
    util.shuffle(list_1);
    util.shuffle(list_2);
    util.shuffle(list_3);
    util.shuffle(list_4);
    util.shuffle(list_loc_1);
    loc_x_1 = list_loc_1[0];
    loc_x_2 = list_loc_1[1];
    loc_x_3 = list_loc_1[2];
    loc_x_4 = list_loc_1[3];
    if ((list_1[0] === 1)) {
        pic_1 = ph2_pic60_1;
        list_1_remove.push(1);
    }
    if ((list_1[0] === 2)) {
        pic_1 = ph2_pic60_2;
        list_1_remove.push(2);
    }
    if ((list_1[0] === 3)) {
        pic_1 = ph2_pic60_3;
        list_1_remove.push(3);
    }
    if ((list_1[0] === 4)) {
        pic_1 = ph2_pic60_4;
        list_1_remove.push(4);
    }
    if ((list_1[0] === 5)) {
        pic_1 = ph2_pic60_5;
        list_1_remove.push(5);
    }
    if ((list_1[0] === 6)) {
        pic_1 = ph2_pic60_6;
        list_1_remove.push(6);
    }
    if ((list_1[0] === 7)) {
        pic_1 = ph2_pic60_7;
        list_1_remove.push(7);
    }
    if ((list_1[0] === 8)) {
        pic_1 = ph2_pic60_8;
        list_1_remove.push(8);
    }
    if ((list_1[0] === 9)) {
        pic_1 = ph2_pic60_9;
        list_1_remove.push(9);
    }
    temp_1 = list_1[0];
    temp_2 = list_2[0];
    temp_3 = list_3[0];
    temp_4 = list_4[0];
    if ((list_2[0] === 1)) {
        pic_2 = ph2_pic70_1;
        list_2_remove.push(1);
    }
    if ((list_2[0] === 2)) {
        pic_2 = ph2_pic70_2;
        list_2_remove.push(2);
    }
    if ((list_2[0] === 3)) {
        pic_2 = ph2_pic70_3;
        list_2_remove.push(3);
    }
    if ((list_2[0] === 4)) {
        pic_2 = ph2_pic70_4;
        list_2_remove.push(4);
    }
    if ((list_2[0] === 5)) {
        pic_2 = ph2_pic70_5;
        list_2_remove.push(5);
    }
    if ((list_2[0] === 6)) {
        pic_2 = ph2_pic70_6;
        list_2_remove.push(6);
    }
    if ((list_2[0] === 7)) {
        pic_2 = ph2_pic70_7;
        list_2_remove.push(7);
    }
    if ((list_2[0] === 8)) {
        pic_2 = ph2_pic70_8;
        list_2_remove.push(8);
    }
    if ((list_2[0] === 9)) {
        pic_2 = ph2_pic70_9;
        list_2_remove.push(9);
    }
    if ((list_3[0] === 1)) {
        pic_3 = ph2_pic80_1;
        list_3_remove.push(1);
    }
    if ((list_3[0] === 2)) {
        pic_3 = ph2_pic80_2;
        list_3_remove.push(2);
    }
    if ((list_3[0] === 3)) {
        pic_3 = ph2_pic80_3;
        list_3_remove.push(3);
    }
    if ((list_3[0] === 4)) {
        pic_3 = ph2_pic80_4;
        list_3_remove.push(4);
    }
    if ((list_3[0] === 5)) {
        pic_3 = ph2_pic80_5;
        list_3_remove.push(5);
    }
    if ((list_3[0] === 6)) {
        pic_3 = ph2_pic80_6;
        list_3_remove.push(6);
    }
    if ((list_3[0] === 7)) {
        pic_3 = ph2_pic80_7;
        list_3_remove.push(7);
    }
    if ((list_3[0] === 8)) {
        pic_3 = ph2_pic80_8;
        list_3_remove.push(8);
    }
    if ((list_3[0] === 9)) {
        pic_3 = ph2_pic80_9;
        list_3_remove.push(9);
    }
    if ((list_4[0] === 1)) {
        pic_4 = ph2_pic90_1;
        list_4_remove.push(1);
    }
    if ((list_4[0] === 2)) {
        pic_4 = ph2_pic90_2;
        list_4_remove.push(2);
    }
    if ((list_4[0] === 3)) {
        pic_4 = ph2_pic90_3;
        list_4_remove.push(3);
    }
    if ((list_4[0] === 4)) {
        pic_4 = ph2_pic90_4;
        list_4_remove.push(4);
    }
    if ((list_4[0] === 5)) {
        pic_4 = ph2_pic90_5;
        list_4_remove.push(5);
    }
    if ((list_4[0] === 6)) {
        pic_4 = ph2_pic90_6;
        list_4_remove.push(6);
    }
    if ((list_4[0] === 7)) {
        pic_4 = ph2_pic90_7;
        list_4_remove.push(7);
    }
    if ((list_4[0] === 8)) {
        pic_4 = ph2_pic90_8;
        list_4_remove.push(8);
    }
    if ((list_4[0] === 9)) {
        pic_4 = ph2_pic90_9;
        list_4_remove.push(9);
    }
    
    image_ax1.setPos([loc_x_1, 0]);
    image_ax1.setImage(pic_1);
    image_ax2.setPos([loc_x_2, 0]);
    image_ax2.setImage(pic_2);
    image_ax3.setPos([loc_x_3, 0]);
    image_ax3.setImage(pic_3);
    image_ax4.setPos([loc_x_4, 0]);
    image_ax4.setImage(pic_4);
    image_buttonA.setImage('img/img_button_ph2/button_A.jpg');
    image_buttonB.setImage('img/img_button_ph2/button_B.jpg');
    image_buttonC.setImage('img/img_button_ph2/button_C.jpg');
    image_buttonD.setImage('img/img_button_ph2/button_D.jpg');
    image_personpic.setImage(person_img);
    // setup some python lists for storing info about the mouse_A
    mouse_A.clicked_name = [];
    gotValidClick = false; // until a click is received
    // setup some python lists for storing info about the mouse_B
    mouse_B.clicked_name = [];
    gotValidClick = false; // until a click is received
    // setup some python lists for storing info about the mouse_C
    mouse_C.clicked_name = [];
    gotValidClick = false; // until a click is received
    // setup some python lists for storing info about the mouse_D
    mouse_D.clicked_name = [];
    gotValidClick = false; // until a click is received
    text_personname.setText(person_name);
    // keep track of which components have finished
    Phase2Components = [];
    Phase2Components.push(image_ax1);
    Phase2Components.push(image_ax2);
    Phase2Components.push(image_ax3);
    Phase2Components.push(image_ax4);
    Phase2Components.push(image_buttonA);
    Phase2Components.push(image_buttonB);
    Phase2Components.push(image_buttonC);
    Phase2Components.push(image_buttonD);
    Phase2Components.push(image_personpic);
    Phase2Components.push(mouse_A);
    Phase2Components.push(mouse_B);
    Phase2Components.push(mouse_C);
    Phase2Components.push(mouse_D);
    Phase2Components.push(text_personname);
    Phase2Components.push(image_ph2axisnow1);
    Phase2Components.push(image_ph2axisnow2);
    Phase2Components.push(image_ph2axisnow3);
    Phase2Components.push(image_ph2axisnow4);
    
    Phase2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Phase2RoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Phase2'-------
    // get current time
    t = Phase2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_ax1* updates
    if (t >= 0.0 && image_ax1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_ax1.tStart = t;  // (not accounting for frame time here)
      image_ax1.frameNStart = frameN;  // exact frame index
      
      image_ax1.setAutoDraw(true);
    }

    
    // *image_ax2* updates
    if (t >= 0.0 && image_ax2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_ax2.tStart = t;  // (not accounting for frame time here)
      image_ax2.frameNStart = frameN;  // exact frame index
      
      image_ax2.setAutoDraw(true);
    }

    
    // *image_ax3* updates
    if (t >= 0.0 && image_ax3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_ax3.tStart = t;  // (not accounting for frame time here)
      image_ax3.frameNStart = frameN;  // exact frame index
      
      image_ax3.setAutoDraw(true);
    }

    
    // *image_ax4* updates
    if (t >= 0.0 && image_ax4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_ax4.tStart = t;  // (not accounting for frame time here)
      image_ax4.frameNStart = frameN;  // exact frame index
      
      image_ax4.setAutoDraw(true);
    }

    
    // *image_buttonA* updates
    if (t >= 0.0 && image_buttonA.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_buttonA.tStart = t;  // (not accounting for frame time here)
      image_buttonA.frameNStart = frameN;  // exact frame index
      
      image_buttonA.setAutoDraw(true);
    }

    
    // *image_buttonB* updates
    if (t >= 0.0 && image_buttonB.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_buttonB.tStart = t;  // (not accounting for frame time here)
      image_buttonB.frameNStart = frameN;  // exact frame index
      
      image_buttonB.setAutoDraw(true);
    }

    
    // *image_buttonC* updates
    if (t >= 0.0 && image_buttonC.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_buttonC.tStart = t;  // (not accounting for frame time here)
      image_buttonC.frameNStart = frameN;  // exact frame index
      
      image_buttonC.setAutoDraw(true);
    }

    
    // *image_buttonD* updates
    if (t >= 0.0 && image_buttonD.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_buttonD.tStart = t;  // (not accounting for frame time here)
      image_buttonD.frameNStart = frameN;  // exact frame index
      
      image_buttonD.setAutoDraw(true);
    }

    
    // *image_personpic* updates
    if (t >= 0.0 && image_personpic.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_personpic.tStart = t;  // (not accounting for frame time here)
      image_personpic.frameNStart = frameN;  // exact frame index
      
      image_personpic.setAutoDraw(true);
    }

    // *mouse_A* updates
    if (t >= 0.0 && mouse_A.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_A.tStart = t;  // (not accounting for frame time here)
      mouse_A.frameNStart = frameN;  // exact frame index
      
      mouse_A.status = PsychoJS.Status.STARTED;
      mouse_A.mouseClock.reset();
      prevButtonState = mouse_A.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_A.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_A.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [image_buttonA,image_buttonB,image_buttonC,image_buttonD]) {
            if (obj.contains(mouse_A)) {
              gotValidClick = true;
              mouse_A.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // *mouse_B* updates
    if (t >= 0.0 && mouse_B.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_B.tStart = t;  // (not accounting for frame time here)
      mouse_B.frameNStart = frameN;  // exact frame index
      
      mouse_B.status = PsychoJS.Status.STARTED;
      mouse_B.mouseClock.reset();
      prevButtonState = mouse_B.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_B.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_B.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [image_buttonA,image_buttonB,image_buttonC,image_buttonD]) {
            if (obj.contains(mouse_B)) {
              gotValidClick = true;
              mouse_B.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // *mouse_C* updates
    if (t >= 0.0 && mouse_C.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_C.tStart = t;  // (not accounting for frame time here)
      mouse_C.frameNStart = frameN;  // exact frame index
      
      mouse_C.status = PsychoJS.Status.STARTED;
      mouse_C.mouseClock.reset();
      prevButtonState = mouse_C.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_C.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_C.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [image_buttonA,image_buttonB,image_buttonC,image_buttonD]) {
            if (obj.contains(mouse_C)) {
              gotValidClick = true;
              mouse_C.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // *mouse_D* updates
    if (t >= 0.0 && mouse_D.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_D.tStart = t;  // (not accounting for frame time here)
      mouse_D.frameNStart = frameN;  // exact frame index
      
      mouse_D.status = PsychoJS.Status.STARTED;
      mouse_D.mouseClock.reset();
      prevButtonState = mouse_D.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_D.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_D.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [image_buttonA,image_buttonB,image_buttonC,image_buttonD]) {
            if (obj.contains(mouse_D)) {
              gotValidClick = true;
              mouse_D.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *text_personname* updates
    if (t >= 0.0 && text_personname.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_personname.tStart = t;  // (not accounting for frame time here)
      text_personname.frameNStart = frameN;  // exact frame index
      
      text_personname.setAutoDraw(true);
    }

    
    // *image_ph2axisnow1* updates
    if (t >= 0.0 && image_ph2axisnow1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_ph2axisnow1.tStart = t;  // (not accounting for frame time here)
      image_ph2axisnow1.frameNStart = frameN;  // exact frame index
      
      image_ph2axisnow1.setAutoDraw(true);
    }

    
    // *image_ph2axisnow2* updates
    if (t >= 0.0 && image_ph2axisnow2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_ph2axisnow2.tStart = t;  // (not accounting for frame time here)
      image_ph2axisnow2.frameNStart = frameN;  // exact frame index
      
      image_ph2axisnow2.setAutoDraw(true);
    }

    
    // *image_ph2axisnow3* updates
    if (t >= 0.0 && image_ph2axisnow3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_ph2axisnow3.tStart = t;  // (not accounting for frame time here)
      image_ph2axisnow3.frameNStart = frameN;  // exact frame index
      
      image_ph2axisnow3.setAutoDraw(true);
    }

    
    // *image_ph2axisnow4* updates
    if (t >= 0.0 && image_ph2axisnow4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_ph2axisnow4.tStart = t;  // (not accounting for frame time here)
      image_ph2axisnow4.frameNStart = frameN;  // exact frame index
      
      image_ph2axisnow4.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Phase2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var _pj;
var list_temp1;
var list_temp2;
var list_temp3;
var list_temp4;
function Phase2RoutineEnd() {
  return async function () {
    //------Ending Routine 'Phase2'-------
    Phase2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    list_temp1 = [];
    list_temp2 = [];
    list_temp3 = [];
    list_temp4 = [];
    if ((list_1.length > 1)) {
        for (var i, _pj_c = 0, _pj_a = list_1, _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
            i = _pj_a[_pj_c];
            if ((! _pj.in_es6(i, list_1_remove))) {
                list_temp1.push(i);
            }
        }
        list_1 = list_temp1;
    }
    if ((list_2.length > 1)) {
        for (var i, _pj_c = 0, _pj_a = list_2, _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
            i = _pj_a[_pj_c];
            if ((! _pj.in_es6(i, list_2_remove))) {
                list_temp2.push(i);
            }
        }
        list_2 = list_temp2;
    }
    if ((list_3.length > 1)) {
        for (var i, _pj_c = 0, _pj_a = list_3, _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
            i = _pj_a[_pj_c];
            if ((! _pj.in_es6(i, list_3_remove))) {
                list_temp3.push(i);
            }
        }
        list_3 = list_temp3;
    }
    if ((list_4.length > 1)) {
        for (var i, _pj_c = 0, _pj_a = list_4, _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
            i = _pj_a[_pj_c];
            if ((! _pj.in_es6(i, list_4_remove))) {
                list_temp4.push(i);
            }
        }
        list_4 = list_temp4;
    }
    console.log(list_1_remove);
    console.log(list_2_remove);
    console.log(list_3_remove);
    console.log(list_4_remove);
    console.log(loc_x_1);
    console.log(loc_x_2);
    console.log(loc_x_3);
    console.log(loc_x_4);
    
    // store data for psychoJS.experiment (ExperimentHandler)
    _mouseXYs = mouse_A.getPos();
    _mouseButtons = mouse_A.getPressed();
    psychoJS.experiment.addData('mouse_A.x', _mouseXYs[0]);
    psychoJS.experiment.addData('mouse_A.y', _mouseXYs[1]);
    psychoJS.experiment.addData('mouse_A.leftButton', _mouseButtons[0]);
    psychoJS.experiment.addData('mouse_A.midButton', _mouseButtons[1]);
    psychoJS.experiment.addData('mouse_A.rightButton', _mouseButtons[2]);
    if (mouse_A.clicked_name.length > 0) {
      psychoJS.experiment.addData('mouse_A.clicked_name', mouse_A.clicked_name[0]);}
    // store data for psychoJS.experiment (ExperimentHandler)
    _mouseXYs = mouse_B.getPos();
    _mouseButtons = mouse_B.getPressed();
    psychoJS.experiment.addData('mouse_B.x', _mouseXYs[0]);
    psychoJS.experiment.addData('mouse_B.y', _mouseXYs[1]);
    psychoJS.experiment.addData('mouse_B.leftButton', _mouseButtons[0]);
    psychoJS.experiment.addData('mouse_B.midButton', _mouseButtons[1]);
    psychoJS.experiment.addData('mouse_B.rightButton', _mouseButtons[2]);
    if (mouse_B.clicked_name.length > 0) {
      psychoJS.experiment.addData('mouse_B.clicked_name', mouse_B.clicked_name[0]);}
    // store data for psychoJS.experiment (ExperimentHandler)
    _mouseXYs = mouse_C.getPos();
    _mouseButtons = mouse_C.getPressed();
    psychoJS.experiment.addData('mouse_C.x', _mouseXYs[0]);
    psychoJS.experiment.addData('mouse_C.y', _mouseXYs[1]);
    psychoJS.experiment.addData('mouse_C.leftButton', _mouseButtons[0]);
    psychoJS.experiment.addData('mouse_C.midButton', _mouseButtons[1]);
    psychoJS.experiment.addData('mouse_C.rightButton', _mouseButtons[2]);
    if (mouse_C.clicked_name.length > 0) {
      psychoJS.experiment.addData('mouse_C.clicked_name', mouse_C.clicked_name[0]);}
    // store data for psychoJS.experiment (ExperimentHandler)
    _mouseXYs = mouse_D.getPos();
    _mouseButtons = mouse_D.getPressed();
    psychoJS.experiment.addData('mouse_D.x', _mouseXYs[0]);
    psychoJS.experiment.addData('mouse_D.y', _mouseXYs[1]);
    psychoJS.experiment.addData('mouse_D.leftButton', _mouseButtons[0]);
    psychoJS.experiment.addData('mouse_D.midButton', _mouseButtons[1]);
    psychoJS.experiment.addData('mouse_D.rightButton', _mouseButtons[2]);
    if (mouse_D.clicked_name.length > 0) {
      psychoJS.experiment.addData('mouse_D.clicked_name', mouse_D.clicked_name[0]);}
    // the Routine "Phase2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_4_allKeys;
var phase3introComponents;
function phase3introRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'phase3intro'-------
    t = 0;
    phase3introClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_4.keys = undefined;
    key_resp_4.rt = undefined;
    _key_resp_4_allKeys = [];
    // keep track of which components have finished
    phase3introComponents = [];
    phase3introComponents.push(image_2);
    phase3introComponents.push(key_resp_4);
    
    phase3introComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function phase3introRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'phase3intro'-------
    // get current time
    t = phase3introClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_2* updates
    if (t >= 0.0 && image_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_2.tStart = t;  // (not accounting for frame time here)
      image_2.frameNStart = frameN;  // exact frame index
      
      image_2.setAutoDraw(true);
    }

    
    // *key_resp_4* updates
    if (t >= 0.0 && key_resp_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_4.tStart = t;  // (not accounting for frame time here)
      key_resp_4.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_4.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.clearEvents(); });
    }

    if (key_resp_4.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_4.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_4_allKeys = _key_resp_4_allKeys.concat(theseKeys);
      if (_key_resp_4_allKeys.length > 0) {
        key_resp_4.keys = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].name;  // just the last key pressed
        key_resp_4.rt = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    phase3introComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function phase3introRoutineEnd() {
  return async function () {
    //------Ending Routine 'phase3intro'-------
    phase3introComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_4.keys', key_resp_4.keys);
    if (typeof key_resp_4.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_4.rt', key_resp_4.rt);
        routineTimer.reset();
        }
    
    key_resp_4.stop();
    // the Routine "phase3intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var fixation2Components;
function fixation2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'fixation2'-------
    t = 0;
    fixation2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.500000);
    // update component parameters for each repeat
    // keep track of which components have finished
    fixation2Components = [];
    fixation2Components.push(text_fixation2);
    
    fixation2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function fixation2RoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'fixation2'-------
    // get current time
    t = fixation2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_fixation2* updates
    if (t >= 0.0 && text_fixation2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_fixation2.tStart = t;  // (not accounting for frame time here)
      text_fixation2.frameNStart = frameN;  // exact frame index
      
      text_fixation2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_fixation2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_fixation2.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    fixation2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function fixation2RoutineEnd() {
  return async function () {
    //------Ending Routine 'fixation2'-------
    fixation2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var img_2_loc;
var img_1_loc;
var phase3Components;
function phase3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'phase3'-------
    t = 0;
    phase3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    image_1axis.setImage(pic_left);
    image_2axis.setImage(pic_right);
    // setup some python lists for storing info about the mouse
    mouse.clicked_name = [];
    gotValidClick = false; // until a click is received
    count_num += 1;
    img_2_loc = pic_left;
    img_1_loc = pic_right;
    list_1 = [1, 2];
    util.shuffle(list_1);
    if ((list_1[0] === 2)) {
        img_2_loc = pic_left;
        img_1_loc = pic_right;
    } else {
        img_2_loc = pic_right;
        img_1_loc = pic_left;
    }
    
    // keep track of which components have finished
    phase3Components = [];
    phase3Components.push(image_ph3Q);
    phase3Components.push(image_1axis);
    phase3Components.push(image_2axis);
    phase3Components.push(image_leftbutton);
    phase3Components.push(image_rightbutton);
    phase3Components.push(mouse);
    phase3Components.push(image_ph3axisnow2);
    phase3Components.push(image_ph3axisnow1);
    
    phase3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function phase3RoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'phase3'-------
    // get current time
    t = phase3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_ph3Q* updates
    if (t >= 0.0 && image_ph3Q.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_ph3Q.tStart = t;  // (not accounting for frame time here)
      image_ph3Q.frameNStart = frameN;  // exact frame index
      
      image_ph3Q.setAutoDraw(true);
    }

    
    // *image_1axis* updates
    if (t >= 0.0 && image_1axis.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_1axis.tStart = t;  // (not accounting for frame time here)
      image_1axis.frameNStart = frameN;  // exact frame index
      
      image_1axis.setAutoDraw(true);
    }

    
    // *image_2axis* updates
    if (t >= 0.0 && image_2axis.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_2axis.tStart = t;  // (not accounting for frame time here)
      image_2axis.frameNStart = frameN;  // exact frame index
      
      image_2axis.setAutoDraw(true);
    }

    
    // *image_leftbutton* updates
    if (t >= 0.0 && image_leftbutton.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_leftbutton.tStart = t;  // (not accounting for frame time here)
      image_leftbutton.frameNStart = frameN;  // exact frame index
      
      image_leftbutton.setAutoDraw(true);
    }

    
    // *image_rightbutton* updates
    if (t >= 0.0 && image_rightbutton.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_rightbutton.tStart = t;  // (not accounting for frame time here)
      image_rightbutton.frameNStart = frameN;  // exact frame index
      
      image_rightbutton.setAutoDraw(true);
    }

    // *mouse* updates
    if (t >= 0.0 && mouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse.tStart = t;  // (not accounting for frame time here)
      mouse.frameNStart = frameN;  // exact frame index
      
      mouse.status = PsychoJS.Status.STARTED;
      mouse.mouseClock.reset();
      prevButtonState = mouse.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [image_leftbutton,image_rightbutton]) {
            if (obj.contains(mouse)) {
              gotValidClick = true;
              mouse.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *image_ph3axisnow2* updates
    if (t >= 0.0 && image_ph3axisnow2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_ph3axisnow2.tStart = t;  // (not accounting for frame time here)
      image_ph3axisnow2.frameNStart = frameN;  // exact frame index
      
      image_ph3axisnow2.setAutoDraw(true);
    }

    
    // *image_ph3axisnow1* updates
    if (t >= 0.0 && image_ph3axisnow1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_ph3axisnow1.tStart = t;  // (not accounting for frame time here)
      image_ph3axisnow1.frameNStart = frameN;  // exact frame index
      
      image_ph3axisnow1.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    phase3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function phase3RoutineEnd() {
  return async function () {
    //------Ending Routine 'phase3'-------
    phase3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // store data for psychoJS.experiment (ExperimentHandler)
    _mouseXYs = mouse.getPos();
    _mouseButtons = mouse.getPressed();
    psychoJS.experiment.addData('mouse.x', _mouseXYs[0]);
    psychoJS.experiment.addData('mouse.y', _mouseXYs[1]);
    psychoJS.experiment.addData('mouse.leftButton', _mouseButtons[0]);
    psychoJS.experiment.addData('mouse.midButton', _mouseButtons[1]);
    psychoJS.experiment.addData('mouse.rightButton', _mouseButtons[2]);
    if (mouse.clicked_name.length > 0) {
      psychoJS.experiment.addData('mouse.clicked_name', mouse.clicked_name[0]);}
    if ((count_num >= 1)) {
        trials_ph3_1.finished = true;
    }
    
    // the Routine "phase3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_6_allKeys;
var phase4introComponents;
function phase4introRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'phase4intro'-------
    t = 0;
    phase4introClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_6.keys = undefined;
    key_resp_6.rt = undefined;
    _key_resp_6_allKeys = [];
    // keep track of which components have finished
    phase4introComponents = [];
    phase4introComponents.push(image_4);
    phase4introComponents.push(key_resp_6);
    
    phase4introComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function phase4introRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'phase4intro'-------
    // get current time
    t = phase4introClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_4* updates
    if (t >= 0.0 && image_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_4.tStart = t;  // (not accounting for frame time here)
      image_4.frameNStart = frameN;  // exact frame index
      
      image_4.setAutoDraw(true);
    }

    
    // *key_resp_6* updates
    if (t >= 0.0 && key_resp_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_6.tStart = t;  // (not accounting for frame time here)
      key_resp_6.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_6.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.clearEvents(); });
    }

    if (key_resp_6.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_6.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_6_allKeys = _key_resp_6_allKeys.concat(theseKeys);
      if (_key_resp_6_allKeys.length > 0) {
        key_resp_6.keys = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].name;  // just the last key pressed
        key_resp_6.rt = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    phase4introComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function phase4introRoutineEnd() {
  return async function () {
    //------Ending Routine 'phase4intro'-------
    phase4introComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_6.keys', key_resp_6.keys);
    if (typeof key_resp_6.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_6.rt', key_resp_6.rt);
        routineTimer.reset();
        }
    
    key_resp_6.stop();
    // the Routine "phase4intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var countdownComponents;
function countdownRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'countdown'-------
    t = 0;
    countdownClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    text_countdownsecond.setText(countdownsec);
    // keep track of which components have finished
    countdownComponents = [];
    countdownComponents.push(text_countdownsecond);
    
    countdownComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function countdownRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'countdown'-------
    // get current time
    t = countdownClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_countdownsecond* updates
    if (t >= 0.0 && text_countdownsecond.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_countdownsecond.tStart = t;  // (not accounting for frame time here)
      text_countdownsecond.frameNStart = frameN;  // exact frame index
      
      text_countdownsecond.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_countdownsecond.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_countdownsecond.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    countdownComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function countdownRoutineEnd() {
  return async function () {
    //------Ending Routine 'countdown'-------
    countdownComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var ph4threat_imageComponents;
function ph4threat_imageRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'ph4threat_image'-------
    t = 0;
    ph4threat_imageClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    ph4threat_imageComponents = [];
    ph4threat_imageComponents.push(image_5);
    
    ph4threat_imageComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function ph4threat_imageRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'ph4threat_image'-------
    // get current time
    t = ph4threat_imageClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_5* updates
    if (t >= 0.0 && image_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_5.tStart = t;  // (not accounting for frame time here)
      image_5.frameNStart = frameN;  // exact frame index
      
      image_5.setAutoDraw(true);
    }

    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_5.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    ph4threat_imageComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ph4threat_imageRoutineEnd() {
  return async function () {
    //------Ending Routine 'ph4threat_image'-------
    ph4threat_imageComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var stopComponents;
function stopRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'stop'-------
    t = 0;
    stopClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    stopComponents = [];
    stopComponents.push(text_stop);
    
    stopComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function stopRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'stop'-------
    // get current time
    t = stopClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_stop* updates
    if (t >= 0.0 && text_stop.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_stop.tStart = t;  // (not accounting for frame time here)
      text_stop.frameNStart = frameN;  // exact frame index
      
      text_stop.setAutoDraw(true);
    }

    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_stop.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_stop.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    stopComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function stopRoutineEnd() {
  return async function () {
    //------Ending Routine 'stop'-------
    stopComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
