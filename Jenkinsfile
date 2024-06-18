pipeline {
    agent any
    stages {
        stage("hello world") {
            steps {
                sh '''
                    sudo docker version
                    sudo docker info
                    sudo docker compose version
                    curl --version
                '''
            }
        }
    }
}