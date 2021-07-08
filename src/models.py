import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String,Boolean,Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    full_name = Column(String(120), unique=False, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(80), unique=False, nullable=False)
    is_active = Column(Boolean(), unique=False, nullable=False)
    promo = Column(Boolean(), unique=False, nullable=False)
    img = Column(String(250), unique=True, nullable=False)
    school = relationship(
    "School",
    secondary=association_table,
    back_populates="school")
    

class Teacher(Base):
    __tablename__ = 'teacher'
    id = Column(Integer, primary_key=True)
    full_name = Column(String(120), unique=False, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(80), unique=False, nullable=False)
    type_of_teacher = Column(String(80), unique=False, nullable=False)
    linkedin = Column(String(80), unique=False, nullable=False)
    is_active = Column(Boolean(), unique=False, nullable=False)
    promo = Column(Boolean(), unique=False, nullable=False)
    img = Column(String(250), unique=True, nullable=False)
    school = relationship(  
    "School",
    secondary=association_table,
    back_populates="school")

class School(Base):
    __tablename__ = 'school'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=False, nullable=False)
    img = Column(String(250), unique=True, nullable=False)
    students = relationship(
    "Student",
    secondary=association_table,
    back_populates="student")
    teachers =  relationship(  
    "Teacher",
    secondary=association_table,
    back_populates="teacher")
  
    

school_student = Table('school_student', Base.metadata,
    Column('student_id', Integer, ForeignKey('student.id')),
    Column('school_id', Integer, ForeignKey('school.id'))
)
teacher_student = Table('teacher_student', Base.metadata,
    Column('teacher_id', Integer, ForeignKey('teacher.id')),
    Column('school_id', Integer, ForeignKey('school.id'))
)


def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e