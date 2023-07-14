import Env_create as env
import numpy as np

#Number of APs
NUM_OF_AP = 9
#Number of Users
NUM_OF_USER = 10
#Number of Applications per User
NUM_OF_APP = 2
#Rate Requirement
R = [6 , 3] #Mbps 
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
#state, action, achivable_rate là toàn bộ các state, action, achivalbe rate của user
#môi trường sẽ tính toán reward này và trả về cho các user nhận lấy reward tại
#vị trí cần tìm trong mảng reward
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
#mảng action cuối cùng, được trả về sau khi tất cả các user nhận chọn được action
#truyền vào hàm bảng Q_table và state
#Bảng Q_table gồm 2 chiều state - action đã được convert sang chỉ số int
#truy cập vào bảng Q_table bằng chỉ số Q_table[state, action]
#state là mảng 2 chiều có dạng user - [applications]

def chose_action(state, Q_table):
    action=np.matrix(np.zeros(shape=(NUM_OF_USER,NUM_OF_APP)))
    random_factor=np.random()
    if(random_factor<EPSILON):
        for k in range (NUM_OF_USER):
            for f in range (NUM_OF_APP):
                action[k,f]=np.random.randint(0,NUM_OF_AP - 1)     #chỉ số của ap chạy từ 0 -> NUM_OF_AP-1
    # else: Chose best action    
    else:
        #duyệt qua tất cả các user
        for k in range (NUM_OF_USER):
            max_index = -9999999999
            max_Q_value = -99999999999
            current_state = state[k]
            current_state_index = convert_to_index[current_state]
            being_checked_action_index = 0;
            expected_action = np.matrix(np.zeros(shape=(1, NUM_OF_APP)))
            # 2 vòng lặp để duyệt tất cả các action có thể chọn
            for f in range (NUM_OF_APP):
                for b in range (NUM_OF_AP):
                    expected_action[f] = b
                    being_checked_action_index = convert_to_index(expected_action)
                    # kiểm tra giá trị trong bảng Q_table
                    if Q_table[being_checked_action_index, being_checked_action_index] > max_Q_value :
                        max_index = being_checked_action_index
                        #giá trị chỉ số state(t+1) = chỉ số action(t) do nếu action t được thực hiện
                        # thì state(t+1) chính là action(t)
                        # app request tới ap nào thì giá trị tại state mới chính bằng ap đó 
                        max_Q_value = Q_table[being_checked_action_index, being_checked_action_index]
            #kết thúc vòng lặp có được chỉ số của action có giá trị Q lớn nhất
            expected_action = convert_from_index(being_checked_action_index)
            for f in range (NUM_OF_APP) :
                action[k, f] = expected_action[f]
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

#Initialize Q
def initialize_Q():
    Q = np.matrix(np.zeros(shape=(NUM_OF_AP,NUM_OF_APP)))
    return Q
def update_Q(state,action,gamma):
    return


#TRAINING
    #Read from old Q-table
    #Train with new data
# users_positions=env.initialize_users_pos()
# aps_positions=env.initialize_aps_pos()
# state=initialize_state_matrix()



    #Write results to data files





#Get index of user's state in Q table
#state là 1 mảng gồm num_of_applications phần tử, mỗi phần tử chứa giá trị index của access point
def convert_to_index (state):
    num = 0;
    for i in range(len(state)):
        num += pow(NUM_OF_AP, i) * state[i]
    return num

def convert_from_index (i):
    state = []
    k = 0
    while (k < NUM_OF_APP):
        state.append(i % NUM_OF_AP)
        i = int(i / NUM_OF_AP)
        k += 1
    state.reverse()
    return state

# state = list(map(int, input("Nhap list: ").split(" ")))
# print(state)
# i = int(input())
# state = convert_from_index(i)
# print(state)