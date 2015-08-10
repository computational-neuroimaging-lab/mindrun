#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.77.00), Mon Aug  5 13:33:44 2013
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""
from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FfINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
from scipy import polyfit # for detrending


# CC some flags
DETREND=1
SUM=0
NUM_PLAYERS=2

# CC some functions
def detrendDist(time,dist):
    if DETREND:
        (slope,offset)=polyfit(time,dist,1)
    else:
        slope=1
        offset=0
        
    curr_dist = dist[-1]
    curr_time = time[-1]

    return curr_dist-(slope*curr_time+offset)



#--- TCPIP RECV - edited below to include IP address and TCP port in dialogue
# Store info about the experiment session
expName = u'net_text'  # from the Builder filename that created this script
expInfo = {'Participant':'', 'Session':'001','IP Address':'127.0.0.1  ', 'TCP Port':'8000'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName, order=['Participant','Session','IP Address','TCP Port'])
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
#--- TCPIP RECV 


# Setup files for saving
if not os.path.isdir('data'):
    os.makedirs('data')  # if this fails (e.g. permissions) we will get error
filename = 'data' + os.path.sep + '%s_%s' %(expInfo['Participant'], expInfo['date'])
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)

#--- TCPIP RECV 
# initialize TCP socket to receive data
import socket
import select
TCP_IP = expInfo['IP Address'].strip() # use localhost
TCP_PORT = int(expInfo['TCP Port'])   # TCP port number
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response

# system calls to initialize the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))

# set socket to non-blocking
try:
    s.setblocking(0)
except:
    print('set non-blocking error')
    core.quit()

# start listening to socket
s.listen(1)

# put up a dialogue to indicate that we are listening for the connection
print('Waiting for connection on %s:%s'%(TCP_IP,TCP_PORT))

ready_to_read, ready_to_write, in_error = select.select([s],[],[],100000)

if ready_to_read:
    conn, addr = s.accept()
else:
    # must be an error
    print('accept failed %s'%(in_error))
    s.close()
    core.quit()

if not conn:
    print('Attempted connection failed');
    s.close()
    core.quit()

print 'Connection address:', addr


#--- TCPIP RECV 


# Setup the Window
#win = visual.Window(size=(1280, 800), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
#    monitor='testMonitor', color=[0,0,0], colorSpace='rgb')

win = visual.Window(size=(1024, 768), fullscr=False, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb')
    
# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
instructions = visual.TextStim(win=win, ori=0, name='instructions',
    text='       Welcome to Mind Run!\n\nBy focusing your attention you control the speed of the runner.\n\nIf you become distracted, your runner stops.\n\nYou are Player 1 racing against\n Player 2\n\n        Who will get farther?',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='orange', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "readySetGo"
readySetGoClock = core.Clock()
Player = visual.TextStim(win=win, ori=0, name='Player',
    text='nonsense',    font=u'Arial',
    pos=[0, .3], height=0.15, wrapWidth=None,
    color=u'orange', colorSpace=u'rgb', opacity=1,
    alignHoriz='center',depth=0.0)
readyText = visual.TextStim(win=win, ori=0, name='readyText',
    text=u"'Get Ready!'\r\n",    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'orange', colorSpace=u'rgb', opacity=1,
    alignHoriz='center',depth=-1.0)
getSetText = visual.TextStim(win=win, ori=0, name='getSetText',
    text=u"'Get Set!'",    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'orange', colorSpace=u'rgb', opacity=1,
    alignHoriz='center',depth=-2.0)
goText = visual.TextStim(win=win, ori=0, name='goText',
    text=u"'Go!'",    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'orange', colorSpace=u'rgb', opacity=1,
    alignHoriz='center',depth=-3.0)

# Initialize components for Routine "mindRun"
mindRunClock = core.Clock()

movie=[]
for i in range(0,NUM_PLAYERS):
    movie = movie+[visual.MovieStim(win=win, name='movie',
        filename=u'mindrun.mp4',
        ori=0, pos=[0, 0], opacity=1,
        depth=0.0,
    )]
    

movieScore = visual.TextStim(win=win, ori=0, name='movieScore',
    text='nonsense',    font=u'Arial',
    pos=[0, 0.6], height=0.1, wrapWidth=None,
    color=u'orange', colorSpace=u'rgb', opacity=1,
    alignHoriz='center',depth=0.0)

# Initialize components for Routine "score"
scoreClock = core.Clock()
playerScoreText = visual.TextStim(win=win, ori=0, name='playerScoreText',
    text='nonsense',    font=u'Arial',
    pos=[0, .2], height=0.1, wrapWidth=None,
    color=u'orange', colorSpace=u'rgb', opacity=1,
    depth=0.0)
player2ScoreText = visual.TextStim(win=win, ori=0, name='player2ScoreText',
    text='nonsense',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'orange', colorSpace=u'rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "finalScore"
finalScoreClock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text=u"'Final Score!'",    font=u'Arial',
    pos=[.4, 0], height=0.4, wrapWidth=None,
    color=u'orange', colorSpace=u'rgb', opacity=1,
    depth=0.0)
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text='nonsense',    font=u'Arial',
    pos=[.2, 0], height=0.1, wrapWidth=None,
    color=u'orange', colorSpace=u'rgb', opacity=1,
    depth=-1.0)
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text='nonsense',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'orange', colorSpace=u'rgb', opacity=1,
    depth=-2.0)
