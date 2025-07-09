pipeline {
    agent any

    environment {
        APP_MODE = 'production'
    }

    stages {
        stage('Clone Code') {
            steps {
                git 'https://github.com/roopalisabakale/flask-docker-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-docker-app .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker run -d -p 5000:5000 --name flask-container flask-docker-app'
            }
        }
    }
}
