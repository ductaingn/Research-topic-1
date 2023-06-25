import Env_create as env
import numpy as np

#Number of APs
NUM_OF_AP = 9
#Number of Users
NUM_OF_USER = 10
#Number of Applications per User
NUM_OF_APP = 2
#Rate Requirement
R1=6 #Mbps
R2=3 #Mbps
#Mean Packet Arrival Rate
MPAR=0.1 #Mbps
#Learning rate alpha, discount factor beta, decay factor lambda, greedy policy factor epsilon
ALPHA=0.8
BETA=0.9
LAMBDA=0.995
EPSILON=1



#PLOT DATA POINTS

#CREATE STATE MATRIXES
#State is a NUM_OF_USER*NUM_OF_APP matrix where state[user_index,app_index]=serving_ap_index
def initialize_state_matrix():
    state = np.matrix(np.zeros(shape=(NUM_OF_USER,NUM_OF_APP)))
    return state

#CREATE REWARD 
#Return a reward array of each user
def reward(state,action,achivable_rate):
    reward=np.array(np.zeros)
    for k in range (NUM_OF_USER):
        c1=0
        c2=0
        for f in range (NUM_OF_APP):
            if(not(check_overload(action,state,achivable_rate[state[k,f],k])[f]==1)):
                c1+=action[k,f]*achivable_rate[state[k,f],k]
            # else:
            #     c2+=
        reward[k]=0.8*c1-0.2*c2
    return reward


#CREATE MODEL
#Action is a NUM_OF_USER*NUM_OF_APP matrix where state[user_index,app_index]=request_ap_index
def chose_action():
    action=np.matrix(np.zeros(shape=(NUM_OF_USER,NUM_OF_APP)))
    random_factor=np.random()
    if(random_factor<EPSILON):
        for k in range (NUM_OF_USER):
            for f in range (NUM_OF_APP):
                action[k,f]=np.random.randint(1,NUM_OF_AP)
    # else: Chose best action
        
    return action

#Return a matrix of achivable rate between each user k and each AP b
def achivable_rate(h):
    r=np.matrix(np.zeros(shape=(NUM_OF_AP,NUM_OF_USER)))
    for b in range (NUM_OF_AP):
        for k in range (NUM_OF_USER):
            r[b,k]=env.r(h,b,k)
    return r

#Return a array of each AP's load
def AP_load(state,achivable_rate):
    load=np.array(np.zeros)
    for k in range (NUM_OF_USER) :
        for f in range (NUM_OF_APP): 
            load[state[k,f]]+=MPAR/achivable_rate[state[k,f],k]
    return load

#Return a array of app dropped per user
#If Appilcation k requires a AP that will be overloaded if it serve app k then overload[k]=1
def check_overload(action,state,achivable_rate_bk):
    overload=np.array()
    load=AP_load(state)
    for k in range (NUM_OF_APP):
        load_for_serving=MPAR/achivable_rate_bk
        if(action[k]==1 and load[k]+load_for_serving>1):
            overload[k]=1
        else: 
            overload[k]=0
    return overload

def initialize_Q():
    Q = np.matrix(np.zeros(shape=(NUM_OF_AP,NUM_OF_APP)))
    return Q
def update_Q(state,action,gamma):
    return

#TRAINING
    #Read from old Q-table
    #Train with new data
users_positions=env.initialize_users_pos()
aps_positions=env.initialize_aps_pos()
state=initialize_state_matrix()
    #Write results to data files