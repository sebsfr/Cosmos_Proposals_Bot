Telegram Bot written in Python using PTB ver.20.0 initially deployed on Heroku (free plan) for some time just for testing purpose, shows only active proposals from the Cosmos ecosystem by scraping data from [Mintscan](https://www.mintscan.io/cosmos/proposals).

# USAGE

1.Search for the bot by looking for CosmosProposals with avatar

![alt text](https://github.com/sebsfr/Cosmos_Proposals_Bot/blob/main/Telegram_Bot_Cosmos_Proposals/pictures/image.png?raw=True "Title")

2.  To start the bot simply type ***start*** or click the ***start*** button at the bottom of the window.
3. Now you can choose the network to see all available proposals by typing the full name with small letters e.g. ***cosmos, juno, sifchain, chihuahua***.

# PROBLEMS

- Since I am using loops and asyncio, what telegram does not really "like" based on my understanding, I couldn't find a solution on how to show a notification, that on a chosen network by the user there are no active proposals, hence there will not be showing anything in that scenario.

![alt text](https://github.com/sebsfr/Cosmos_Proposals_Bot/blob/main/Telegram_Bot_Cosmos_Proposals/pictures/example.png?raw=True "Title")



- I'm still working on message handlers and as I am using new PTB, I didn't figure it out yet...
