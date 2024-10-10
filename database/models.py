# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  October 10, 2024 13:23:24
# Database: sqlite:////tmp/tmp.onWidDoUuo/doctor/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Department(SAFRSBaseX, Base):
    """
    description: Information about hospital departments.
    """
    __tablename__ = 'departments'
    _s_collection_name = 'Department'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    NurseList : Mapped[List["Nurse"]] = relationship(back_populates="department")
    RoomList : Mapped[List["Room"]] = relationship(back_populates="department")



class Doctor(SAFRSBaseX, Base):
    """
    description: Stores doctor information.
    """
    __tablename__ = 'doctors'
    _s_collection_name = 'Doctor'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    specialty = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    AppointmentList : Mapped[List["Appointment"]] = relationship(back_populates="doctor")



class Patient(SAFRSBaseX, Base):
    """
    description: Stores patient information.
    """
    __tablename__ = 'patients'
    _s_collection_name = 'Patient'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    dob = Column(DateTime, nullable=False)
    gender = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    AppointmentList : Mapped[List["Appointment"]] = relationship(back_populates="patient")
    BillingList : Mapped[List["Billing"]] = relationship(back_populates="patient")
    InsuranceList : Mapped[List["Insurance"]] = relationship(back_populates="patient")
    LabTestList : Mapped[List["LabTest"]] = relationship(back_populates="patient")
    MedicalRecordList : Mapped[List["MedicalRecord"]] = relationship(back_populates="patient")



class Appointment(SAFRSBaseX, Base):
    """
    description: Stores appointment details.
    """
    __tablename__ = 'appointments'
    _s_collection_name = 'Appointment'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    patient_id = Column(ForeignKey('patients.id'), nullable=False)
    doctor_id = Column(ForeignKey('doctors.id'), nullable=False)
    appointment_date = Column(DateTime, nullable=False)
    notes = Column(String)

    # parent relationships (access parent)
    doctor : Mapped["Doctor"] = relationship(back_populates=("AppointmentList"))
    patient : Mapped["Patient"] = relationship(back_populates=("AppointmentList"))

    # child relationships (access children)
    PrescriptionList : Mapped[List["Prescription"]] = relationship(back_populates="appointment")



class Billing(SAFRSBaseX, Base):
    """
    description: Manages billing information.
    """
    __tablename__ = 'billing'
    _s_collection_name = 'Billing'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    patient_id = Column(ForeignKey('patients.id'), nullable=False)
    amount_due = Column(Float, nullable=False)
    due_date = Column(DateTime, nullable=False)
    paid_date = Column(DateTime)

    # parent relationships (access parent)
    patient : Mapped["Patient"] = relationship(back_populates=("BillingList"))

    # child relationships (access children)



class Insurance(SAFRSBaseX, Base):
    """
    description: Stores insurance details for patients.
    """
    __tablename__ = 'insurances'
    _s_collection_name = 'Insurance'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    patient_id = Column(ForeignKey('patients.id'), nullable=False)
    provider_name = Column(String, nullable=False)
    policy_number = Column(String, nullable=False)

    # parent relationships (access parent)
    patient : Mapped["Patient"] = relationship(back_populates=("InsuranceList"))

    # child relationships (access children)



class LabTest(SAFRSBaseX, Base):
    """
    description: Records laboratory tests results.
    """
    __tablename__ = 'lab_tests'
    _s_collection_name = 'LabTest'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    patient_id = Column(ForeignKey('patients.id'), nullable=False)
    test_name = Column(String, nullable=False)
    test_date = Column(DateTime, nullable=False)
    result = Column(String)

    # parent relationships (access parent)
    patient : Mapped["Patient"] = relationship(back_populates=("LabTestList"))

    # child relationships (access children)



class MedicalRecord(SAFRSBaseX, Base):
    """
    description: Stores medical records for each patient.
    """
    __tablename__ = 'medical_records'
    _s_collection_name = 'MedicalRecord'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    patient_id = Column(ForeignKey('patients.id'), nullable=False)
    diagnosis = Column(String)
    treatment = Column(String)
    record_date = Column(DateTime, nullable=False)

    # parent relationships (access parent)
    patient : Mapped["Patient"] = relationship(back_populates=("MedicalRecordList"))

    # child relationships (access children)
    TreatmentList : Mapped[List["Treatment"]] = relationship(back_populates="medical_record")



class Nurse(SAFRSBaseX, Base):
    """
    description: Stores nurse information.
    """
    __tablename__ = 'nurses'
    _s_collection_name = 'Nurse'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    department_id = Column(ForeignKey('departments.id'))

    # parent relationships (access parent)
    department : Mapped["Department"] = relationship(back_populates=("NurseList"))

    # child relationships (access children)



class Room(SAFRSBaseX, Base):
    """
    description: Contains details about hospital rooms.
    """
    __tablename__ = 'rooms'
    _s_collection_name = 'Room'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    room_number = Column(String, nullable=False)
    department_id = Column(ForeignKey('departments.id'))
    type = Column(String)

    # parent relationships (access parent)
    department : Mapped["Department"] = relationship(back_populates=("RoomList"))

    # child relationships (access children)



class Prescription(SAFRSBaseX, Base):
    """
    description: Contains prescription data.
    """
    __tablename__ = 'prescriptions'
    _s_collection_name = 'Prescription'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    appointment_id = Column(ForeignKey('appointments.id'), nullable=False)
    medication_name = Column(String, nullable=False)
    dosage = Column(String)
    instructions = Column(String)

    # parent relationships (access parent)
    appointment : Mapped["Appointment"] = relationship(back_populates=("PrescriptionList"))

    # child relationships (access children)



class Treatment(SAFRSBaseX, Base):
    """
    description: Details of treatments given to patients.
    """
    __tablename__ = 'treatments'
    _s_collection_name = 'Treatment'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    medical_record_id = Column(ForeignKey('medical_records.id'), nullable=False)
    treatment_name = Column(String, nullable=False)
    cost = Column(Float, nullable=False)

    # parent relationships (access parent)
    medical_record : Mapped["MedicalRecord"] = relationship(back_populates=("TreatmentList"))

    # child relationships (access children)
