---
title: Task Prioritization Environment
emoji: 🤖
colorFrom: blue
colorTo: green
sdk: docker
app_port: 7860
---


# Task Prioritization Environment

## Overview
This project simulates a real-world task management system where an AI agent learns to prioritize tasks, manage time, and reduce procrastination.

## Motivation
Procrastination and poor time management are common real-world problems. This environment models task scheduling decisions to help AI learn efficient behavior.

## Environment Design

### Observation Space
- List of tasks (id, priority, deadline, done)
- Current time

### Action Space
- complete(task_id)
- skip
- increase_priority(task_id)

### Reward Function
- +reward for completing tasks
- higher reward for high-priority tasks
- penalty for delays or bad actions

## Tasks

### Easy
Complete at least one task.

### Medium
Complete multiple tasks with decent efficiency.

### Hard
Complete all tasks optimally before deadlines.

## Setup

```bash
pip install -r requirements.txt
python test_env.py