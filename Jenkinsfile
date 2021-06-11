
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
        sh 'python test_app.py'
      }
    }
    stage('Building image') {
      steps{
        script {
          dockerImage = docker.build "dithicus/caltech_devops_project" + ":$BUILD_NUMBER"
        }
      }
    }
  }
}