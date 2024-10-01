pipeline {
    agent any

    environment {
        DOCKER_REGISTRY = "docker.io"
        IMAGE_NAME = "tosyeno/my-flask-app"  
        IMAGE_TAG = "${env.BUILD_NUMBER}"
        DOCKER_CREDENTIALS_ID = "ef0373b9-d3d0-479b-80a5-3b1b11bd3c9f"  // Update with your actual credentials ID
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
                    // Run the built Docker container, exposing the app on port 9090
                    dockerImage.run('-d -p 9090:80')
                }
            }
        }

        stage('Access Web Application') {
            steps {
                script {
                    // Perform a basic check to see if the web app is accessible on port 9090
                    sh 'sleep 10'  // Allow some time for the container to start
                    sh 'curl http://localhost:8080'  // Updated to port 9090, since the app is being exposed on port 9090
                }
            }
        }

        stage('Push Docker Image to Registry') {
            steps {
                script {
                    // Log in to Docker Hub and push the Docker image to the registry
                    docker.withRegistry("https://${DOCKER_REGISTRY}", "${DOCKER_CREDENTIALS_ID}") {
                        dockerImage.push("${IMAGE_TAG}")  // Push the image with the current build tag
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
