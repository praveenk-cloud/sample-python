
pipeline {

    agent {
        label 'agent-node'
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t myapp .'
            }
        }

        stage('Deploy Application') {
            steps {
                sh 'docker rm -f myapp-container || true'

                sh '''
                    docker run -d \
                    --name myapp-container \
                    -p 80:80 \
                    myapp
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh 'docker ps'
            }
        }
    }
}
