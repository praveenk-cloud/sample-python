
pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                echo 'Starting application build'
                sh 'pwd'
                sh 'ls -l'
            }
        }

        stage('Test') {
            steps {
                echo 'Running Python application'
                sh 'python3 app.py'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Application deployment completed'
            }
        }

    }
}
