---
layout: page
title: side projects
permalink: /side-projects/
description: Things I build outside my research, mostly small open-source tools that grew out of my own note-taking and planning.
nav: true
nav_order: 5
horizontal: true
---

<!-- pages/side-projects.md: the projects in category "side" -->
<div class="projects">
{% assign side_projects = site.projects | where: "category", "side" | sort: "importance" %}
{% if page.horizontal %}
  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
    {% for project in side_projects %}
      {% include projects_horizontal.liquid %}
    {% endfor %}
    </div>
  </div>
{% else %}
  <div class="row row-cols-1 row-cols-md-3">
    {% for project in side_projects %}
      {% include projects.liquid %}
    {% endfor %}
  </div>
{% endif %}
</div>
