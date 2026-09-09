---
layout: page
title: Life Matters
description: An open framework for simulating and optimizing individual-scale health and behavioral decisions
img: assets/img/3.jpg
importance: 1
category: work
---

Life Matters (LM) is a cross-scale, multi-model dynamics simulation framework for individual-scale health and behavioral decisions, spanning timescales from minutes to years. It converts statistical findings from published medical and social-science literature, such as odds ratios, hazard ratios, and effect sizes, into runnable dynamics models, then searches the space of possible interventions, diet, exercise, and medication timing among them, for Pareto-optimal tradeoffs.

The project treats a decision problem as a coupling problem rather than a single-study replication problem. Instead of reproducing one paper's conclusion at a time, each model places mechanisms independently validated by separate publications into the same dynamical system, letting mechanisms that would otherwise never interact do so, and surfacing tradeoffs that are invisible within any single paper's own scope. The same framework also serves as a consistency check: parameters drawn from multiple independent sources can be tested for whether they remain jointly feasible once combined.

LM is organized as three connected components: an open YAML format specification for describing variables, equations, simulation, and optimization; a reference simulation and multi-objective optimization engine with a web interface; and a growing library of literature-grounded models spanning physiology, nutrition, disease, and social dynamics. A card-game frontend presents the same simulated scenarios, historical figures, literary characters, and medical cases, through gameplay.

Source code, documentation, and a live demo are available at [life-matters-reference-engine](https://github.com/shenfan19/life-matters-reference-engine) and [life-matters-models](https://github.com/shenfan19/life-matters-models). This is ongoing work; a paper describing the format and a set of worked case studies is in preparation.
