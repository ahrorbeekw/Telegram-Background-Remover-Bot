Features

Accepts images from users via Telegram.

Removes the background from the image.

Returns the processed image back to the user.

Requirements

Python 3.8+

Telegram Bot Token

The following Python libraries:

aiogram

rembg

Pillow

requests

Installation

Clone this repository:

git clone https://github.com/yourusername/telegram-bg-remover-bot.git
cd telegram-bg-remover-bot

Install required dependencies:

pip install aiogram rembg pillow requests

Set up your bot token:

Get your bot token from BotFather.

Replace TOKEN = "bot tokeni" in bot.py with your actual bot token.

Usage

Run the bot using the following command:

python bot.py

After starting the bot, send an image via Telegram. The bot will process the image and return the background-removed version.

Bot Code Explanation

The bot is structured as follows:

The bot uses aiogram for handling messages and commands.

When a user sends an image, the bot:

Retrieves the file from Telegram servers.

Downloads the file.

Processes the image using rembg to remove the background.

Sends the processed image back to the user.

Notes

The bot may take a few seconds to process high-resolution images.

Ensure that your bot has permission to receive and send images in Telegram.

License

This project is licensed under the MIT License.
