from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = "mongodb://localhost:27017"  # MongoDB connection URL (local)
mongo_client = AsyncIOMotorClient(MONGO_URL)  # Create an async MongoDB client
db = mongo_client["mail_summarizer"]  # Get the "mail_summarizer" database
summaries_collection = db["summaries"]  # Get the "summaries" collection