
pipeline {
  environment {
    registry = "dithicus/caltech_devops_project"
    registryCredential = 'dockerhub'
    dockerImage = ''
  }
  agent any
  stages {
    stage('Cloning Git') {
      steps {
        checkout scm
      }
    }
    stage('Run Unit Tests') {
      steps {
        bat "python test_app.py"
      }
    }
  }
}