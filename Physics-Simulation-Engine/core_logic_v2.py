# Physics-Simulation-Engine - Module v2
def simulate_physics(time_step=0.01):
    print('Calculating GPR Wave Propagations...')
    # Logic: Basic propagation check
    if time_step <= 0:
        return "Error: Invalid time step"
    
    velocity = 3e8 # Speed of light in vacuum (approx)
    distance = velocity * time_step
    print(f"Wave traveled {distance} meters in {time_step}s")
    return True