# Data and Analytics Engineering Tech Radar

In the MoJ [Data and Analytics Engineering community](https://ministryofjustice.github.io/data-and-analytics-engineering/), 
we maintain a [public Tech Radar](http://zalando.github.io/tech-radar/) to help our teams
align on technology choices. It is based on the [pioneering work
by ThoughtWorks](https://www.thoughtworks.com/radar) and uses a modified version of Zalando's 
[`radar.js`](https://github.com/zalando/tech-radar/blob/master/docs/radar.js) [d3.js v4](https://d3js.org) tech radar visualisation.

Tech radar blips are configured in `blips.json` against tech radar rings 
and quadrants configured in `radar_config.json`. 

GitHub discussions provide additional context to the blips, 
which are queried using the GitHub graphql API to populate `blips.json`.

## Setting Up Visual Studio Code to Modify the Repository Locally
### How to Install a Live Server to Check the Output of index.html
To view the output of your index.html file in real-time, you need to install the Live Server extension. While some methods may suggest using tools like Yarn to install the necessary packages, we simplify the process by using the Live Server extension in Visual Studio Code (VS Code). This approach avoids unnecessary complexity and streamlines the workflow.
Follow these steps to install and use Live Server in Visual Studio Code:

Open Visual Studio Code: Launch VS Code on your computer.
- Access Extensions: Click on the Extensions icon in the Activity Bar on the side of the window.
- Search for Live Server: In the Extensions view, type "Live Server" in the search bar.
- Install Live Server: Click on the Install button for the Live Server extension.
- Open Your Project: Open the folder containing your project files, including index.html.
- Start Live Server: Right-click on your index.html file and select "Open with Live Server" from the context menu.
### Updating .py Files in manage_discussions locally

When your live server is running, some local file changes will be automatically reflected. However, if you need to make changes to a ```.py``` file in the manage_discussions directory, you must add an ```.env``` file to your root directory and include your GitHub token in that file. Follow these steps to obtain your GitHub token:
- Log in to GitHub: Go to GitHub and log in to your account.
- Access Settings: Click on your profile picture in the upper-right corner and select "Settings" from the dropdown menu.
- Navigate to Developer Settings: Scroll down and click on "Developer settings" in the left-hand menu.
- Generate a New Token: Click on "Personal access tokens" and then on "Generate new token".
- Select Scopes: Select the scopes or permissions you need for your token. For most purposes, repo (full control of private repositories) and user (read user data) are sufficient.
- Generate Token: Click the "Generate token" button at the bottom of the page.
- Copy the Token: Copy the generated token. Make sure to store it securely as it will not be shown again.