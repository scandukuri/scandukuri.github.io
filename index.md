---
layout: home
title: Home
---

<div id="intro-wrapper" class="l-text">
	<div id="intro-title-wrapper">
		<div id="intro-image-wrapper">
			<img id="intro-image" src="/images/profile-square.png"></div>
		<div id="intro-title-text-wrapper">
			<h1 id="intro-title">Hi, I'm Chinmaya</h1>
			<div id="intro-subtitle">I'm a student at Stanford University.</div>
			<div id="intro-title-socials">
				{% for link in site.data.social-links %}
					{% if link.on-homepage == true %}
						{% include social-link.html link=link %}
					{% endif %}
				{% endfor %}
			</div>
		</div>
	</div>
	<!-- <hr class="l-middle home-hr"> -->
	<div id="everything-else" class="l-middle">
		<a href="{{ site.url }}/cv"><div><i class="fa fa-portrait icon icon-right-space"></i>CV</div></a>
		<a href="{{ site.url }}/projects"><div><i class="fa fa-shapes icon icon-right-space"></i>Projects</div></a>
		<a href="{{ site.url }}/everything-else"><div><i class="fa fa-list-ul icon icon-right-space"></i>Everything Else</div></a>
	</div>
	<div>
		I'm interested in building AI systems that are <b>open, safe</b>, and <b>useful</b> by studying reasoning and problem-solving in language models. Recently, I've been thinking about bootstrapping and self-improvement in language models with <a href="https://cocolab.stanford.edu/ndg"> Noah Goodman</a> and <a href="https://janphilippfranken.github.io/"> Jan-Philipp Fränken</a>.
	</div>
	<div style="height: 1rem"></div>
	<div>
		I recently received my B.S. in Mathematical and Computational Science from <img class="intro-logo" style="width: 13px; padding-bottom: 5px;" src="/images/stanford.svg"> Stanford University, where I'm currently working on my M.S. in Computer Science.
	</div>
	<!-- <div style="height: 1rem"></div>
	<div>
		I have collaborated with designers, developers, artists, and scientists while working at <img class="intro-logo" style="width: 19px; padding-bottom: 5px;" src="/images/apple.svg"> Apple, <img class="intro-logo" style="width: 18px; padding-bottom: 3px;" src="/images/microsoft.svg"> Microsoft Research, <img class="intro-logo" style="width: 24px" src="/images/nasa.svg"> NASA Jet Propulsion Lab, and <img class="intro-logo" style="width: 24px;" src="/images/pnnl.svg"> Pacific Northwest National Lab.
	</div> -->
</div>

<hr class="l-middle home-hr">

<h2 class="feature-title">Featured <a href="https://scandukuri.github.io/projects/">projects</a></h2>

<p class="feature-text">
	Some research, academic course projects, and miscellaneous interests.
</p>

<div class="cover-wrapper cover-wrapper-2-col l-middle">
	{% assign projects = site.data.articles | where: "project", true %}
	{% for feature in projects %}
		{% include feature.html feature=feature %}
	{% endfor %}
</div>

