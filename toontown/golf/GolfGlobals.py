from direct.directnotify import DirectNotifyGlobal;import random;MAX_PLAYERS_PER_HOLE=4;GOLF_BALL_RADIUS=0.25;GOLF_BALL_VOLUME=4.0/3.0*3.14159*GOLF_BALL_RADIUS**3;GOLF_BALL_MASS=0.5;GOLF_BALL_DENSITY=GOLF_BALL_MASS/GOLF_BALL_VOLUME;GRASS_SURFACE=0;BALL_SURFACE=1;HARD_SURFACE=2;HOLE_SURFACE=3;SLICK_SURFACE=4;OOB_RAY_COLLIDE_ID=-1;GRASS_COLLIDE_ID=2;HARD_COLLIDE_ID=3;TOON_RAY_COLLIDE_ID=4;MOVER_COLLIDE_ID=7;WINDMILL_BASE_COLLIDE_ID=8;CAMERA_RAY_COLLIDE_ID=10;BALL_COLLIDE_ID=42;HOLE_CUP_COLLIDE_ID=64;SKY_RAY_COLLIDE_ID=78;SLICK_COLLIDE_ID=13;BALL_CONTACT_FRAME=9;BALL_CONTACT_TIME=(BALL_CONTACT_FRAME+1)/24.0;AIM_DURATION=60;TEE_DURATION=15;RANDOM_HOLES=True;KICKOUT_SWINGS=2;TIME_TIE_BREAKER=True;CourseInfo={0:{'holeIds':(2,3,4,5,6,7,8,12,13,15,16),'numHoles':3,'name':''},1:{'holeIds':((0,5),(1,5),2,3,4,5,6,7,8,9,10,(11,5),12,13,(14,5),15,16,(17,5),(20,5),(21,5),(22,5),(23,5),(24,5),(25,5),(26,5),(28,5),(30,5),(31,5),(33,5),(34,5)),'numHoles':6,'name':''},2:{'holeIds':((1,5),4,5,6,7,8,9,10,11,12,13,(14,5),15,(17,5),(18,20),(19,20),(20,20),(21,5),(22,5),(23,20),(24,20),(25,20),(26,20),(27,20),(28,20),(29,20),(30,5),(31,20),(32,20),(33,5),(34,20),(35,20)),'numHoles':9,'name':''}};HoleInfo={0:{'optionalMovers':(),'maxSwing':6,'terrainModel':'phase_6/models/golf/hole18.bam','name':'','blockers':(),'par':3,'physicsData':'golfGreen18'},1:{'maxSwing':6,'terrainModel':'phase_6/models/golf/hole1.bam','name':'','blockers':(),'par':3,'physicsData':'golfGreen1'},2:{'maxSwing':6,'terrainModel':'phase_6/models/golf/hole2.bam','name':'','blockers':(),'par':3,'physicsData':'golfGreen2'},3:{'maxSwing':6,'terrainModel':'phase_6/models/golf/hole3.bam','name':'','blockers':(),'par':2,'physicsData':'golfGreen3'},4:{'maxSwing':6,'terrainModel':'phase_6/models/golf/hole4.bam','name':'','blockers':(),'par':3,'physicsData':'golfGreen4'},5:{'maxSwing':6,'terrainModel':'phase_6/models/golf/hole5.bam','name':'','blockers':(),'par':3,'physicsData':'golfGreen2'},6:{'maxSwing':6,'terrainModel':'phase_6/models/golf/hole6.bam','name':'','blockers':(),'par':3,'physicsData':'golfGreen6'},7:{'maxSwing':6,'terrainModel':'phase_6/models/golf/hole7.bam','name':'','blockers':(),'par':3,'physicsData':'golfGreen7'},8:{'maxSwing':6,'terrainModel':'phase_6/models/golf/hole8.bam','name':'','blockers':(),'par':3,'physicsData':'golfGreen8'},9:{'maxSwing':6,'terrainModel':'phase_6/models/golf/hole9.bam','name':'','blockers':2,'par':3,'physicsData':'golfGreen9'},10:{'maxSwing':6,'terrainModel':'phase_6/models/golf/hole10.bam','name':'','blockers':(),'par':3,'physicsData':'golfGreen10'},11:{'maxSwing':6,'terrainModel':'phase_6/models/golf/hole11.bam','name':'','blockers':(),'par':3,'physicsData':'golfGreen11'},12:{'maxSwing':6,'terrainModel':'phase_6/models/golf/hole12.bam','name':'','blockers':(),'par':3,'physicsData':'golfGreen12'},13:{'maxSwing':6,'terrainModel':'phase_6/models/golf/hole13.bam','name':'','blockers':(),'par':3,'physicsData':'golfGreen13'},14:{'maxSwing':6,'terrainModel':'phase_6/models/golf/hole14.bam','name':'','blockers':(),'par':3,'physicsData':'golfGreen14'},15:{'maxSwing':6,'terrainModel':'phase_6/models/golf/hole15.bam','name':'','blockers':(),'par':3,'physicsData':'golfGreen15'},16:{'maxSwing':6,'terrainModel':'phase_6/models/golf/hole16.bam','name':'','blockers':(),'par':3,'physicsData':'golfGreen16'},17:{'maxSwing':6,'terrainModel':'phase_6/models/golf/hole17.bam','name':'','blockers':(),'par':3,'physicsData':'golfGreen17'},18:{'optionalMovers':1,'maxSwing':6,'terrainModel':'phase_6/models/golf/hole18.bam','name':'','blockers':(1,2),'par':3,'physicsData':'golfGreen18'},19:{'maxSwing':6,'terrainModel':'phase_6/models/golf/hole1.bam','name':'','blockers':(2,5),'par':3,'physicsData':'golfGreen1'},20:{'maxSwing':6,'terrainModel':'phase_6/models/golf/hole2.bam','name':'','blockers':(1,3),'par':3,'physicsData':'golfGreen2'},21:{'maxSwing':6,'terrainModel':'phase_6/models/golf/hole3.bam','name':'','blockers':(1,2,3),'par':3,'physicsData':'golfGreen3'},22:{'maxSwing':6,'terrainModel':'phase_6/models/golf/hole4.bam','name':'','blockers':2,'par':3,'physicsData':'golfGreen4'},23:{'optionalMovers':1,'maxSwing':6,'terrainModel':'phase_6/models/golf/hole5.bam','name':'','blockers':(3,4),'par':3,'physicsData':'golfGreen5'},24:{'optionalMovers':1,'maxSwing':6,'terrainModel':'phase_6/models/golf/hole6.bam','name':'','blockers':1,'par':3,'physicsData':'golfGreen6'},25:{'optionalMovers':1,'maxSwing':6,'terrainModel':'phase_6/models/golf/hole7.bam','name':'','blockers':3,'par':3,'physicsData':'golfGreen7'},26:{'optionalMovers':1,'maxSwing':6,'terrainModel':'phase_6/models/golf/hole8.bam','name':'','blockers':(),'par':3,'physicsData':'golfGreen8'},27:{'optionalMovers':(1,2),'maxSwing':6,'terrainModel':'phase_6/models/golf/hole9.bam','name':'','blockers':(),'par':3,'physicsData':'golfGreen9'},28:{'optionalMovers':(1,2),'maxSwing':6,'terrainModel':'phase_6/models/golf/hole10.bam','name':'','blockers':(),'par':3,'physicsData':'golfGreen10'},29:{'optionalMovers':1,'maxSwing':6,'terrainModel':'phase_6/models/golf/hole11.bam','name':'','blockers':(),'par':3,'physicsData':'golfGreen11'},30:{'maxSwing':6,'terrainModel':'phase_6/models/golf/hole12.bam','name':'','blockers':(1,2,3),'par':3,'physicsData':'golfGreen12'},31:{'optionalMovers':1,'maxSwing':7,'terrainModel':'phase_6/models/golf/hole13.bam','name':'','blockers':(3,4),'par':4,'physicsData':'golfGreen13'},32:{'optionalMovers':1,'maxSwing':6,'terrainModel':'phase_6/models/golf/hole14.bam','name':'','blockers':1,'par':3,'physicsData':'golfGreen14'},33:{'optionalMovers':(1,2),'maxSwing':6,'terrainModel':'phase_6/models/golf/hole15.bam','name':'','blockers':(1,2,3),'par':3,'physicsData':'golfGreen15'},34:{'optionalMovers':1,'maxSwing':6,'terrainModel':'phase_6/models/golf/hole16.bam','name':'','blockers':(1,2,5,6),'par':3,'physicsData':'golfGreen16'},35:{'maxSwing':7,'terrainModel':'phase_6/models/golf/hole17.bam','name':'','blockers':(3,4,5),'par':4,'physicsData':'golfGreen17'}}
for hi in HoleInfo:
    if type(HoleInfo[hi]['blockers'])==type(0):blockerNum=HoleInfo[hi]['blockers'];HoleInfo[hi]['blockers']=(blockerNum,)
    if 'optionalMovers' in HoleInfo[hi] and type(HoleInfo[hi]['optionalMovers'])==type(0):blockerNum=HoleInfo[hi]['optionalMovers'];HoleInfo[hi]['optionalMovers']=(blockerNum,)
