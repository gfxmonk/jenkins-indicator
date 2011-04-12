#!/usr/bin/env python

import urllib

class JobStatus:
    base_uri = "http://localhost:8080/jenkins/api/python"

    def build(self):
        json_jobs = eval(urllib.urlopen(self.base_uri).read()).get("jobs")
        jobs = []
        for json_job in json_jobs:
            jobs.append(Job(json_job.get("name")[0:20], json_job.get("color"), json_job.get("url")))
        return jobs

class Job:
    def __init__(self, name, color, url):
        self.name = name
        self.color = color
        self.url = url

if __name__ == '__main__':
    parser = JobStatus()
    jobs = parser.build()
    for job in jobs:
        print("name: "+job.name+", "+job.color)