text_4 = visual.TextStim(win=win, ori=0, name='text_4',
    text='nonsense',    font=u'Arial',
    pos=[-.2, 0], height=0.1, wrapWidth=None,
    color=u'orange', colorSpace=u'rgb', opacity=1,
    depth=-3.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "Instructions"-------
t = 0
InstructionsClock.reset()  # clock 
frameN = -1
routineTimer.add(1000.000000)
# update component parameters for each repeat
instructionsFin = event.BuilderKeyResponse()  # create an object of type KeyResponse
instructionsFin.status = NOT_STARTED
# keep track of which components have finished
InstructionsComponents = []
InstructionsComponents.append(instructions)
InstructionsComponents.append(instructionsFin)
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Instructions"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = InstructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
        
    # *instructions* updates
    if t >= 0.0 and instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructions.tStart = t  # underestimates by a little under one frame
        instructions.frameNStart = frameN  # exact frame index
        instructions.setAutoDraw(True)
    elif instructions.status == STARTED and t >= (0.0 + 1000.0):
        instructions.setAutoDraw(False)
    
    # *instructionsFin* updates
    if t >= 0.0 and instructionsFin.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructionsFin.tStart = t  # underestimates by a little under one frame
        instructionsFin.frameNStart = frameN  # exact frame index
        instructionsFin.status = STARTED
        # keyboard checking is just starting
        instructionsFin.clock.reset()  # now t=0
        event.clearEvents()
    elif instructionsFin.status == STARTED and t >= (0.0 + 1000.0):
        instructionsFin.status = STOPPED
    if instructionsFin.status == STARTED:
        theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
        if len(theseKeys) > 0:  # at least one key was pressed
            instructionsFin.keys = theseKeys[-1]  # just the last key pressed
            instructionsFin.rt = instructionsFin.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
mindRunTrials = data.TrialHandler(nReps=3, method=u'sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions(u'mindrun.csv'),
    seed=None, name='mindRunTrials')
thisExp.addLoop(mindRunTrials)  # add the loop to the experiment
thisMindRunTrial = mindRunTrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisMindRunTrial.rgb)
if thisMindRunTrial != None:
    for paramName in thisMindRunTrial.keys():
        exec(paramName + '= thisMindRunTrial.' + paramName)

#-------Setup list to track frame count
movie_position=[0]*NUM_PLAYERS;
playerNdx=0;

if DETREND == 1:
    time_array=[]
    dist_array=[]

