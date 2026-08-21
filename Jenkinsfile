pipeline {

    agent any

    tools {
        maven 'maven'
    }

    stages {

        stage('Build') {
            steps {
                sh 'mvn clean package'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh '''
                    mvn sonar:sonar \
                    -Dsonar.projectKey=devops-handson-activities
                    '''
                }
            }
        }

        stage('Upload Artifact to Nexus') {
            steps {
                sh 'mvn deploy'
            }
        }

        stage('Docker Build') {
            steps {
                sh '''
                docker build -t microservice-demo:v1 .
                '''
            }
        }

        stage('Trivy Scan') {
            steps {
                sh '''
                trivy image --severity HIGH,CRITICAL microservice-demo:v1
                '''
            }
        }

        stage('Run Application') {
            steps {
                sh '''
                nohup java -jar target/*.jar > app.log 2>&1 &
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
