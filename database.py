from motor.motor_asyncio import AsyncIOMotorClient
from bson.objectid import ObjectId
from urllib.parse import quote_plus

# URL encode your username and password
username = quote_plus('admin')  # Replace 'admin' with your actual username if different
password = quote_plus('1234@')  # Replace '1234' with your actual password

# Properly formatted MongoDB connection string
MONGO_DETAILS = f"mongodb+srv://{username}:{password}@cluster0.guvmtb9.mongodb.net/?retryWrites=true&w=majority"

client = AsyncIOMotorClient(MONGO_DETAILS)

database = client['cluster0']  # Replace 'your_database_name' with your actual database name

# Collections
name_collection = database.get_collection("names")
email_collection = database.get_collection("emails")
country_collection = database.get_collection("countries")
phone_collection = database.get_collection("phones")
languages_collection = database.get_collection("languages")
experience_collection = database.get_collection("experiences")
compensation_collection = database.get_collection("compensations")
certification_collection = database.get_collection("certifications")

# Helper function to format BSON ObjectId to string
def format_id(document):
    document["_id"] = str(document["_id"])
    return document
