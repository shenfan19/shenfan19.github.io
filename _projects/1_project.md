---
layout: page
title: Solar Sail Deformation & Adjustment
description: Deformation modeling and trajectory adjustment for flexible solar sail structures
img: assets/img/SHEN et al_3.jpeg
importance: 1
category: work
related_publications: true
---

Solar sails use lightweight materials and large structures to improve the performance of acceleration. However, during flight, structural deformations inevitably occur on the membrane due to solar pressure. These deformations affect geometry parameters and acceleration, making orbit and attitude control highly complicated given the changing moment of inertia.

Our research primarily investigates these small deformations occurring on the sail because of solar pressure, and how those shape changes propagate into attitude and trajectory control:

<div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/SHEN et al_3.jpeg" title="Solar sail deformation and lifting adjustment" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Deformation state and adjustment direction for the solar sail model.
</div>

<div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/SHEN et al_1.jpeg" title="Structural Deformation" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Structural deformation contour under solar pressure loading.
</div>

Finite-element analysis (FEA) has traditionally been used to study large-deformation solar sails, considering the nonlinearity of highly flexible booms. In this work, we analyze the modeling approaches, including multi-particle numerical models, to understand elastic models in two dimensions (without out-of-plane stiffness) for spinning solar sail attitude controls.

<div class="row justify-content-sm-center">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/SHEN et al_2.jpeg" title="Simulation analysis" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/SHEN et al_0.png" title="Trajectory correction variables" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

Our findings highlight that attitude control alone may not compensate for failures caused by deformation. It underscores the critical need to accurately study membrane deformation and subsequent trajectory modifications when designing control systems.
