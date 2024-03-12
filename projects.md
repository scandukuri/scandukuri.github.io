---
layout: page
title: Projects
permalink: projects/
---

Things I do, including research, academic course projects, and miscellaneous interests. 

### Research
Nothing yet, but stay tuned.

## Unpublished work

Short experiments, investigations or projects that aren't quite suited for paper form

<div class="project-spacer-small"></div>

<div class="cover-wrapper cover-wrapper-2-col l-middle">
	{% assign parametric = site.data.articles | where: "unpublished", true %}
	{% for feature in parametric %}
		{% include feature.html feature=feature %}
	{% endfor %}
</div>

<div class="project-spacer-small"></div>

### Unpublished work
<ul>
<li><a href="https://github.com/janphilippfranken/printllama">printllama<a/> <small style="color: #c0c0c0">2024</small>
<li><a href="https://scandukuri.github.io/independent-research/normbank">manipulativeLMs</a> <small style="color: #c0c0c0">2023</small></li>
