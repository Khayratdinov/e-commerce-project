from datetime import timedelta
from requests import get
import telegram
import asyncio


def message_for_developer(text):
    token = "5983933395:AAFkMDeyzhfPbeiylzUO-M6fb2EY-g19QJU"

    chat_id = "611841827"

    text = f"{ text }  "
    url = (
        f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}"
    )
    try:
        _ = get(url)
    except:
        print("Telegramga ma'lumot jo'natishda xatolik")


# import threading


# async def send_message_async(bot, chat_id, text):
#     await bot.send_message(chat_id=chat_id, text=text)


def send_order_to_telegram(order):
    bot_token = "5983933395:AAFkMDeyzhfPbeiylzUO-M6fb2EY-g19QJU"

    admin_chat_ids = "1400827875"

    orders_text = ""

    orders = order.order_item.select_related("collection_book", "product")

    for item in orders:
        product_title = (
            item.product.title
            if not item.collection_order_status
            else item.collection_book.title
        )
        orders_text += f"📙:{product_title} (x{item.quantity }{' :' if item.collection_order_status else ''})"

    order_data = order.created_at = order.created_at + timedelta(hours=5)
    message_text = f"""     🛎 Yangi buyirtma 🛍

🆔 Buyirtma raqami #{order.order_code}

👤 Buyurtmachi: {order.full_name}

📞 Telefon raqami: {order.phone_number}

🌍 Viloyat: {order.country}

🏡 Manzili: {order.street_address_1}

🏡 Qoshimcha manzil: {order.street_address_2}

🚚 Yetkazip berish: {order.shipping}

💸 Tolov: {order.total} so`m

💳 Tolov turi: {order.payment_methot}

⌛️ Buyurtma vaqti: {order_data.strftime("%d.%m.%Y %H:%M:%S")}


-------------------------
📚 Buyurtmalar:

{orders_text}
                    """

    bot = telegram.Bot(token=bot_token)

    # loop = asyncio.new_event_loop()
    # asyncio.set_event_loop(loop)

    # for chat_id in admin_chat_ids:
    #     asyncio.ensure_future(send_message_async(bot, chat_id, message_text), loop=loop)

    # loop.run_until_complete(asyncio.gather(*asyncio.all_tasks(loop=loop)))

    # loop.close()

    asyncio.run(bot.send_message(chat_id=admin_chat_ids, text=message_text))