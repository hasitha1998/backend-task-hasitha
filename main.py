import uvicorn
from fastapi import FastAPI
from database import (
    name_collection,
    email_collection,
    country_collection,
    phone_collection,
    languages_collection,
    experience_collection,
    compensation_collection,
    certification_collection
)
from models import (
    NameFormModel,
    EmailFormModel,
    CountryFormModel,
    PhoneFormModel,
    LanguagesFormModel,
    CodingExperienceFormModel,
    AnnualCompensationFormModel,
    CertifyingStatementFormModel
)
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

app = FastAPI()

@app.get("/")
async def root():
    logging.info("Root endpoint called")
    return {"message": "Hello World"}

@app.post("/submit-name")
async def submit_name(form: NameFormModel):
    logging.info(f"Name form submitted with data: {form}")
    # Process the name form data
    await name_collection.insert_one(form.dict())
    return {"message": "Name form submitted", "data": form}

@app.post("/submit-email")
async def submit_email(form: EmailFormModel):
    logging.info(f"Email form submitted with data: {form}")
    # Process the email form data
    await email_collection.insert_one(form.dict())
    return {"message": "Email form submitted", "data": form}

@app.post("/submit-country")
async def submit_country(form: CountryFormModel):
    logging.info(f"Country form submitted with data: {form}")
    # Process the country form data
    await country_collection.insert_one(form.dict())
    return {"message": "Country form submitted", "data": form}

@app.post("/submit-phone")
async def submit_phone(form: PhoneFormModel):
    logging.info(f"Phone form submitted with data: {form}")
    # Process the phone form data
    await phone_collection.insert_one(form.dict())
    return {"message": "Phone form submitted", "data": form}

@app.post("/submit-languages")
async def submit_languages(form: LanguagesFormModel):
    logging.info(f"Languages form submitted with data: {form}")
    # Process the languages form data
    await languages_collection.insert_one(form.dict())
    return {"message": "Languages form submitted", "data": form}

@app.post("/submit-experience")
async def submit_experience(form: CodingExperienceFormModel):
    logging.info(f"Coding experience form submitted with data: {form}")
    # Process the coding experience form data
    await experience_collection.insert_one(form.dict())
    return {"message": "Coding experience form submitted", "data": form}

@app.post("/submit-compensation")
async def submit_compensation(form: AnnualCompensationFormModel):
    logging.info(f"Annual compensation form submitted with data: {form}")
    # Process the annual compensation form data
    await compensation_collection.insert_one(form.dict())
    return {"message": "Annual compensation form submitted", "data": form}

@app.post("/submit-certification")
async def submit_certification(form: CertifyingStatementFormModel):
    logging.info(f"Certifying statement form submitted with data: {form}")
    # Process the certifying statement form data
    await certification_collection.insert_one(form.dict())
    return {"message": "Certifying statement form submitted", "data": form}

if __name__ == "__main__":
    logging.info("Starting server...")
    uvicorn.run(app, host="127.0.0.1", port=8000)
