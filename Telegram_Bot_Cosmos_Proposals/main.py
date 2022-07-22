from requests import get
import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    filters,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

CHOOSING = range(1)


async def start(update: Update, context):
    """Start the conversation and ask user for input."""
    await update.message.reply_text(
        "Hello!\n To check current active governance proposals, type the network full name...\n👇👇👇",

    )

    return CHOOSING


async def proposals(update: Update, context):
    """Executing scraping code into TG chat"""
    text = update.message.text
    context.user_data["choice"] = text
    url = f"https://api.mintscan.io/v1/{text.lower()}/proposals"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
                                                                         Chrome/73.0.3683.103 Safari/537.36',
               'Accept': 'application/json'
               }
    data = get(url, headers=headers).json()

    for i in data:
        if i['proposal_status'] == 'PROPOSAL_STATUS_VOTING_PERIOD':
            number = i['id']
            title = i['title']
            link = f"https://www.mintscan.io/{text.lower()}/proposals/{number}"
            message = f"{text.lower()}\nProposal {number} is in voting stage!\n{title}\n{link}"
            await update.message.reply_text(f"{message}")
    await update.message.reply_text("\nTo try different network, type the full name below👇")


def main():
    # Place your token below
    application = Application.builder().token('TOKEN').build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            CHOOSING: [
                MessageHandler(
                    filters.Regex("^(cosmos|akash|bitcanna|comdex|evmos|kava|nyx|regen|stargaze|"
                                  "assetmantle|bitsong|crescent|fetch.ai|kichain|omniflix|rizon|starname|axelar|cerberus|"
                                  "crypto.org|g-bridge|konstellation|osmosis|secret|umee|band|certik|desmos|injective|"
                                  "lum|persistence|sentinel|binance|chihuahua|emoney|juno|medibloc|provenance|sifchain|irishub)$"),
                    proposals,

                ),
            ],

        },
        fallbacks=[MessageHandler(filters.Regex("^start$"), start)],

    )

    application.add_handler(conv_handler)

    application.run_polling()


if __name__ == "__main__":
    main()
