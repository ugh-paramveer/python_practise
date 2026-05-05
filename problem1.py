# Problem #1 — Grader
# Write a function that takes a list of student scores and returns a dict with each student's grade.

def rank(students:list[dict])->dict:
   rank={}
   for student in students :
      name=student["name"]
      if 100>=student["score"]>=90:
        #  rank.append({"name":"A"})#to add list of dict [{}]add braces
        rank[name] = "A" #rank[name] = "A"  better vrsion
      elif 89>=student["score"]>=80:
         rank[name] = "B" #rank[name] = "A"
      elif 79>=student["score"]>=70:
         rank[name] = "C" #rank[name] = "A"
      elif 69>=student["score"]>=60:
         rank[name] = "D" #rank[name] = "A"
      elif student["score"]<60:
         rank[name] = "F" #rank[name] = "A"
      else:
         raise ValueError("invalid number or chracter")
   return rank  

students = [
    {"name": "Param", "score": 85},
    {"name": "Raj",   "score": 52},
    {"name": "Priya", "score": 73},
    {"name": "Amit",  "score": 91},
]
new=rank(students)

for nme in new:
   print(f"{nme}:{new[nme]}")