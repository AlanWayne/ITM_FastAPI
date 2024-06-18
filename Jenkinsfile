pipeline {
    agent any
    stages {
        stage("hello world") {
            steps {
                sh '''
                    docker version
                    docker info
                    docker compose version
                    curl --version
                '''
            }
        }
    }
}