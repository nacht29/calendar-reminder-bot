import logging
from telegram import Update, BotCommand
from telegram.ext import Application, CommandHandler, ContextTypes

# logging
logging.basicConfig(
	format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
	level=logging.INFO
)

# bot token
TOKEN = '7248700753:AAEsdVfcYvsBdWKAZZyM0RPJZZ5w-hFmCKw'

async def start(update:Update, context:ContextTypes.DEFAULT_TYPE):
	await update.message.reply_text('Hello! I am Nacht29, your personal Google Clendar Reminder')
	logging.info(f'Start command received from {update.effective_user.id}')

async def echo(update:Update, context:ContextTypes.DEFAULT_TYPE):
	text = update.message.text[6:] # skip /echo
	await update.message.reply_text(text)
	logging.info(f'Echo command received: {text}')

async def set_commands(application:Application):
	logging.info('Setting bot commands...')
	try:
		await application.bot.set_my_commands([
			BotCommand(start, 'Start the bot'),
			BotCommand('echo', 'Echo your message')
		])
		logging.info('Bot commands set successfully!')
	except Exception as error:
		logging.error(f'Failed to set commands: {error}')

def main():
	app = Application.builder().token(TOKEN).post_init(set_commands).build()
	
	# command handlers
	app.add_handler(CommandHandler('start', start))
	app.add_handler(CommandHandler('echo', echo))
	
	logging.info('Bot is starting...')
	app.run_polling()

if __name__ == '__main__':
	main()