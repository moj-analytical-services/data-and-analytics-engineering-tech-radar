# Data and Analytics Engineering Tech Radar

The MoJ [Data and Analytics Engineering community](https://ministryofjustice.github.io/data-and-analytics-engineering/)
maintains a [public Tech Radar](http://zalando.github.io/tech-radar/) to help
align technology choices within our teams. This Tech Radar is based on [pioneering work
by ThoughtWorks](https://www.thoughtworks.com/radar) and uses Zalando's JavaScript Library
[`radar.js`](https://github.com/zalando/tech-radar/blob/master/docs/radar.js) with [d3.js v4](https://d3js.org) for visualisation.

Tech radar blips are configured in `blips.json`, while tech radar rings and quadrants are set up in `radar_config.json`. Additional context for the blips is provided by GitHub discussions, which are queried using the GitHub GraphQL API to populate `blips.json`


### Viewing the output locally in VS Code
#### Install Live Server Extension
<ol>
  <li>Open Visual Studio Code: Launch VS Code on your computer.</li>
  <li>Access Extensions: Click on the Extensions icon in the Activity Bar on the side of the window.</li>
<li>Search for Live Server: In the Extensions view, type "Live Server" in the search bar.</li>
<li>Install Live Server: Click on the Install button for the Live Server extension.</li>
</ol>

#### Start Live Server

<ol>
  <li> Open Your Project: Open the folder containing your project files, including index.html</li>
  <li>Start Live Server: Right-click on your index.html file and select "Open with Live Server" from the context menu.</li>
</ol>