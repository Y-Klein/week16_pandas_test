from fastapi import FastAPI
import uvicorn
from dal import *


app = FastAPI()


@app.get("/employees/engineering/high-salary")
def q1():
    return get_engineering_high_salary_employees()
@app.get("/employees/by-age-and-role")
def q2():
    return get_employees_by_age_and_role()

@app.get("/employees/top-seniority")
def q3():
    return get_top_seniority_employees_excluding_hr()

@app.get("/employees/age-or-seniority")
def q4():
    return get_employees_by_age_or_seniority()

@app.get("/employees/managers/excluding-departments")
def q5():
    return get_managers_excluding_departments()

@app.get("/employees/by-lastname-and-age")
def q6():
    return get_employees_by_lastname_and_age()


if __name__ == "__main__":
    uvicorn.run(app,port=8000)