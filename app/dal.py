from connection import collection


def get_engineering_high_salary_employees():
    result = []
    cursor = collection.find(
        {"job_role.department":"Engineering","salary":{"$gt":65000}},
        {"employee_id":1,"name":1,"salary":1,"_id":0})
    for doc in cursor:
        result.append(doc)
    return result

def get_employees_by_age_and_role():
    result = []
    cursor = collection.find(
        {"age":{"$gte":30,"$lte":40},
         "$or": [{"job_role.title": "Engineer"}, {"job_role.title": "Specialist"}]},
        {"_id": 0})
    for doc in cursor:
        result.append(doc)
    return result

def get_top_seniority_employees_excluding_hr():
    result = []
    cursor = collection.find(
        {"job_role.department":{"$ne":"HR"}},
        {"_id": 0}).sort("years_at_company",-1).limit(7)
    for doc in cursor:
        result.append(doc)
    return result

def get_employees_by_age_or_seniority():
    result = []
    cursor = collection.find(
        {"$or":[{ "age": {"$gt":50}},{"years_at_company":{"$lt":3}}]},
        {"employee_id": 1, "name": 1, "age": 1,"years_at_company":1 ,"_id": 0})
    for doc in cursor:
        result.append(doc)
    return result


def get_managers_excluding_departments():
    result = []
    cursor = collection.find(
        {"job_role.title": "Manager","job_role.department":{"$nin":["Sales","Marketing"]}},
        {"_id": 0})
    for doc in cursor:
        result.append(doc)
    return result

def get_employees_by_lastname_and_age():
    result = []
    cursor = collection.find(
        {"age":{"$lt":35},"name":{"$in":["Wright","Nelson"]}},
        {"name": 1,"age":1,"job_role.department":1,"_id": 0})
    for doc in cursor:
        result.append(doc)
    return result

