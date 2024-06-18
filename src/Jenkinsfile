pipeline {
    agent any

    stages {
        stage("hello world") {
            steps {
                sh 'docker version'
                sh 'docker-compose version'
            }
        }
    
        stage('Prune Docker data') {
            steps {
                sh 'docker system prune -a --volumes -f'
            }
        }

        stage('Start container') {
            steps {
                sh 'docker-compose up -d --no-color --wait'
                sh 'docker-compose ps'
            }
        }

        stage('Run tests against the container') {
            steps {
                sh 'curl http://localhost:3000/param?query=demo | jq'
            }
        }
    }

    post {
        always {
            sh 'docker-compose down --remove-orphans -v'
            sh 'docker-compose ps'
        }
    }
}