DistanceToBeInHole=0.75;CoursesCompleted=0;CoursesUnderPar=1;HoleInOneShots=2;EagleOrBetterShots=3;BirdieOrBetterShots=4;ParOrBetterShots=5;MultiPlayerCoursesCompleted=6;CourseZeroWins=7;CourseOneWins=8;CourseTwoWins=9;TwoPlayerWins=10;ThreePlayerWins=11;FourPlayerWins=12;MaxHistoryIndex=9;NumHistory=MaxHistoryIndex+1;CalcOtherHoleBest = False;CalcOtherCourseBest = False;TrophyRequirements={CoursesCompleted:(4,40,400),CoursesUnderPar:(1,10,100),HoleInOneShots:(1,10,100),EagleOrBetterShots:(2,20,200),BirdieOrBetterShots:(3,30,300),ParOrBetterShots:(4,40,400),MultiPlayerCoursesCompleted:(6,60,600),CourseZeroWins:(1,10,100),CourseOneWins:(1,10,100),CourseTwoWins:(1,10,100)};PlayerColors=[(0.925,0.168,0.168,1),(0.13,0.59,0.973,1),(0.973,0.809,0.129,1),(0.598,0.402,0.875,1)];KartColors=[[[0,50],[90,255],[0,85]],[[160,255],[-15,15],[0,120]],[[160,255],[0,110],[0,110]]];NumTrophies=0
for key in TrophyRequirements:NumTrophies += len(TrophyRequirements[key])
NumCups=3;TrophiesPerCup=NumTrophies/NumCups
def calcTrophyListFromHistory(h):
    rv,hi=[],0
    for ti in xrange(NumHistory):
        r=TrophyRequirements[ti]
        for an in r:
            if h[hi]>=an:rv.append(True)
            else:rv.append(False)
        hi+=1
    return rv
