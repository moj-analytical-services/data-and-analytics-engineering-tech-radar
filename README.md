# Data and Analytics Engineering Tech Radar

In the MoJ [Data and Analytics Engineering community](https://ministryofjustice.github.io/data-and-analytics-engineering/), 
we maintain a [public Tech Radar](http://zalando.github.io/tech-radar/) to help our teams
align on technology choices. It is based on the [pioneering work
by ThoughtWorks](https://www.thoughtworks.com/radar) and uses Zalando's 
[`radar.js`](https://github.com/zalando/tech-radar/blob/master/docs/radar.js) [d3.js v4](https://d3js.org) visualisation.

Tech radar blips are configured in `blips.json` against tech radar rings 
and quadrants configured in `radar_config.json`. 

We use GitHub discussions to provide additional context to the blips, 
and the GitHub graphql API to automate the population of `blips.json`.