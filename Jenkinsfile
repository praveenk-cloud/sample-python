
pipeline {
    agent {
        label 'agent-node'
    }

    stages {
        stage('Check Agent') {
            steps {
                sh '''
                    echo "Hello from Jenkins Agent!"
                    echo "Hostname:"
                    hostname
                    echo "Current User:"
                    whoami
                    echo "Current Directory:"
                    pwd
                '''
            }
        }

        stage('Create Folder') {
            steps {
                sh '''
                    mkdir -p ~/jenkins-deployment
                    echo "Folder created successfully!"
                    ls -ld ~/jenkins-deployment
                '''
            }
        }
    }
}
