---
layout: page
title: Projects
permalink: projects/
---
<p>Some research, academic course projects, and miscellaneous interests.</p>

### Research
Nothing yet, but stay tuned.
<div class="project-spacer-small"></div>

### Unpublished work
Short experiments, investigations or projects that aren't quite suited for paper form.
<div class="project-spacer-small"></div>
<div class="cover-wrapper cover-wrapper-2-col l-middle">
	{% assign projects = site.data.articles | where: "project", true %}
	{% for feature in projects %}
		{% include feature.html feature=feature %}
	{% endfor %}
</div>
