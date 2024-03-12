---
layout: page
title: Projects
permalink: projects/
---

Things I do, including research, academic course projects, and miscellaneous interests. 

### Research
Nothing yet, but stay tuned.

<div class="project-spacer-small"></div>

### Unpublished work

Short experiments, investigations or projects that aren't quite suited for paper form

<div class="project-spacer-small"></div>

<div class="cover-wrapper cover-wrapper-2-col l-middle">
	{% assign parametric = site.data.articles | where: "unpublished", true %}
	{% for feature in parametric %}
		{% include feature.html feature=feature %}
	{% endfor %}
</div>
