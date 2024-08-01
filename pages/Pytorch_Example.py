import streamlit as st
import torch
import torch.nn as nn
import torch.optim as optim

# Define a simple neural network
class AINetwork(nn.Module):
    def __init__(self):
        super(AINetwork, self).__init__()
        self.fc1 = nn.Linear(2, 4)  # Taking two inputs: in_air and distance_to_obstacle
        self.fc2 = nn.Linear(4, 2)   # Two outputs: jump (0) or don't jump (1)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        return torch.softmax(self.fc2(x), dim=0)

# Function to decide whether to jump
def decide_jump(in_air, distance_to_obstacle):
    model = AINetwork()
    inputs = torch.tensor([float(in_air), distance_to_obstacle])
    output = model(inputs)

    # Action: jump (0) or don't jump (1)
    action = torch.argmax(output).item()  # 0 means jump, 1 means do not jump
    return action

# Simulation function
def simulate(in_air, distance_to_obstacle):
    score = 0
    score_feedback = []

    while True:
        # Decision-making
        jump_decision = decide_jump(in_air, distance_to_obstacle)

        # Check jump action
        if jump_decision == 0:  # AI decides to jump
            score_feedback.append("AI decides to jump!")

        # Score increases over time
        score += 1
        score_feedback.append(f"Current score: {score}")

        # Simulate hitting an obstacle (for demonstration we assume this happens randomly)
        if distance_to_obstacle < 1.0:  # Arbitrary condition to hit an obstacle
            score_feedback.append("AI hits an obstacle!")
            score = -100
            break

        # Decrease distance to obstacle over time for simulation
        distance_to_obstacle -= 0.1  # Simulate movement towards the obstacle
        if distance_to_obstacle < 0:
            distance_to_obstacle = 0

        # Simulate ground state
        in_air = False

    return score, score_feedback

# Streamlit app
def main():
    st.title("AI Jump Decision Simulation")

    in_air = st.checkbox("In Air", value=False)
    distance_to_obstacle = st.number_input("Distance to Obstacle", min_value=0.0, max_value=100.0, value=10.0, step=0.1)

    if st.button("Simulate"):
        final_score, feedback = simulate(in_air, distance_to_obstacle)
        st.subheader("Simulation Feedback")
        for line in feedback:
            st.write(line)
        st.write(f"Final score: {final_score}")

if __name__ == "__main__":
    main()