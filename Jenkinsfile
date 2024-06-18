pipeline {
    agent any
    stages {
        stage("hello world") {
            steps {
                sh '''
                    docker-compose version
                    curl --version
                '''
            }
        }
    }
}