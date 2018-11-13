# Copyright 2015-2015 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file
# except in compliance with the License. A copy of the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is distributed on an "AS IS"
# BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under the License.

import os
import string
import random
from locust import HttpLocust, TaskSet, task

class MyTaskSet(TaskSet):
# All instance targets
#    @task(1000)
#    def index(self):
#        self.client.get("/")
    @task(1000)
    def search(self):
        self.client.get("/catalog?locale=en&search_field=all_fields")

# Staging targets
#    @task(1000)
#    def concern1(self):
#        self.client.get("/concern/publications/5q47rn851?locale=en")

# Production targets
#    @task(1000)
#    def concern1(self):
#        self.client.get("/concern/publications/3t945q76s?locale=en")
#    @task(1000)
#    def concern2(self):
#        self.client.get("/concern/publications/8336h188j?locale=en")

    # This task will 15 times for every 1000 runs of the above task
    # @task(15)
    # def about(self):
    #     self.client.get("/blog")

    # This task will run once for every 1000 runs of the above task
    # @task(1)
    # def about(self):
    #     id = id_generator()
    #     self.client.post("/signup", {"email": "example@example.com", "name": "Test"})

class MyLocust(HttpLocust):
    host = os.getenv('TARGET_URL', "http://localhost")
    task_set = MyTaskSet
    min_wait = 200
    max_wait = 200
