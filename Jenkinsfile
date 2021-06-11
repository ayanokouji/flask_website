
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
    stage('Building image') {
      steps{
        script {
          dockerImage = docker.build "dithicus/caltech_devops_project" + ":$BUILD_NUMBER"
        }
      }
    }
    stage('Deploy Image') {
      steps{
        script {
          docker.withRegistry( 'https://registry-1.docker.io/v2/', 'dockerhub' ) {
            dockerImage.push()
          }
        }
      }
    }
  }
}