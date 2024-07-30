# Tech Radar Slides

This folder contains slides for our Tech Radar discussions, where we track, record the summary and actions from the tech radar refresh across all categories. The slides are organised by the date of the tech radar refresh, with each category having its own `README.md` file.


The slides are created using [MARP](https://marp.app/), a tool that helps you create presentations using Markdown. The `.github/workflows` folder contains a GitHub Action workflow that automatically converts the README.md files to HTML and deploys to GitHub pages when changes are pushed to `main`. The link to the slides are provided in the README.md header.

The process aims at assisting the team facilitators in presenting a summary of their discussions, highlight key takeaways, new entries, and technologies requiring further assessment.

**To update the slides:**

- Navigate to the relevant tech radar refresh folder, e.g. slides/2024_august
- Open the `README.md` file in the allocated category folder e.g languages
- Review and update the content to reflect the outcomes of the most recent Tech Radar discussion
    - Add any new technologies that have been assessed
    - Note any technologies that are now on pause
    - List any technologies that need further assessment in upcoming discussions
- Create a Pull Request to merge your changes into the main branch.
- Once approved, the GitHub Actions workflow will automatically build and deploy the slides.

**Tips and Reminders:**
* Make sure to follow the Markdown formatting guidelines to ensure a consistent look and feel across all category pages.
* Keep the README.md files up-to-date with the latest Tech Radar discussions.
* If you need help or have questions, don't hesitate to reach out to the team.
