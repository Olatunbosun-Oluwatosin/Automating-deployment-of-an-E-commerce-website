pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        git 'https://github.com/Olatunbosun-Oluwatosin/Automating-deployment-of-an-E-commerce-website.git'
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
  }
}
