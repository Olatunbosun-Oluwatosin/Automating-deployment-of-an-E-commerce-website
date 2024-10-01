# Automating-deployment-of-an-E-commerce-website


### _Jenkins Installation_
![](./img/01.%20jenkin.png)

This shows that Jenkins was installed successfully on the Ubuntu server and reachable on the browser as seen in the image. We can then move forward to create our first pipeline job according to the task in the exercise given.

### _Dependencies for the jenkins CI/CD pipeline job_
![](./img/02.%20project-dependencies.png)
As seen in the image shared, there are few dependencies (java, git and docker) that must be installed for Jenkins server to run smoothly without issue on the server. Also because Jenkins is plugins dependent, we are also mandated to install git plugin, docker pipeline plugin and others.

### _Github webhook_
![](./img/03.%20github-webhook.png)
Github webhook is setup such that when there is any push into the repository, the build job is triggered automatically to run by itself and that exemplify continuous integration & deployment. This is setup both on github repository and on jenkins platform.

### _Docker image push to docker hub_
![](./img/04.%20docker-image-push.png)
After several attempts to push the docker image automatically with the jenkinsfile but failed, i have to resolved to pushing it manually using the same credentials via the local machine and it was successful as seen in the image.

### _Pipeline job completed_
![](./img/05.%20pipeline-job-finished.png)
After several tries, i was able to completed the build job with a success as seen in the image. This came after several failures.

### _Build job_
![](./img/06.%20jenkins-build-successfully.png)
