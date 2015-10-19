"""example script for profiling a beam; starts with a preview and will measure 100 times, roughly 3 seconds per measurement"""

import MT_g2d as g2d
from beam_profiler_XP import BeamProfiler as bp
from matplotlib import pylab as pylab
import numpy as np

beamProfiler=bp()

for i in range (0,1):
	"""Preview, and take image"""
	beamProfiler.take_image_preview()

	'''Find max'''
	max_img = np.amax(beamProfiler.image_raw)
	print max_img

	"""Fit image data to Gaussian"""
	Gauss2D = g2d.Gaussian2D(beamProfiler.array)

	"""Print widths of fit"""
	print 'w_a = ', Gauss2D._w_a_len, 'mm'
	print 'w_b = ', Gauss2D._w_b_len, 'mm'

	i = i+1