for thisMindRunTrial in mindRunTrials:
    currentLoop = mindRunTrials
    # abbreviate parameter names if possible (e.g. rgb = thisMindRunTrial.rgb)
    # CC I am pretty sure that this is where "player" et al. gets set
    if thisMindRunTrial != None:
        for paramName in thisMindRunTrial.keys():
            exec(paramName + '= thisMindRunTrial.' + paramName)
    
    #CC set our playerNdx
    playerNdx=int(player)-1
    if playerNdx >= NUM_PLAYERS:
        print('Player ndx %d exceeds length %d'%(playerNdx,NUM_PLAYERS))
    
    #CC start off by clearing the TCP buffer
    try:
        data = conn.recv(BUFFER_SIZE)
    except socket.error as ex:
        pass
    
    #------Prepare to start Routine "readySetGo"-------
    t = 0
    readySetGoClock.reset()  # clock 
    frameN = -1
    routineTimer.add(6.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    readySetGoComponents = []
    readySetGoComponents.append(Player)
    readySetGoComponents.append(readyText)
    readySetGoComponents.append(getSetText)
    readySetGoComponents.append(goText)
    for thisComponent in readySetGoComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    

    #-------Start Routine "readySetGo"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = readySetGoClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Player* updates
        if t >= 0.0 and Player.status == NOT_STARTED:
            # keep track of start time/frame for later
            Player.tStart = t  # underestimates by a little under one frame
            Player.frameNStart = frameN  # exact frame index
            Player.setAutoDraw(True)
        elif Player.status == STARTED and t >= (0.0 + 4.0):
            Player.setAutoDraw(False)
        if Player.status == STARTED:  # only update if being drawn
            Player.setText('Player %s'%(player), log=False)
        
        # *readyText* updates
        if t >= 1.0 and readyText.status == NOT_STARTED:
            # keep track of start time/frame for later
            readyText.tStart = t  # underestimates by a little under one frame
            readyText.frameNStart = frameN  # exact frame index
            readyText.setAutoDraw(True)
        elif readyText.status == STARTED and t >= (1.0 + 1.0):
            readyText.setAutoDraw(False)
        
        # *getSetText* updates
        if t >= 2.0 and getSetText.status == NOT_STARTED:
            # keep track of start time/frame for later
            getSetText.tStart = t  # underestimates by a little under one frame
            getSetText.frameNStart = frameN  # exact frame index
            getSetText.setAutoDraw(True)
        elif getSetText.status == STARTED and t >= (2.0 + 1.0):
            getSetText.setAutoDraw(False)
        
        # *goText* updates
        if t >= 3.0 and goText.status == NOT_STARTED:
            # keep track of start time/frame for later
            goText.tStart = t  # underestimates by a little under one frame
            goText.frameNStart = frameN  # exact frame index
            goText.setAutoDraw(True)
        elif goText.status == STARTED and t >= (3.0 + 1.0):
            goText.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in readySetGoComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "readySetGo"-------
    for thisComponent in readySetGoComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #------Prepare to start Routine "mindRun"-------
    t = 0
    
    # CC reset score to 0 between blocks
    
    score=float(0.0)
    MOVIE_PAUSED=False
    
    mindRunClock.reset()  # clock 
    frameN = -1
    routineTimer.add(60.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    mindRunComponents = []
    mindRunComponents.append(movie[playerNdx])
    mindRunComponents.append(movieScore)
        
    for thisComponent in mindRunComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "mindRun"-------
    continueRoutine = True
    
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = mindRunClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        #--- TCPIP RECV 
        # check the network interface for new data
        data=[]
        try:
            data = conn.recv(BUFFER_SIZE)
        except socket.error as ex:
            pass
            
        if data:
            print('received %s\n'%(data))
            try:
                tcp_dist=float(data.split('\n')[0]);
            except:
                tcp_dist=0.0;
            print('converted to %f\n'%(tcp_dist))
         
            if DETREND == 1:
                time_array=time_array+[t]
                dist_array=dist_array+[tcp_dist]
                dist_detrend = detrendDist(time_array, dist_array)
            else:
                dist_detrend = tcp_dist
         #--- TCPIP RECV
         
        if playerNdx ==  1:
            dist_detrend=np.random.normal(0,3.0, 1)
            
        if SUM == 1:
            score=score+dist_detrend
        else:
            score=dist_detrend
        
        # *movie* updates
        if t >= 0.0 and movie[playerNdx].status == NOT_STARTED:
            # keep track of start time/frame for later
            movie[playerNdx].tStart = t  # underestimates by a little under one frame
            movie[playerNdx].frameNStart = frameN  # exact frame index
            movie[playerNdx].setAutoDraw(True)
            movieScore.setAutoDraw(True)
        elif t < (0.0 + 60.0):
            movieScore.setText('Player %s: %3.0f'%(player,np.ceil(1000*movie[playerNdx]._player.time)), log=False)
            print('Player %s: %f (%f,%f)::%3.0f'%(player,score,dist_detrend,tcp_dist,np.ceil(1000*movie[playerNdx]._player.time)))
            
            if movie[playerNdx].status == STARTED:
                if score < 0.0:
                    movie[playerNdx].pause()
            elif movie[playerNdx].status == PAUSED: 
                if score>=0.0:
                    movie[playerNdx].play()
                
        elif t >= (0.0 + 60.0):
            movie_position[playerNdx]=np.ceil(1000*movie[playerNdx]._player.time)
            if movie[playerNdx].status == STARTED:
                movie[playerNdx].pause()
            movieScore.setAutoDraw(False)
            movie[playerNdx].setAutoDraw(False)
            
        if movie[playerNdx].status == FINISHED:  # force-end the routine
            continueRoutine = False
            
            
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mindRunComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "mindRun"-------
    for thisComponent in mindRunComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #------Prepare to start Routine "score"-------
    t = 0
    scoreClock.reset()  # clock 
    frameN = -1
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    scoreComponents = []
    scoreComponents.append(playerScoreText)
    scoreComponents.append(player2ScoreText)
    for thisComponent in scoreComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "score"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = scoreClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *playerScoreText* updates
        if t >= 0.0 and playerScoreText.status == NOT_STARTED:
            # keep track of start time/frame for later
            playerScoreText.tStart = t  # underestimates by a little under one frame
            playerScoreText.frameNStart = frameN  # exact frame index
            playerScoreText.setAutoDraw(True)
        elif playerScoreText.status == STARTED and t >= (0.0 + 5.0):
            playerScoreText.setAutoDraw(False)
        if playerScoreText.status == STARTED:  # only update if being drawn
            playerScoreText.setText('Player 1 Score %3.0f'%(movie_position[0]), log=False)
        
        # *player2ScoreText* updates
        if t >= 0.0 and player2ScoreText.status == NOT_STARTED:
            # keep track of start time/frame for later
            player2ScoreText.tStart = t  # underestimates by a little under one frame
            player2ScoreText.frameNStart = frameN  # exact frame index
            player2ScoreText.setAutoDraw(True)
        elif player2ScoreText.status == STARTED and t >= (0.0 + 5.0):
            player2ScoreText.setAutoDraw(False)
        if player2ScoreText.status == STARTED:  # only update if being drawn
            player2ScoreText.setText('Player 2 Score %3.0f'%(movie_position[1]), log=False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in scoreComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "score"-------
    for thisComponent in scoreComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 5 repeats of 'mindRunTrials'


#------Prepare to start Routine "finalScore"-------
t = 0
finalScoreClock.reset()  # clock 
frameN = -1
routineTimer.add(6.000000)
# update component parameters for each repeat
# keep track of which components have finished
finalScoreComponents = []
finalScoreComponents.append(text)
finalScoreComponents.append(text_2)
finalScoreComponents.append(text_3)
finalScoreComponents.append(text_4)
for thisComponent in finalScoreComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "finalScore"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = finalScoreClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t  # underestimates by a little under one frame
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    elif text.status == STARTED and t >= (0.0 + 6.0):
        text.setAutoDraw(False)
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t  # underestimates by a little under one frame
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    elif text_2.status == STARTED and t >= (0.0 + 6.0):
        text_2.setAutoDraw(False)
    if text_2.status == STARTED:  # only update if being drawn
        text_2.setText('Player 1 %s'%(player), log=False)
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t  # underestimates by a little under one frame
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    elif text_3.status == STARTED and t >= (0.0 + 6.0):
        text_3.setAutoDraw(False)
    if text_3.status == STARTED:  # only update if being drawn
        text_3.setText('Player 2 %s'%(player), log=False)
    
    # *text_4* updates
    if t >= 0.0 and text_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_4.tStart = t  # underestimates by a little under one frame
        text_4.frameNStart = frameN  # exact frame index
        text_4.setAutoDraw(True)
    elif text_4.status == STARTED and t >= (0.0 + 6.0):
        text_4.setAutoDraw(False)
    if text_4.status == STARTED:  # only update if being drawn
        text_4.setText('Player s Wins!'%(player), log=False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in finalScoreComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "finalScore"-------
for thisComponent in finalScoreComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
        
#--- TCPIP RECV
#end, lets kill the connection and the socket
conn.close()
s.close()
#--- TCPIP RECV

win.close()
core.quit()
