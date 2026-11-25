pipeline {
    agent {
        label 'agent-node'
    }

    stages {
        stage('Check Docker Permission') {
            steps {
                sh '''
                    whoami
                    id
                    docker ps
                '''
            }
        }
    }
}
