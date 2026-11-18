pipeline{
    agent {
        label 'linux-agent-1'
    }
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
                sh 'docker build -t python-image .'
            }
        }
        stage('deploy'){
            steps {
                echo 'deploy the image'
                sh 'docker rm -f c1 || true'
                sh 'docker run -dit --name c1 -p 80:80 python-image '
            }
        }
    }
}
