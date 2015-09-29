# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 10:18:04 2014

@author: halley
"""
import functionalhelpers as fh
import music21helpers as mh
from music21 import *
import scale as sc
from constants import *
import rhythms as rhy
import pitchhelpers as pth

#Etude 1: up and down the scale
durs = fh.concat([[0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,1.0] for i in range(0,8)])
degs = fh.concat([map(lambda j: j + i, [0,1,2,3,4,3,2,1,0]) for i in range(0,8)])

score = mh.listsDegreesToPart(degs, durs)
score.insert(0, meter.TimeSignature('5/4'))
#score.show('musicxml')


#Etude 2: up and down different scales
durs = fh.concat([[0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,1.0] for i in range(0,8)])
degs = fh.concat([sc.degreesToNotes([0,1,2,3,4,3,2,1,0], scale = map(lambda j: j + i, scales["major"])) for i in scales["major"] + [12]])
score = mh.listsToPart(degs, durs)
score.insert(0, meter.TimeSignature('5/4'))
#score.show('musicxml')

#Etude 3: up and down scale with intervals of 2
degs = fh.concat([[j, j + 2] for j in range(0,7)])
degs.append(7)
degs.extend(fh.concat([[j, j - 2] for j in range(7,0,-1)]))
degs.append(0)
durs = [1 for i in range(0, 14)] + [2] + [1 for i in range(0, 14)] + [2]
score = mh.listsDegreesToPart(degs, durs)
#score.show('musicxml')

#Etude 4: up and down the scale with intervals of 2, plus a random walk in the middle of each measure
degs = []
durs = fh.concat([1, 0.5, 0.5, 0.5, 0.5, 1] for i in range(0,7)) + [3,1] + fh.concat([1, 0.5, 0.5, 0.5, 0.5, 1] for i in range(0,7)) + [2]
for i in range(0,7):
    degs.extend(pth.randomWalkBeginningEndDegrees(i, i+2, len(tmp_dur)))
degs.extend([7,7])
for i in range(7,0,-1):
    degs.extend(pth.randomWalkBeginningEndDegrees(i, i-2, len(tmp_dur)))
score = mh.listsDegreesToPart(degs, durs)
#score.show('musicxml')