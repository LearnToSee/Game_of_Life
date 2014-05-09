import sys
sys.path.insert(0,'lib/')
from life_grid_world import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation

gl = GridLife()

state_matrix= gl.init_grid_world()

def animate(framenumber):

            global state_matrix
            newGrid = state_matrix

            mat.set_data(newGrid)

            newGrid = gl.set_next_state_matrix(state_matrix)
            state_matrix = newGrid
            return [mat]



if __name__=='__main__':

    fig, ax = plt.subplots()
    mat = ax.matshow(state_matrix)
    ani = animation.FuncAnimation(fig, animate, frames=20,save_count=20)
    plt.show()
