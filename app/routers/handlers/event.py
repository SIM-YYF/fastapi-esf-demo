from app import db


async def start_up():
    await db.database.connect()


async def shut_down():
    await db.database.disconnect()
