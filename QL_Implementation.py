import Env_create as env
import numpy as np

#Number of APs
NUM_OF_AP = 9
#Number of Users
NUM_OF_USER = 10
#Number of Applications per User
NUM_OF_APP = 2
#Rate Requirement
R=(6,3) #Mbps
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
def reward(action,load,achivable_rate):
    reward=np.array(np.zeros(NUM_OF_USER))
    for k in range (NUM_OF_USER):
        c1=0
        c2=0
        for f in range (NUM_OF_APP):
            AP_request_index=state[k,f]
            if((not(check_drop(action[k,f],load,achivable_rate[AP_request_index,k])[f])) and achivable_rate[AP_request_index,k]>= R[f]):
                c1+=achivable_rate[AP_request_index,k]
            # else:
            #     c2-=
        reward[k]=0.8*c1+0.2*c2
    return reward


#CREATE MODEL
#Action is a NUM_OF_USER*NUM_OF_APP matrix where state[user_index,app_index]=request_ap_index
#Code lại phần epsilon random dựa trên user không phải application
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
    load=np.array(np.zeros(NUM_OF_APP))
    for k in range (NUM_OF_USER) :
        for f in range (NUM_OF_APP): 
            load[state[k,f]]+=MPAR/achivable_rate[state[k,f],k]
    return load

#Return a array of app dropped per user
#If Appilcation k requires a AP that will be overloaded if it serve app k then drop[k]=True
#action_of_user is a row in action matrix 
#load is the array of each AP's load
#achivable_rate_bk is the value of achivable_rate[b,k]
def check_drop(action_of_user,load,achivable_rate_bk):
    drop=np.array(2)
    for k in range (NUM_OF_APP):
        load_for_serving=MPAR/achivable_rate_bk
        if(load[action_of_user[k]]+load_for_serving>1):
            drop[k]=True
        else:
            drop[k]=False
    return drop

#Map state or action with a real number 
def state_action_to_Q_index(state_of_user,action_of_user):
    state_index=0
    for i in range (NUM_OF_APP):
        state_index+=state[i]*pow(NUM_OF_AP,i)

    action_index=0
    for i in range (NUM_OF_APP):
        action_index+=state[i]*pow(NUM_OF_AP,i)
    index=(state_index,action_index)
    return index

def Q_index_to_state_action(index):
    state_index=index[1]
    state=np.array
    for i in range(NUM_OF_AP):
        state_index

#Initialize Q
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