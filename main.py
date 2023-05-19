from telegram import Bot, Filters, MessageTypes, ParseMode, Update
from payment import check
from db import register
from tiket import get
import time

TOKEKEY = ""

bot = Bot(token=TOKEKEY)

DB = register.newDB()


@bot.message(content_types=[MessageTypes.TEXT], filters=Filters.command('help'))
async def help_command(update: Update):
    # Obtener el mensaje original
    message = await update.get_message()
    if not message:
        return
    # Convertir el mensaje a mayúsculas
    new_text = message.text.upper()

    # Mandar el nuevo mensaje
    await update.send_message(new_text)


@bot.message(content_types=[MessageTypes.TEXT], filters=Filters.command('tiket'))
async def tiket_command(update: Update):
    message = await update.get_message()
    if not message:
        return
    pass

    message_index = message.text.split()

    confirmation_trx = await check.check_trx(message_index[1])

    if confirmation_trx < 0:
        await update.send_message("aun no hay confirmaciones del pago")

    itemhash = get.combinar_hash(message_index[1])

    try:
        await get.newtiket(DB, message_index[0], message_index[1], itemhash)
        await update.send_message("peticion hecha con exito")
    except:
        await update.send_message("hubo un error al procesar la peticion")


@bot.message(content_types=[MessageTypes.TEXT], filters=Filters.command('get'))
async def getiket_command(update: Update):
    message = await update.get_message()
    if not message:
        return

    result = await register.getpeticion(message.text)

    if result is None:
        await update.send_message("el tiket no existe")

    await update.send_message(f'fecha: {result["datetime"]}, peticion: {result["peticion"]}, trx: {result["payID"]}')


if __name__ == "__main__":

    bot = Bot(token='TOKEN', parse_mode=None)

    bot.add_handler(help_command, Filters.incoming_message())
    bot.add_handler(tiket_command, Filters.incoming_message())
    bot.add_handler(getiket_command, Filters.incoming_message())

    while True:
        try:
            bot.start_polling()
            bot.stop_polling()
        except KeyboardInterrupt:
            break
