Discord Bot version is scraping data to the Discord server chat same as the telegram version hovewer it will ping only new proposals after checking on them according to specific time frame that can be adjusted in the line 36.
# REQUIRED ACTIONS
1. Generate new token from [Discord Developer Portal](https://discord.com/developers/applications)
2. Paste your token in the line 39,
- Unless you are using web server like ***Repl.it*** to host your bot, you will have to create ***env*** file containing your Token and 
modify line 39 into ***client.run(os.getenv("TOKEN"))***
