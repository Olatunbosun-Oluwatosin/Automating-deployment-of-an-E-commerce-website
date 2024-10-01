pipeline {
    agent any

    environment {
        DOCKER_REGISTRY = "docker.io"
        IMAGE_NAME = "tosyeno/my-flask-app"  
        IMAGE_TAG = "${env.BUILD_NUMBER}"
        DOCKER_CREDENTIALS_ID = "docker_credentials_id"
    }

    stages {
        stage('Clone Repository') {
            steps {
                // Clone the repository that contains the Dockerfile and the source code
                git branch: 'main', url: 'https://github.com/Olatunbosun-Oluwatosin/Automating-deployment-of-an-E-commerce-website.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image using the Dockerfile in the cloned repository
                    dockerImage = docker.build("${DOCKER_REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG}")
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Run the built Docker container, exposing the app on port 8080
                    dockerImage.run('-d -p 9090:80')
                }
            }
        }

        stage('Access Web Application') {
            steps {
                script {
                    // Perform a basic check to see if the web app is accessible on port 8080
                    sh 'sleep 10'  // Allow some time for the container to start
                    sh 'curl http://localhost:8080'
                }
            }
        }

        stage('Push Docker Image to Registry') {
            steps {
                script {
                    // Push the Docker image to the registry
                    docker.withRegistry("https://${DOCKER_REGISTRY}", "${DOCKER_CREDENTIALS_ID}") {
                        dockerImage.push("${IMAGE_TAG}")
                    }
                }
            }
        }
    }

    post {
        always {
            cleanWs() // Clean the workspace after build
        }
        success {
            echo 'Build and deployment successful!'
        }
        failure {
            echo 'Build or deployment failed!'
        }
    }
}
