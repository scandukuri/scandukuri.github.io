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
			<div id="intro-subtitle">I'm a researcher + engineer at Capital One.</div>
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
		I'm interested in building AI systems that are <b>safe</b> and <b>useful</b> by studying the abilities and limitations of language models. Currently, I'm a software engineer in the Applied Research group at Capital One, where I work on making language models better assistants through simulation, synthetic data, and evaluation. Previously, I worked on LM bootstrapping and self-improvement in Stanford's <a href="https://cocolab.stanford.edu/"> Computation & Cognition Lab</a>, advised by <a href="https://cocolab.stanford.edu/ndg"> Noah Goodman</a> and <a href="https://janphilippfranken.github.io/"> Jan-Philipp Fränken</a>. 
	</div>
	<div style="height: 1rem"></div>
	<div>
		I recently received my B.S. in Mathematical and Computational Science from <img class="intro-logo" style="width: 13px; padding-bottom: 5px; margin-left: 3px; margin-right: 3px;" src="/images/stanford.svg">
 Stanford University, where I'm currently working on my M.S. in Computer Science (on leave). 
	</div>
	<!-- <div style="height: 1rem"></div>
	<div>
		I have collaborated with designers, developers, artists, and scientists while working at <img class="intro-logo" style="width: 19px; padding-bottom: 5px;" src="/images/apple.svg"> Apple, <img class="intro-logo" style="width: 18px; padding-bottom: 3px;" src="/images/microsoft.svg"> Microsoft Research, <img class="intro-logo" style="width: 24px" src="/images/nasa.svg"> NASA Jet Propulsion Lab, and <img class="intro-logo" style="width: 24px;" src="/images/pnnl.svg"> Pacific Northwest National Lab.
	</div> -->


</div>

<hr class="l-middle home-hr">

<h2 class="feature-title">Featured <a href="/cv/#publications">research publications</a></h2>

<p class="feature-text">
	Latest research.
</p>

<div class="cover-wrapper cover-wrapper-2-col l-page">
	{% assign sortedPublications = site.categories.papers | sort: 'feature-order' %}
	{% for feature in sortedPublications %}
		{% if feature.featured == true %}
			{% include feature.html feature=feature %}
		{% endif %}
	{% endfor %}
</div>

<br>

<hr class="l-middle home-hr">

<h2 class="feature-title">Featured <a href="https://scandukuri.github.io/projects/">projects</a></h2>

<p class="feature-text">
	Some academic course projects, mini-investigations and miscellaneous interests.
</p>

<div class="cover-wrapper cover-wrapper-3-col l-middle">
	{% assign projects = site.data.articles | where: "project", true %}
	{% for feature in projects %}
		{% include feature.html feature=feature %}
	{% endfor %}
</div>

