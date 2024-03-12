---
layout: page
title: Projects
permalink: projects/
---

Things I do, including research, academic course projects, and miscellaneous interests.


## Research

Research publications for fans of language modeling, AI cognition and reasoning.

<div class="project-spacer-small"></div>

<div class="l-page project-grid">
    {% for project in site.categories.papers | where: 'published', true %}
    {% include project.html project=project %}
    {% endfor %}
</div>

<div class="project-spacer"></div>

## Unpublished work

Short investigations or side projects.

<div class="project-spacer-small"></div>

<div class="l-page project-grid">
    {% for project in site.categories.papers | where: 'unpublished', true%}
    {% include project.html project=project %}
    {% endfor %}
</div>

<div class="project-spacer"></div>


## Course Projects

<ul>
    <li><a href="{{ site.url }}/projects/cs-6750-health-easel">Health Easel</a> <small style="color: #c0c0c0">2017</small></li>
    <li><a href="{{ site.url }}/projects/cs-7450-a-viz-of-ice-and-fire">A Viz of Ice and Fire</a> <small style="color: #c0c0c0">2016</small></li>
    <li><a href="{{ site.url }}/projects/materials-informatics-grain-growth">Materials Informatics: Grain Growth</a> <small style="color: #c0c0c0">2016</small></li>
    <li><a href="{{ site.url }}/projects/cse-6730-bobby-dodd-simulation">Modeling of Pedestrian Traffic Around Bobby-Dodd Stadium</a> <small style="color: #c0c0c0">2016</small></li>
    <li><a href="{{ site.url }}/projects/uga-undergrad-course-projects">UGA Undergrad Course Projects</a></li>
    <ul style="padding-left: 3rem;">
        <li>Image Compression <small style="color: #c0c0c0">2014</small></li>
        <li>Railgun Simulation <small style="color: #c0c0c0">2014</small></li>
        <li>Path Minimization <small style="color: #c0c0c0">2013</small></li>
        <li>Numerical ODE Solution and Integration Project <small style="color: #c0c0c0">2013</small></li>
    </ul>
    <li><a href="{{ site.url }}/projects/cube-decomposition-trophy">Cube Decomposition Trophy</a> <small style="color: #c0c0c0">2014</small></li>
    <li><a href="{{ site.url }}/projects/uga-keychain">UGA Keychain</a> <small style="color: #c0c0c0">2014</small></li>
</ul>

<div class="project-spacer-small"></div>

## Other

<ul>
<li><a href="https://github.com/fredhohman/fredhohman.github.io"><code>fredhohman.com</code> on Github</a></li>
<li><a href="{{ site.url }}/projects/raspberry-pi-case">Raspberry Pi Case</a> <small style="color: #c0c0c0">2013</small></li>
<li><a href="{{ site.url }}/projects/road-bike-restoration">Road Bike Restoration</a> <small style="color: #c0c0c0">2012</small></li>
</ul>

[trefoil]: {{ site.url }}/projects/3d-printing-the-trefoil-knot-and-its-pages "3D Printing the Trefoil Knot and its Pages"
[reu]: {{ site.url }}/projects/mathematics-&-computational-science-reu "Mathematics & Computational Science REU"

