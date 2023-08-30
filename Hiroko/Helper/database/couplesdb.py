from typing import Dict, List, Union
from config import MONGO_URL
from motor.motor_asyncio import AsyncIOMotorClient as MongoCli

mongo = MongoCli(MONGO_URL).Rankings

coupledb = mongo.couple

   
async def _get_lovers(chat_id: int):
    lovers = await coupledb.find_one({"chat_id": chat_id})
    if lovers and "couple" in lovers:
        lovers = lovers["couple"]
    else:
        lovers = {}
    return lovers
    

async def get_couple(chat_id: int, date: str):
    lovers = await _get_lovers(chat_id)
    if date in lovers:
        return lovers["date"]
    else:
        return False


async def save_couple(chat_id: int, date: str, couple: dict):
    lovers = await _get_lovers(chat_id)
    lovers[date] = couple
    await coupledb.update_one(
        {"chat_id": chat_id},
        {"$set": {"couple": lovers}},
        upsert=True,
    )
