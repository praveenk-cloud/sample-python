pipeline{
    agent any
    stages{
        stage('checkout'){
            steps {
                echo 'downloading scm'
                checkout scm

            }
        }
        stage('build') {
            steps {
                echo 'build docker image'
                sh 'sudo docker build -t python-image .'
            }
        }
        stage('deploy'){
            steps {
                echo 'deploy the image'
                sh 'sudo docker run -dit --name c1 -p 80:80 python-image '
            }
        }
    }
}