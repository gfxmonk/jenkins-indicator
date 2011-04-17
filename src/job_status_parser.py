#!/usr/bin/env python

import urllib
from job import Job

class JobStatusParser:
    def __init__(self, base_uri, images, max_image_size):
        self.base_uri = base_uri
        self.images = images
        self.max_image_size = max_image_size

    def build(self, config):
        json_jobs = eval(urllib.urlopen(self.base_uri).read()).get("jobs")
        jobs = []
        for json_job in json_jobs:
            job = Job(json_job.get("name")[0:20], json_job.get("color"), json_job.get("url"), config, self.images, self.max_image_size)
            jobs.append(job)
        return jobs

