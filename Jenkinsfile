pipeline {
    agent any
    
    tools {
        nodejs "NodeJS-Tool" // The name you configured in Global Tool Configuration
    }
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Olatunbosun-Oluwatosin/Automating-deployment-of-an-E-commerce-website.git'
            }
        }
        
        stage('Build') {
            steps {
                sh 'npm install'
            }
        }
        
        stage('Test') {
            steps {
                sh 'npm test'
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Deploying the application...'
            }
        }
    }
}
