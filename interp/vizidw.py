import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import lfmViz as lfmv
from matplotlib.colors import LogNorm
import matplotlib.gridspec as gridspec

lfmv.ppInit()
figSize = (16,8)

idScls = [3,4,5,6]
NumID = len(idScls)
figQ = 300

PBs = []

for i in idScls:
	fIn = "idw%d.vti"%(i)
	print("Reading %s"%(fIn))
	Bx,By,Bz = lfmv.getVTI_Slc(fIn)
	ori,dx,extent = lfmv.getVTI_Eq(fIn)
	PBi = np.sqrt(Bx**2.0 + By**2.0 + Bz**2.0)
	PBs.append(PBi)

#Create grid
x = ori[0] + dx[0]*np.arange(extent[0],extent[1]+1)
y = ori[1] + dx[1]*np.arange(extent[2],extent[3]+1)

vNorm = LogNorm(vmin=1.0,vmax=1.0e+3)
cMap = "viridis"
WRs = 10*np.ones(NumID+2)
WRs[-1] = 0.25
WRs[-2] = 0.1

fig = plt.figure(figsize=figSize)
gs = gridspec.GridSpec(1,NumID+2,width_ratios=WRs)

for i in range(NumID):
	Ax = fig.add_subplot(gs[0,i])
	Ax.pcolormesh(x,y,PBs[i].T,norm=vNorm,cmap=cMap)
	plt.axis('scaled')
	plt.xlim([-15,12.75])
	plt.ylim([-20,20])	
	plt.title("IDW = %d"%(idScls[i]))
AxC = fig.add_subplot(gs[0,-1])
cb = mpl.colorbar.ColorbarBase(AxC,cmap=cMap,norm=vNorm,orientation='vertical')
cb.set_label("Log(Pb)")
figName = "idwPic.png"
plt.savefig(figName,dpi=figQ)
lfmv.trimFig(figName)

