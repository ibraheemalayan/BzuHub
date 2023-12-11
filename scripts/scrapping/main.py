from bs4 import BeautifulSoup
from dataclasses import dataclass, asdict
import json
import re



@dataclass
class Program:
    name_en: str
    name_ar: str
    code: str
    
    
@dataclass
class Department:
    name_en: str
    name_ar: str
    programs: list[Program]

@dataclass
class Faculty:
    name_en: str
    name_ar: str
    departments: list[Department]
    uncat_programs: list[Program] = None
    
    
with open('index_ar.html', 'r', encoding='utf-8') as file:
    bs4_ar = BeautifulSoup(file, 'html.parser', from_encoding='utf-8')
with open('index_en.html', 'r', encoding='utf-8') as file:
    bs4_en = BeautifulSoup(file, 'html.parser', from_encoding='utf-8')
faculties = zip(bs4_en.find_all(class_='lvl2'), bs4_ar.find_all(class_='lvl2'))
faculties_list = []
for faculty_en, faculty_ar in faculties:
    faculty_en_name = faculty_en.find(class_='head2').text.strip()
    faculty_ar_name = faculty_ar.find(class_='head2').text.strip()
    departments = zip(faculty_en.find_all(class_='lvl3'), faculty_ar.find_all(class_='lvl3'))
    departments_list = []
    uncat_programs = []
    for department_en, department_ar in departments:
        department_en_name = department_en.find(class_='head3').text.strip()
        department_ar_name = department_ar.find(class_='head3').text.strip()
        if bool(re.search(r'[a-zA-Z]', department_ar_name)):
            program_en_name = department_en_name
            program_ar_raw = department_ar_name
            program_code = re.sub(r'[^A-Za-z]+', '', program_ar_raw)
            program_ar_name = re.sub(r'[A-Za-z]+', '', program_ar_raw)
            uncat_programs.append(Program(name_en=program_en_name, name_ar=program_ar_name, code=program_code))
            continue
        programs_list = []
        programs = zip(department_en.find_all(class_='lvl4'), department_ar.find_all(class_='lvl4'))
        for program_en, program_ar in programs:
            program_en_name = program_en.find(class_='head4').text.strip()
            program_ar_raw = program_ar.find(class_='head4').text.strip()

            program_code = re.sub(r'[^A-Za-z]+', '', program_ar_raw)
            program_ar_name = re.sub(r'[A-Za-z]+', '', program_ar_raw)
            programs_list.append(Program(name_en=program_en_name, name_ar=program_ar_name, code=program_code))
        departments_list.append(Department(name_en=department_en_name, name_ar=department_ar_name, programs=programs_list))
    faculties_list.append(Faculty(name_en=faculty_en_name, name_ar=faculty_ar_name, departments=departments_list, uncat_programs=uncat_programs))
        

with open('data_uncat.json', 'w', encoding='utf-8') as file:
    json.dump([asdict(faculty) for faculty in faculties_list], file, ensure_ascii=False, indent=4)