# Boid Simulation

This repository contains a Python implementation of a boid simulation using Pygame.

## Introduction

Boids are a type of artificial life program, simulating the flocking behavior of birds. This project demonstrates the principles of separation, alignment, and cohesion to simulate this behavior.

## Key Features

1. **Flocking Behavior**: Demonstrates how boids avoid crowding, align with neighbors' heading, and move towards the average position of neighbors.
2. **Interactive Visualization**: Utilizes Pygame for an interactive visualization of boid movement and behavior.
3. **User Interaction**: Users can modify simulation parameters and observe how changes affect flocking dynamics.
4. **Educational Tool**: Serves as an educational tool to understand emergent behaviors in collective systems and swarm intelligence.

## How It Works

The simulation follows three main rules to achieve flocking behavior:
1. **Separation**: Boids avoid crowding neighbors.
2. **Alignment**: Boids steer towards the average heading of neighbors.
3. **Cohesion**: Boids move towards the average position of neighbors.

## Usage

1. **Installation**:
   - Ensure Python and Pygame are installed.
   - Use pip to install Pygame: `pip install pygame`

2. **Clone Repository**:
   ```sh
   git clone https://github.com/your-username/boid-simulation.git
   cd boid-simulation