def calcCupListFromHistory(h):
    rv,tl,nt=[False]*NumCups,calcTrophyListFromHistory(h),0
    for gt in tl:
        if gt:nt+=1
    for ci in xrange(len(rv)):
        tr=(ci+1)*TrophiesPerCup
        if tr<=nt:rv[ci]=True
    return rv
def getCourseName(ci):
    from toontown.toonbase import TTLocalizer
    if ci in CourseInfo:
        if not CourseInfo[ci]['name']:CourseInfo[ci]['name']=TTLocalizer.GolfCourseNames[ci]
        return CourseInfo[ci]['name']
    else:return ''
def getHoleName(hi):
    from toontown.toonbase import TTLocalizer
    if hi in HoleInfo:
        if not HoleInfo[hi]['name']:HoleInfo[hi]['name']=TTLocalizer.GolfHoleNames[hi]
        return HoleInfo[hi]['name']
    else:return ''
def getHistoryIndexForTrophy(ti):
    rv,db=-1,int(ti/3)
    if db<NumHistory:rv=db
    return rv
def packGolfHoleBest(hb):
    rv,sl=[],False
    for h in hb:
        h&=15
        if sl:rv[-1]|=h<<4;sl=False
        else:rv.append(h);sl=True
    return rv
def unpackGolfHoleBest(phb):
    rv=[]
    for ph in phb:lb=ph&15;rv.append(lb);hb=(ph & 240)>>4;rv.append(hb)
    return rv
