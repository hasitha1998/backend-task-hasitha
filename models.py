from pydantic import BaseModel, Field
from typing import List, Optional

class NameFormModel(BaseModel):
    first_name: str
    last_name: str

class EmailFormModel(BaseModel):
    email: str

class CountryFormModel(BaseModel):
    country: str

class PhoneFormModel(BaseModel):
    phone_number: str

class LanguagesFormModel(BaseModel):
    languages: List[str]

class CodingExperienceFormModel(BaseModel):
    experience_level: str

class AnnualCompensationFormModel(BaseModel):
    compensation: str

class CertifyingStatementFormModel(BaseModel):
    acceptance: bool
