import decimal

import logging



logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

import sqlalchemy



from sqlalchemy.sql import func  # end imports from system/genai/create_db_models_inserts/create_db_models_prefix.py



from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Base class
Base = declarative_base()

# Database creation
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')

# Define each table with a description and necessary fields

class Patient(Base):
    """description: Stores patient information."""
    __tablename__ = 'patients'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    dob = Column(DateTime, nullable=False)
    gender = Column(String, nullable=True)

class Doctor(Base):
    """description: Stores doctor information."""
    __tablename__ = 'doctors'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    specialty = Column(String, nullable=True)

class Appointment(Base):
    """description: Stores appointment details."""
    __tablename__ = 'appointments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    doctor_id = Column(Integer, ForeignKey('doctors.id'), nullable=False)
    appointment_date = Column(DateTime, nullable=False)
    notes = Column(String, nullable=True)

class Prescription(Base):
    """description: Contains prescription data."""
    __tablename__ = 'prescriptions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    appointment_id = Column(Integer, ForeignKey('appointments.id'), nullable=False)
    medication_name = Column(String, nullable=False)
    dosage = Column(String, nullable=True)
    instructions = Column(String, nullable=True)

class MedicalRecord(Base):
    """description: Stores medical records for each patient."""
    __tablename__ = 'medical_records'
    id = Column(Integer, primary_key=True, autoincrement=True)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    diagnosis = Column(String, nullable=True)
    treatment = Column(String, nullable=True)
    record_date = Column(DateTime, nullable=False, default=datetime.utcnow)

class Billing(Base):
    """description: Manages billing information."""
    __tablename__ = 'billing'
    id = Column(Integer, primary_key=True, autoincrement=True)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    amount_due = Column(Float, nullable=False)
    due_date = Column(DateTime, nullable=False)
    paid_date = Column(DateTime, nullable=True)

class Insurance(Base):
    """description: Stores insurance details for patients."""
    __tablename__ = 'insurances'
    id = Column(Integer, primary_key=True, autoincrement=True)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    provider_name = Column(String, nullable=False)
    policy_number = Column(String, nullable=False)

class Department(Base):
    """description: Information about hospital departments."""
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=True)

class Nurse(Base):
    """description: Stores nurse information."""
    __tablename__ = 'nurses'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    department_id = Column(Integer, ForeignKey('departments.id'), nullable=True)

class Room(Base):
    """description: Contains details about hospital rooms."""
    __tablename__ = 'rooms'
    id = Column(Integer, primary_key=True, autoincrement=True)
    room_number = Column(String, nullable=False)
    department_id = Column(Integer, ForeignKey('departments.id'), nullable=True)
    type = Column(String, nullable=True)

class Treatment(Base):
    """description: Details of treatments given to patients."""
    __tablename__ = 'treatments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    medical_record_id = Column(Integer, ForeignKey('medical_records.id'), nullable=False)
    treatment_name = Column(String, nullable=False)
    cost = Column(Float, nullable=False)

class LabTest(Base):
    """description: Records laboratory tests results."""
    __tablename__ = 'lab_tests'
    id = Column(Integer, primary_key=True, autoincrement=True)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    test_name = Column(String, nullable=False)
    test_date = Column(DateTime, nullable=False)
    result = Column(String, nullable=True)

# Create all tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Insert sample data
session.add_all([
    Patient(first_name='Alice', last_name='Smith', dob=datetime(1990, 5, 24), gender='Female'),
    Patient(first_name='Bob', last_name='Jones', dob=datetime(1985, 8, 17), gender='Male'),
    Doctor(first_name='Emma', last_name='Brown', specialty='Cardiology'),
    Doctor(first_name='William', last_name='Davis', specialty='Neurology'),
    Appointment(patient_id=1, doctor_id=1, appointment_date=datetime(2023, 10, 10), notes='Routine check-up'),
    Prescription(appointment_id=1, medication_name='Aspirin', dosage='2 tablets', instructions='Take after meals'),
    MedicalRecord(patient_id=1, diagnosis='Hypertension', treatment='Lifestyle changes', record_date=datetime(2023, 10, 11)),
    Billing(patient_id=1, amount_due=200.00, due_date=datetime(2023, 11, 10), paid_date=None),
    Insurance(patient_id=1, provider_name='HealthSafe', policy_number='HS12345'),
    Department(name='Cardiology', location='3rd Floor'),
    Nurse(first_name='Jessica', last_name='Taylor', department_id=1),
    Room(room_number='101', department_id=1, type='Private'),
    Treatment(medical_record_id=1, treatment_name='Blood Pressure Monitoring', cost=150.00),
    LabTest(patient_id=1, test_name='Blood Test', test_date=datetime(2023, 10, 3), result='Normal')
])

session.commit()

# Close the session
session.close()
