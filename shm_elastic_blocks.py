import matplotlib.pyplot as plt

A_0 = 5
k_1 = 2
k_2 = 1
m_1 = 2
m_2 = 1
dist = 3

time = 0
sim_time = 100
dt = 0.001

state = [A_0, 0, 0, 0, None, None, None] # x_1, x_2, v_1, v_2, a_1, a_2, col_data

li_time = [0]
li_pos_1 = [A_0]
li_pos_2 = [0]

def new(state):
    
    # acceleration
    state[4] = -(k_1*state[0])/m_1
    state[5] = -(k_2*state[1])/m_2
    
    # velocity (dv = a*dt)
    state[2] += state[4]*dt
    state[3] += state[5]*dt
    
    # position (dx = v*dt)
    state[0] += state[2]*dt
    state[1] += state[3]*dt
    
    # collision check + monitoring
    if state[2] >= 0:
        sign_1 = "p"
    else:
        sign_1 = "n"
        
    if state[3] >= 0:
        sign_2 = "p"
    else:
        sign_2 = "n"
    
    # check that collision did not occur in "recent" times
    if state[6] == None or state[6][0] == "NO" or (state[6][0] == "YES" and (state[6][1] != sign_1 or state[6][2] != sign_2)):
        if abs(state[1] - state[0] - dist) < 0.01:
            state[6] = ["YES", sign_1, sign_2]
            v_1 = state[2]
            v_2 = state[3]
            state[2] = (2*m_2*v_2 + v_1*(m_1 - m_2))/(m_1 + m_2)
            state[3] = (2*m_1*v_1 + v_2*(m_2 - m_1))/(m_1 + m_2)
    return state
    
while time < sim_time:
    time += dt
    li_time.append(time)
    state = new(state)
    li_pos_1.append(state[0])
    li_pos_2.append(state[1])
    
start = int(50/dt)
plt.plot(li_time[start:], li_pos_1[start:])
plt.plot(li_time[start:], li_pos_2[start:])
