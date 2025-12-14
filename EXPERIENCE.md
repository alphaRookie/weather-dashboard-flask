# Tool Selection Justification

I used GitHub Copilot as the vibe coding tool for this project. I chose Copilot because it is directly integrated into VS Code and can assist me during coding without interrupting the development flow. It helped save time when fixing simple to medium-level mistakes and was mainly useful for debugging and small code suggestions rather than generating full features.

I did not rely heavily on Copilot for learning concepts. For understanding code flow, connections between components, and best practices used by real developers, I preferred using chatgpt, which provide clearer explanations and reasoning behind the code.

---

#  Development Process

I started with a basic Flask setup and a simple route to make sure the page could render correctly. After that, I worked on the weather API logic separately, first focusing on fetching coordinates and then retrieving the weather data. Once that part was working, I connected it to the Flask route so the data could be displayed on the page.

Each time I added or changed something, I tested the app manually by entering both valid and invalid inputs and refreshing the page to see how it behaved. When bugs appeared, I checked the error messages, adjusted the logic, and tested again until the issue was fixed. This trial-and-error process helped me understand the flow of the application and made the final result more stable.

During development, I wrote most of the project manually, also i get some help from Youtube tutorial, and then improve it with my idea. When errors occurred, such as runtime errors or incorrect request handling, I used GitHub Copilot to help identify possible causes and suggest fixes.

---

# Challenges and Solutions

One major challenge was that refreshing the page caused the same weather data or error message to appear again. This happened because the POST request was being reused. I solved this by applying the Post/Redirect/Get pattern and using sessions to store temporary data.

Another challenge was handling invalid or empty API responses. Sometimes the API returned an empty list or unexpected data instead of valid coordinates. To prevent crashes, I added validation checks to ensure the response had the expected structure before using it.

Managing sensitive data such as API keys and the Flask secret key was also a challenge. I solved this by storing them in an `.env` file and using environment variables instead of hardcoding values.

---

# Reflection

This project showed me that vibe coding tools like GitHub Copilot are useful for increasing speed, especially during debugging, but they does not really makes me understand. For me, I still needed to learn concepts such as Flask request handling, sessions, and redirects separately from chatgpt.

Using Copilot changed my workflow by making error resolution faster, but I would not rely on it to build entire applications. In the future, I would use tools like this as assistants rather than primary developers. I believe this technology will improve productivity but still requires strong fundamentals from developers.
