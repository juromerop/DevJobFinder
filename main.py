from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = "Jobs API"

fakeJobsDB = [ {"job_title" : "Junior dev"}, {"job_title" : "Senior dev"}, {"job_title" : "DevOps"}, {"job_title" : "Tech lead"} ]

@app.get("/jobs", tags=["jobs"])
async def get_jobs():
    return HTMLResponse('<h1>Jobs API</h1>')