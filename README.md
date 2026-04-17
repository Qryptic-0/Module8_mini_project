# Module8_mini_project
Telegram Bot


HOW TO OBTAIN THE BOT TOKEN 

 1. Find the BotFather
 * Open your **Telegram app**.
 * In the search bar, type @BotFather.
 * Look for the one with the **blue verified checkmark**.
 * Click **Start** (or "Restart" if you've used it before).
 2. Create the New Bot
 * Type or click the command: /newbot.
 * **Choose a Name:** BotFather will ask for a name. This is the display name users will see (e.g., My Bootcamp Bot).
 * **Choose a Username:** This must end in the word bot (e.g., GeminiHelperBot or task_manager_bot). It must be unique; if the one you want is taken, try adding numbers or underscores.
 3. Save Your Token
 * Once the username is accepted, BotFather will send you a long message.
 * Look for the text that says: **"Use this token to access the HTTP API:"**
 * Below that, you will see a string of numbers and letters (e.g., 123456789:ABCDefGhIJKlmNoP_qrsTUVwxyZ).
 * **Copy this token.** This is what goes into your main.py code.



SETUP INSTRUCTIONS 
1. Install Python 3.9 or higher
2. Open your terminal and run pip install -r requirements.txt.
3. Create an .env file and paste your Telegram Bot token.
4. Run the bot by typing main.py


DEPLOYMENT GUIDE 
This bot can be deployed to any cloud server that supports Python like an AWS EC2 instance or Heroku.
1. Clone the repository to the server
2. Install dependencies using pip install -r requirements.txt
3. Setup the environment variables(the token) in the server's control panel.
4. Run main.py using a procesß manager like PM2 to keep it running forever.


BOT FEATURES 

 * User Persistence: Automatically detects and saves new users to a SQLite database.
 * Message Tracking: Counts how many messages a user sends.
 * Keyword Intelligence: Uses Regular Expressions (Regex) to respond to greetings and bootcamp-related words.
 * Interactive UI: Features an Inline Keyboard (button) that links to the project repository.
 * Self-Service Stats: Users can check their own engagement via the /stats command.





*Note: Due to unforeseen power outages and hardware limitations, I had to build this final project using mobile tools and architectural assistance. While I couldn't run a full local test environment, I focused on mastering the logic behind SQLAlchemy for data persistence and Regex for intelligent keyword matching. I am submitting this merely as a demonstration of my understanding of backend architecture.*
