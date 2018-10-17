#add parent dir to find package. Only needed for source code build, pip install doesn't need it.
import os, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(os.path.dirname(currentdir))
os.sys.path.insert(0,parentdir)
from pybullet_envs.bullet.kukaGymEnvReach import KukaGymEnvReach as KukaGymEnv
import time

from numpy import array
import numpy as np
from copy import deepcopy as copy


from pdb import set_trace
np.set_printoptions(precision=3)

def main():
	env = KukaGymEnv(renders=True,isDiscrete=False, maxSteps = 10000000)
		
	  
	motorsIds=[]
	#motorsIds.append(env._p.addUserDebugParameter("posX",0.4,0.75,0.537))
	#motorsIds.append(env._p.addUserDebugParameter("posY",-.22,.3,0.0))
	#motorsIds.append(env._p.addUserDebugParameter("posZ",0.1,1,0.2))
	#motorsIds.append(env._p.addUserDebugParameter("yaw",-3.14,3.14,0))
	#motorsIds.append(env._p.addUserDebugParameter("fingerAngle",0,0.3,.3))
	
	dv = 0.00
	# motorsIds.append(env._p.addUserDebugParameter("posX",-dv,dv,0))
	# motorsIds.append(env._p.addUserDebugParameter("posY",-dv,dv,0))
	# motorsIds.append(env._p.addUserDebugParameter("posZ",-dv,dv,0))
	# motorsIds.append(env._p.addUserDebugParameter("yaw",-dv,dv,0))
	# motorsIds.append(env._p.addUserDebugParameter("fingerAngle",0,0.3,.3))
	for n in range(10):
		done = False
		start = np.random.rand(3)*0.1 + array([0.6,0.1,0.4])
		goal = np.random.rand(3)*0.1 + array([0.6,0.1,0.4])
		state = env._reset_positions([0.6,0.1,0.4	])     #default [-0.100000,0.000000,0.070000]
		action = (goal - state[:3])*0.001
		eps = 0.01
		action = action.tolist()
		action += [0,0]
		print('diff goal - start: {}'.format(goal - state[:3]))
		print('start state: {}, goal state: {}'.format(state[:3], goal))
		print('normed action: {}'.format((state[:3]- goal)/np.linalg.norm(state[:3]- goal)))
		ii = 0
		while (not done):
			true_state = env._get_link_state()
			# print(state)
			state_old = copy(state)
			state, reward, done, info = env.step2(action)
			obs = env.getExtendedObservation()
			if ii % 100 == 0:
				print(state[:3])
				print('normed executed action: {}'.format((state[:3] - state_old[:3])/np.linalg.norm(state[:3] - state_old[:3])))

			ii += 1
		set_trace()

if __name__=="__main__":
    main()
